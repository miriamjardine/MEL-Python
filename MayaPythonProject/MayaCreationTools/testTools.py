import maya.cmds as cmds

def select_SpecifiedType():
    specified_sels = cmds.ls(type='parentConstraint')
    cmds.select(specified_sels, r=True)

select_SpecifiedType()

def constrain_basic():

    #select ctrl and then jnt

    sels = cmds.ls(sl=True)
    first_sel = sels[0]
    second_sel = sels[1]

    # create constraints

    cmds.parentConstraint(first_sel, second_sel, maintainOffset=True, weight=1) #parent constraint
    cmds.scaleConstraint(first_sel, second_sel, maintainOffset=True, weight=1) #scale constraint

constrain_basic()

