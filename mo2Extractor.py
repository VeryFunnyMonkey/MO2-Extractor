import os
import shutil
import PySimpleGUI as sg

def readModList(modlistFile):
    with open(modlistFile, 'r') as file:
        modList = [line.lstrip('+').rstrip() for line in file if line.startswith('+')]
    modList.reverse()
    return modList

def copyModList(modlistFile, modList, destination, output_elem):
    modsFolder = (modlistFile.split("/profiles")[0] + "/mods")

    modFiles = os.listdir(modsFolder)

    if os.path.exists(destination):
        shutil.rmtree(destination)

    output = ""
    for mod in modList:
        if mod in modFiles:
            output += "Copying mod: " + mod + "\n"
            shutil.copytree((modsFolder + "/" + mod), destination, dirs_exist_ok=True)
            output_elem.update(value=output)

def main():
    layout = [
        [sg.Text("Source"), sg.InputText(key="source"), sg.FileBrowse(file_types=(("Modlist Files", "modlist.txt"),))],
        [sg.Text("Destination"), sg.InputText(key="destination"), sg.FolderBrowse()],
        [sg.Button("Go")],
        [sg.Text("Output", size=(10, 1))],
        [sg.Output(size=(60, 10), key='-OUTPUT-', font='Courier 10')]
    ]

    window = sg.Window("Mod Copy Tool", layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == "Go":
            source = values["source"]
            destination = values["destination"]
            if source and destination:
                modList = readModList(source)
                copyModList(source, modList, destination, window['-OUTPUT-'])
                sg.popup("Mod list copied successfully!")

    window.close()

if __name__ == "__main__":
    main()
