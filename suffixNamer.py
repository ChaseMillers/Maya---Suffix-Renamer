"""
This utility lets you add any suffix of choice to selected objects.
This was built to quickly prep for low and high baking in Substance but can be used for any purpose.

Instructions:
1. *Windows- Place script file in: C:\Users\NAME\Documents\maya\2019\scripts

2. copy paste into python console -
import suffixNamer
reload(suffixNamer)
suffixNamer.Suffix().show()

3. Highlight, then middle mouse drag code to shelf
"""

from maya import cmds


class BaseWindow(object):
    windowTitle = 'Suffix Naming'
    def show(self):
        self.windowID = "myWindowID"

        if cmds.window(self.windowID, title=self.windowTitle, exists=True):
            cmds.deleteUI( self.windowID )

        cmds.windowPref(self.windowID, remove=True)
        cmds.window(self.windowID, title=self.windowTitle ,w=205, h=60)
        self.buildUI()
        cmds.showWindow()

    def close(self, *args):
        cmds.deleteUI(self.windowID)

class Suffix(BaseWindow):
    def buildUI(self):
        cmds.rowColumnLayout(numberOfColumns=3, columnWidth=[(1, 80), (2, 60), (3, 60)])
        cmds.separator(style=None, h=5), cmds.separator(style=None, h=5), cmds.separator(style=None, h=5)
        # enter name
        cmds.text(label='    Suffix Name:  __  ')
        self.suffix_value = cmds.textField(text="low")

        cmds.button(label="Apply", command=self.rename)
        cmds.separator(style=None, h=10)
        cmds.button(label="Close", command=self.close, width = 120)

    def rename(self, *args):
        # check the suffix value
        suffix = cmds.textField(self.suffix_value, query=True, text=True)

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

