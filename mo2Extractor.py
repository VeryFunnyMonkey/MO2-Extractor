import os
import shutil
import threading

import PySimpleGUI as sg


def read_mod_list(mod_list_file):
    with open(mod_list_file, "r", encoding="utf-8") as file:
        mod_list = [line.lstrip("+").rstrip() for line in file if line.startswith("+")]
    mod_list.reverse()
    return mod_list

def set_mod_folder(mod_list_file, output_elem):
    mods_folder = mod_list_file.split("/profiles")[0] + "/mods"

    if not os.path.exists(mods_folder):
        mods_folder = sg.popup_get_folder("Mods folder not found! Please specify the mods folder.")
        
    output_elem.update(value ="Mods Folder: \n" +  mods_folder)
    return mods_folder

def copy_mod_list(mods_folder, mod_list, destination, output_elem):
    mod_files = os.listdir(mods_folder)

    if os.path.exists(destination):
        shutil.rmtree(destination)

    output = ""
    for mod in mod_list:
        if mod in mod_files:
            output += "Copying mod: " + mod + "\n"
            shutil.copytree((mods_folder + "/" + mod), destination, dirs_exist_ok=True)
            output_elem.update(value=output)
    sg.popup("Mod list copied successfully!")


def copy_mods_thread(mod_list_file, mod_list, destination, output_elem):
    t = threading.Thread(target=copy_mod_list, args=(mod_list_file, mod_list, destination, output_elem))
    t.daemon = True  # Set the thread as daemon - kills the thread on window close
    t.start()


def main():
    layout = [
        [
            sg.Text("Source"),
            sg.InputText(key="source", enable_events=True),
            sg.FileBrowse(file_types=(("Modlist Files", "modlist.txt"),)),
        ],
        [sg.Text("Destination"), sg.InputText(key="destination", enable_events=True), sg.FolderBrowse()],
        [sg.Button("Go")],
        [sg.Text("Output", size=(10, 1))],
        [sg.Output(size=(60, 10), key="-OUTPUT-", font="Courier 10")],
    ]

    window = sg.Window("Mod Copy Tool", layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event=="source":
            source = values["source"]
            modList = read_mod_list(source)
            mods_folder = set_mod_folder(source, window["-OUTPUT-"])
        if event=="destination":
            destination = values["destination"]
        if event == "Go":
            if source and destination:
                copy_mods_thread(mods_folder, modList, destination, window["-OUTPUT-"])

    window.close()


if __name__ == "__main__":
    main()
