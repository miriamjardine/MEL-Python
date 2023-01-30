import maya.cmds as cmds
# in class work with professor

def create_joints():
    sels = cmds.ls(sl=True)
    joints = []

    cmds.select(clear=True)
    for sel in sels:
        cmds.select(clear=True)
        xform_data = get_xform(sel)

        joint = cmds.joint(position=xform_data[0], absolute=True)
        joints.append(joint)

    cmds.select(joints, replace=True)
    return joints

def create_controls(shape='circle'):
    '''
    Creates controls on obj(s) selected
    return: [controls]
    '''
    sels = cmds.ls(sl=True)
    ctrls = []

    for sel in sels:
        cmds.select(clear=True)

        if shape is 'circle':
            ctrl = cmds.circle(center=[0,0,0],
                                    normal=[1,0,0],
                                    sweep=360,
                                    radius=1,
                                    degree=3,
                                    ut=0,
                                    tolerance=.01,
                                    sections=8,
                                    constructionHistory=True)[0]
#       You can add elif statements for different shapes
        
        else:
            cmds.error('%s not valid arguement' % (shape))

        xform_data = get_xform(sel)

        cmds.xform(ctrl,
                   worldSpace=True,
                   translation=xform_data[0],
                   rotation=xform_data[1],
                   scale=xform_data[2])

        prefix = sel.rpartition('_Jnt')[0]
        ctrl = cmds.rename(ctrl, '%s_Ctrl' % (prefix))

        ctrl = group(ctrl)[0]
        ctrls.append(ctrl)

    cmds.select(ctrls, r=True)

    return ctrls

def get_xform(obj):
    '''
    Returns the transformation data for the object passed as the argument.
    Return: [position, rotation, scale]
    '''
    pos = cmds.xform(obj, q=True, translation=True, worldSpace=True)
    rot = cmds.xform(obj, q=True, rotation=True, worldSpace=True)
    scale = cmds.xform(obj, q=True, scale=True, worldSpace=True)

    return ([pos, rot, scale])

def group(obj):
    '''
    Create a new parent group at transformations of objs
    return: [obj, group]
    '''
    xform_data = get_xform(obj)

    parent = cmds.listRelatives(obj, parent=True, fullPath=True)

    cmds.select(cl=True)

    grp = cmds.group(world=True, empty=True)
    cmds.rename(grp, '%s_Grp' % (obj))
    cmds.xform(group,
               worldSpace=True,
               translation=xform_data[0],
               rotation=xform_data[1],
               scale=xform_data[2])
    if parent:
        grp = cmds.parent(grp, parent[0])[0]
    obj = cmds.parent(obj, grp)[0]
    cmds.select(obj, r=True)
    return [obj, grp]

create_joints()
create_controls()