import selectionMenu as sm
import savingSystem as ss
import os
import inputOptions as iopt

def sortingAlgorithm(finalDir, fileTypes, searchDir):
    files = os.listdir(searchDir)
    for i in files:
        fileSplit = [str(x) for x in i.split(".")]
        try:
            if fileSplit[1] in fileTypes:
                print(i)
                os.rename(searchDir + "\\" + i, finalDir + "\\" + i)
        except:
            pass
    print()


def runSortingAlgorithm(configName):
    data = ss.readConfig(configName)
    finalDirectory = data[0]
    fileTypes = [str(x) for x in data[1].split("<>")]
    searchDirectories = [str(x) for x in data[2].split("<>")]
    for i in searchDirectories:
        if len(i) > 1:
            print(i + " moving files to " + finalDirectory)
            print()
            sortingAlgorithm(finalDirectory, fileTypes, str(i))
    iopt.option_choice("The sorting algorithm has run succesfully :3\nPress ENTER to continue")



cmd1 = "run"
cmd2 = "add"
cmd3 = "edit"
cmd4 = "remove"
cmd5 = "exit"

def mainLoop():
    running = True
    while running:
        MainMenu.l = ss.listConfigFiles()
        answer = MainMenu.mainLoop()
        try:
            if answer[0] == cmd1:
                runSortingAlgorithm(answer[1])
            elif answer[0] == cmd2:
                ss.addConfig(answer[1])
                pass
            elif answer[0] == cmd3:
                ss.editConfig(answer[1])
                pass
            elif answer[0] == cmd4:
                ss.removeConfig(answer[1])
            elif answer[0] == cmd5:
                running = False
            else:
                pass
        except IndexError:
            pass

MainMenu = sm.SelectionMenu()
MainMenu.titleText = "F.S.S. - File Sorting System"
MainMenu.desc = "Program that automates file sorting. :O\nDown below you can select which action to perform."
MainMenu.options = f"{cmd1} (config name) - to run the algorithm\n{cmd2} (config name) - to sort with that config\n{cmd3} (config name) - to edit config\n{cmd4} - to remove config\n{cmd5} - to close program"
MainMenu.isSingleOption = False
MainMenu.useList = True


mainLoop()