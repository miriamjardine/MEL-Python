import maya.cmds as cmds

size = 3
melt = 1.9

base = cmds.polySphere(sx=20, sy=20, r=size)

middle = cmds.polySphere(sx=20, sy=20, r=(size*.6))
cmds.move(0,(size*1.25),0,relative=True, objectSpace=True, worldSpaceDistance=True)

head = cmds.polySphere(sx=20, sy=20, r=(size*.3))
cmds.move(0,(size*2),0,relative=True, objectSpace=True, worldSpaceDistance=True)

cmds.polyCylinder( sx=20, sy=1, sz=1, h=1, radius=.4)
cmds.move(0,7.1,0,relative=True, objectSpace=True, worldSpaceDistance=True)

cmds.polyCylinder( sx=20, sy=1, sz=1, h=.2, radius=.75)
cmds.move(0,6.9,0,relative=True, objectSpace=True, worldSpaceDistance=True)

cmds.polyCone( sx=20, sy=1, sz=0, r=.2, h=1)
cmds.rotate( '90deg', 0, 0, r=True)
cmds.move(0,0,-6.1,relative=True, objectSpace=True, worldSpaceDistance=True)
cmds.move(0,1.2,0,relative=True, objectSpace=True, worldSpaceDistance=True)


