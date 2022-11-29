# Class practice

# def test_function(name, number, message):
#   print('%s threw a ball %i feet. %s' % (name, number, message))
# test_function('Mary', 50, 'Congrats.')

# Random Placement Generator

import maya.cmds as cmds
import random

def random_placement(dup_number, min_x, max_x, min_y, max_y, min_z, max_z):
    selected_objs = cmds.ls(sl=True)

    for obj in selected_objs:
        for times in range(dup_number):
            dup_obj = cmds.duplicate(obj, rr=True)[0] #[0] takes the obj out of the list

            temp = [min_x, max_x]
            temp.sort() # this makes it idiot proof. min will always be lower than max.
            pos_x = random.uniform(temp[0], temp[1])
            temp = [min_y, max_y]
            temp.sort()
            pos_y = random.uniform(temp[0], temp[1])
            temp = [min_z, max_z]
            temp.sort()
            pos_z = random.uniform(temp[0], temp[1])

            cmds.xform(dup_obj, translation=[pos_x,pos_y,pos_z], ws=True)

random_placement(500, 7, 300, 9, 32, 17, 84)