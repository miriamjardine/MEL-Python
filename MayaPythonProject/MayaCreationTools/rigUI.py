import maya.cmds as cmds

def btn_joint():
    import jointAndCtrlCreationTools
    jointAndCtrlCreationTools.create_joints()

def btn_group():
    import jointAndCtrlCreationTools
   # jointAndCtrlCreationTools.group()


window = 'rigToolUI'

if cmds.window(window, q=True, exists=True):
    cmds.deleteUI(window)

window = cmds.window(window,
            widthHeight=(400, 200),
            sizeable=True,
            title="Rig Tools")
m_column = cmds.columnLayout(parent=window,
                  adjustableColumn=True)

cmds.button(parent=m_column,
            label='Create Joint',
            command=btn_joint())
cmds.button(parent=m_column,
            label='Parent Group',
            command=btn_group())

cmds.showWindow(window)
