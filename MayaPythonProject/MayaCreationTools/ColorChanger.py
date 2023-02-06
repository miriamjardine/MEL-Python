import maya.cmds as cmds

sels = cmds.ls(type='nurbsCurve')

color = int(input())

for sel in sels:
    cmds.setAttr(sel + ".overrideEnabled ", 1)
    cmds.setAttr(sel + ".overrideColor", color)
