"""
This utility lets you add any suffix of choice to selected objects.
This was built to quickly prep for low and high baking in Substance but can be used for any purpose.
"""

from maya import cmds

def rename(suffix=None):
    """
    Author: Chase Miller

    This function will rename selected objects to have suffix of choice.
    Args:
        suffix: Suffix name that will be added to objects current name.

    Returns:
        A list of all objects operated on and name with added suffix.

    How to use:
    After installed
    Run this in the Python Console:

    import substanceSuffix
    reload (substanceSuffix)
    substanceSuffix.rename(suffix='VALUE')

    #NOTE: Be sure to change VALUE with name of choice
    """

    # If set to false, user wont have to select anything.
    selection = True
    objects = cmds.ls(selection=True, dag=True, long=True)
    print "You sellected", objects

    if selection and not objects:
        raise RuntimeError("You didn't select anything! Sellect the object you wish to add a suffix to.")
    objects.sort(key=len, reverse=True)

    for obj in objects:
        # grabs last name listed separated by "|".
        shortName = obj.split('|')[-1]

        # If no suffix was entered
        if not suffix:
            raise RuntimeError("You need to enter a suffix name. EXAMPLE: substanceSuffix.rename(suffix='high'). ")

        if obj.endswith('_'+suffix):
            print shortName+" already had that suffix, so it was skipped."
            continue

        newName = shortName+"_"+suffix

        cmds.rename(obj, newName)

        print "new name: ", newName
