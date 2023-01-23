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

def create_controls():
    sels = cmds.ls(sl=True)
    ctrls = []

    for sel in sels:
        cmds.select(clear=True)
        ctrl = cmds.circle(center=[0,0,0],
                                normal=[0,1,0],
                                sweep=360,
                                radius=1,
                                degree=3,
                                ut=0,
                                tolerance=.01,
                                sections=8,
                                constructionHistory=True)[0]
        ctrls.append(ctrl)

        xform_data = get_xform(sel)

        cmds.xform(ctrl,
                   worldSpace=True,
                   translation=xform_data[0],
                   rotation=xform_data[1],
                   scale=xform_data[2])
    cmds.select(ctrls, r=True)

    return ctrls

def get_xform(obj):
    '''
    Returns the transformation data for the object passed as the argument.
    Return: [position, rotation, scale]
    '''
    pos = cmds.xform(obj, q=True, translation=True, worldSpace=True)
    rot = cmds.xform(obj, q=True, translation=True, worldSpace=True)
    scale = cmds.xform(obj, q=True, translation=True, worldSpace=True)

    return ([pos, rot, scale])

create_joints()
create_controls()