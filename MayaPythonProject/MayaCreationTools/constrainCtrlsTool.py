import maya.cmds as cmds

#created using the guidance of professor Clayton Lantz

def constrain_ctrls():
# make viewport selection, parent ctrl and then child ctrl


    # get selection, separate parent and child
    sels = cmds.ls(sl=True) #[parent control, child control]
    parent_ctrl = sels[0]
    child_ctrl = sels[1]

    # get the parent group of child ctrl
    child_ctrl_grp = cmds.listRelatives(child_ctrl, parent=True)[0] #[child ctrl's parent node]

    # create constraints
    p_constraint_trans = cmds.parentConstraint(parent_ctrl, child_ctrl_grp,
                                               maintainOffset=True,
                                               skipRotate=['x','y','z'],
                                               weight=1)[0] #translate constraint
    p_constraint_rot =cmds.parentConstraint(parent_ctrl, child_ctrl_grp,
                                            maintainOffset=True,
                                            skipTranslate=['x','y','z'],
                                            weight=1)[0] #rotate constraint

    # create attributes on the child ctrl

    cmds.addAttr(child_ctrl,
                 longName='FollowTranslate',
                 attributeType='double',
                 minValue=0,
                 maxValue=1,
                 defaultValue=1,)
    cmds.setAttr(('%s.FollowTranslate' % (child_ctrl)),
                 e=True,
                 keyable=True,)
    cmds.addAttr(child_ctrl,
                 longName='FollowRotate',
                 attributeType='double',
                 minValue=0,
                 maxValue=1,
                 defaultValue=1,)
    cmds.setAttr(('%s.FollowRotate' % (child_ctrl)),
                 e=True,
                 keyable=True,)

    # connect attributes from child ctrl to constraint weights

    cmds.connectAttr('%s.FollowTranslate' % (child_ctrl),
                    '%s.w0' % (p_constraint_trans),
                    f=True)

    cmds.connectAttr('%s.FollowRotate' % (child_ctrl),
                        '%s.w0' % (p_constraint_rot),
                        f=True)

constrain_ctrls()



