import os
import inputOptions as iOpt
import selectionMenu as sm

program_loc = "C:\Code\PY\Projects\FileSorter"

def listConfigFiles():
    files = os.listdir(program_loc + "\\config\\")
    allConfigs = []
    for i in files:
        singleConfig = [str(x) for x in i.split(".")]
        if singleConfig[1] == "txt":
            allConfigs.append(singleConfig[0])
    return allConfigs

def saveConfig(destFile, data):
        with open(program_loc + "\\config\\" + destFile + ".txt", "w") as f:
            f.write(data)
            f.close()


finalDirEditorText = sm.SelectionMenu()
finalDirEditorText.isSingleOption = False

def finalDirEditor(configName, fdData):
    cmd1 = "edit"
    cmd2 = "save"

    finalDirEditorText.titleText = f"Editing final directory in {configName} config"
    finalDirEditorText.options = f"To change final directory type: {cmd1} (final dir addres)\nTo save and exit type {cmd2}"

    editing = True
    while editing:
        finalDirEditorText.desc = f"Current final directory is: {fdData}"
        choice = finalDirEditorText.mainLoop()
        if choice[0] == cmd1:
            fdData = choice[1]
        elif choice[0] == cmd2:
            return fdData

fileTypeEditorText = sm.SelectionMenu()
fileTypeEditorText.isSingleOption = False
fileTypeEditorText.useList = True

def fileTypeEditor(configName, ftData):
    cmd1 = "add"
    cmd2 = "remove"
    cmd3 = "save"

    currentFileTypes = []
    try:
        currentFileTypes = [str(x) for x in ftData.split("<>")]
        currentFileTypes.remove("")
    except:
        pass
    fileTypeEditorText.titleText = f"Editing file types (ft) in {configName} config"
    fileTypeEditorText.options = f"{cmd1} (fileType) - to add\n{cmd2} (fileType) - to remove\n{cmd3} - to save and exit"

    editing = True
    while editing:
        fileTypeEditorText.l = currentFileTypes
        choice = fileTypeEditorText.mainLoop()

        try:
            if choice[0] == cmd1:
                currentFileTypes.append(choice[1])
            elif choice[0] == cmd2:
                currentFileTypes.remove(choice[1])
            elif choice[0] == cmd3:
                ftData = ""
                for i in currentFileTypes:
                    ftData += i + "<>"
                return ftData
        except:
            pass
        
searchDirectoryEditorText = sm.SelectionMenu()
searchDirectoryEditorText.isSingleOption = False
searchDirectoryEditorText.useList = True

def searchDirectoryEditor(configName, sdData):
    cmd1 = "add"
    cmd2 = "remove"
    cmd3 = "save"

    currentDirectories = []
    try:
        currentDirectories = [str(x) for x in sdData.split("<>")]
        currentDirectories.remove("")
    except:
        pass
    searchDirectoryEditorText.titleText = f"Editing directories (ft) in {configName} config"
    searchDirectoryEditorText.options = f"{cmd1} (dir addres) - to add\n{cmd2} (dir addres number) - to remove\n{cmd3} - to save and exit"

    editing = True
    while editing:
        searchDirectoryEditorText.l = currentDirectories
        choice = searchDirectoryEditorText.mainLoop()

        try:
            if choice[0] == cmd1:
                currentDirectories.append(choice[1])
            elif choice[0] == cmd2:
                currentDirectories.remove(currentDirectories[int(choice[1])])
            elif choice[0] == cmd3:
                sdData = ""
                for i in currentDirectories:
                    sdData += i + "<>"
                return sdData
        except:
            pass

configEditorText = sm.SelectionMenu()
configEditorText.isSingleOption = False

def configEditor(configName, data):
    cmd1 = "edit"
    opt1_1 = "fd"
    opt2_1 = "ft"
    opt3_1 = "sd"

    cmd2 = "save"
    
    configEditorText.titleText = f"Currently editting {configName} config"
    configEditorText.options = f"Chose an action to perform:\n{cmd1} {opt1_1} - (final directory)/{opt2_1} - (file types to sort)/{opt3_1} - (directories that you want to be sorted)\n{cmd2} - to save and exit)"
    editing = True

    updatedData = [None]*3
    try:
        for i in range(len(data)):
            updatedData[i] = data[i]
    except:
        pass

    while editing:
        choice = configEditorText.mainLoop()

        if choice[0] == cmd1:
            if choice[1] == opt1_1:
                updatedData[0] = finalDirEditor(configName, updatedData[0])
            elif choice[1] == opt2_1:
                updatedData[1] = fileTypeEditor(configName, updatedData[1])
            elif choice[1] == opt3_1:
                updatedData[2] = searchDirectoryEditor(configName, updatedData[2])

        elif choice[0] == cmd2:
            editing = False
            finalData = ""
            for i in updatedData:
                if i == None:
                    finalData += "\n"
                else:
                    finalData += i + "\n"
            saveConfig(configName, finalData)

        else:
            pass

def readConfig(configName):
    try:
        with open(program_loc + "\\config\\" + configName + ".txt", "r") as f:
            data = [str(x) for x in f.read().split("\n")]
            f.close()
            return data
    except OSError:
        iOpt.option_choice(f"Config with {configName} name does not exits (press ENTER to continue)")

def addConfig(configName):
    try:
        with open(program_loc + "\\config\\" + configName + ".txt", "w") as f:
            f.write("None\nNone\nNone\n")
            f.close()
            configEditor(configName, None), configName + ".txt"
    except OSError:
        iOpt.option_choice("Cannot use some special symbols! (press ENTER to continue)")

def editConfig(configName):
    try:
        with open(program_loc + "\\config\\" + configName + ".txt", "r") as f:
            data = [str(x) for x in f.read().split("\n")]
            f.close()
            configEditor(configName, data), configName + ".txt"
    except OSError:
        iOpt.option_choice(f"Config with {configName} name does not exits (press ENTER to continue)")

def removeConfig(configName):
    try:
        os.remove(program_loc + "\\config\\" + configName + ".txt")
    except OSError:
        iOpt.option_choice(f"Config with {configName} name does not exits (press ENTER to continue)")