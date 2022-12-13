import maya.cmds as cmds

txt = input()
sels = cmds.ls(sl=True)

for i, sel in enumerate(sels):
    count = txt.count('#')
    x = txt.find("#" * count)
    if x == 0:
        cmds.error('# must be consecutive.')
    if count == 0:
        cmds.error('Must enter # as digit')

    y = txt.rpartition("#" * count)
    num = i+1
    str_num = str(num)
    digit = str_num.zfill(count)
    middle = txt.replace("#"*count, digit)
    cmds.rename(sel, middle)
