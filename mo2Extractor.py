import os
import shutil

import PySimpleGUI as sg


def read_mod_list(mod_list_file):
    with open(mod_list_file, "r", encoding="utf-8") as file:
        mod_list = [line.lstrip("+").rstrip() for line in file if line.startswith("+")]
    mod_list.reverse()
    return mod_list


def copy_mod_list(mod_list_file, mod_list, destination, output_elem):
    modsFolder = mod_list_file.split("/profiles")[0] + "/mods"

    modFiles = os.listdir(modsFolder)

    if os.path.exists(destination):
        shutil.rmtree(destination)

    output = ""
    for mod in mod_list:
        if mod in modFiles:
            output += "Copying mod: " + mod + "\n"
            shutil.copytree((modsFolder + "/" + mod), destination, dirs_exist_ok=True)
            output_elem.update(value=output)


def main():
    layout = [
        [
            sg.Text("Source"),
            sg.InputText(key="source"),
            sg.FileBrowse(file_types=(("Modlist Files", "modlist.txt"),)),
        ],
        [sg.Text("Destination"), sg.InputText(key="destination"), sg.FolderBrowse()],
        [sg.Button("Go")],
        [sg.Text("Output", size=(10, 1))],
        [sg.Output(size=(60, 10), key="-OUTPUT-", font="Courier 10")],
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
                modList = read_mod_list(source)
                copy_mod_list(source, modList, destination, window["-OUTPUT-"])
                sg.popup("Mod list copied successfully!")

    window.close()


if __name__ == "__main__":
    main()
