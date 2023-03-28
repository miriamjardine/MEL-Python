import maya.cmds as cmds

#created using the guidance of professor Clayton Lantz
# this script constrains the ctrls to the ctrl system. Not to the joints.

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
    cmds.scaleConstraint(parent_ctrl, child_ctrl_grp, weight=1)

    # create attributes on the child ctrl

    if not cmds.attributeQuery('FollowTranslate', node=child_ctrl, exists=True):
        cmds.addAttr(child_ctrl,
                     longName='FollowTranslate',
                     attributeType='double',
                     minValue=0,
                     maxValue=1,
                     defaultValue=1,)
        cmds.setAttr(('%s.FollowTranslate' % (child_ctrl)),
                     e=True,
                     keyable=True,)


    if not cmds.attributeQuery('FollowRotate', node=child_ctrl, exists=True):
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

def constrain_ctrl_basic():

    #select ctrl and then jnt

    sels = cmds.ls(sl=True)
    ctrl_sel = sels[0]
    jnt_sel = sels[1]

    # create constraints

    cmds.parentConstraint(ctrl_sel, jnt_sel, maintainOffset=True, weight=1) #parent constraint
    cmds.scaleConstraint(ctrl_sel, jnt_sel, maintainOffset=True, weight=1) #scale constraint

constrain_ctrl_basic()


