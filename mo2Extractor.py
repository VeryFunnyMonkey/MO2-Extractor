import os
import shutil
import threading

import PySimpleGUI as sg


def read_mod_list(mod_list_file):
    with open(mod_list_file, "r", encoding="utf-8") as file:
        mod_list = [line.lstrip("+").rstrip() for line in file if line.startswith("+")]
    mod_list.reverse()
    return mod_list


def set_mod_folder(mod_list_file, ):
    mods_folder = mod_list_file.split("/profiles")[0] + "/mods"

    if not os.path.exists(mods_folder):
        mods_folder = sg.popup_get_folder("Mods folder not found! Please specify the mods folder.")
        if not mods_folder:
            return mods_folder

    print("Mods Folder: \n" + mods_folder)
    return mods_folder


def copy_mod_list(mods_folder, mod_list, destination, enabled_mods_elem):
    mod_files = os.listdir(mods_folder)

    if os.path.exists(destination):
        shutil.rmtree(destination)

    enabled_mods = enabled_mods_elem.get_list_values()
    for mod in mod_list:
        if mod in mod_files and mod in enabled_mods:
            print("Copying mod: " + mod + "\n")
            shutil.copytree((mods_folder + "/" + mod), destination, dirs_exist_ok=True)
    print("Mod list copied successfully!\n")


def copy_mods_thread(mod_list_file, mod_list, destination, enabled_mods_elem):
    t = threading.Thread(target=copy_mod_list, args=(mod_list_file, mod_list, destination, enabled_mods_elem))
    t.daemon = True  # Set the thread as daemon - kills the thread on window close
    t.start()


def update_mods_list(mod_list, enabled_mods_elem, disabled_mods_elem):
    enabled_mods_elem.update(values=mod_list)
    disabled_mods_elem.update(values=[])


def main():
    sg.theme("LightGrey1")

    tab1_layout = [
        [
            sg.Text("Source"),
            sg.InputText(key="-SOURCE-", enable_events=True, readonly=True),
            sg.FileBrowse(file_types=(("Modlist Files", "modlist.txt"),)),
        ],
        [sg.Text("Destination"), sg.InputText(key="-DESTINATION-", enable_events=True, readonly=True), sg.FolderBrowse()],
        [sg.Button("Go", size=(8, 1), bind_return_key=True)],
        [sg.Text("Output", size=(10, 1))],
        [sg.Output(size=(60, 20), key="-OUTPUT-", font="Courier 10")],
    ]

    tab2_layout = [
        [sg.Text("Enabled Mods:")],
        [
            sg.Listbox(values=[], size=(60, 10), key="-ENABLEDMODS-", enable_events=True, select_mode="LISTBOX_SELECT_MODE_SINGLE")
        ],
        [sg.Text("Disabled Mods:")],
        [
            sg.Listbox(values=[], size=(60, 10), key="-DISABLEDMODS-", enable_events=True, select_mode="LISTBOX_SELECT_MODE_SINGLE")
        ]
    ]

    layout = [[sg.TabGroup([[sg.Tab("Copy Mods", tab1_layout), sg.Tab("Mod List", tab2_layout)]])]]

    window = sg.Window("Mod Copy Tool", layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == "-SOURCE-":
            source = values["-SOURCE-"]
            if values["-SOURCE-"]:
                mod_list = read_mod_list(source)
                enabled_mods = mod_list
                disabled_mods = []
                mods_folder = set_mod_folder(source)
                if not mods_folder:
                    window["-SOURCE-"].update("")
                else:
                    update_mods_list(mod_list, window["-ENABLEDMODS-"], window["-DISABLEDMODS-"])
        if event == "-DESTINATION-":
            destination = values["-DESTINATION-"]
        if event == "-ENABLEDMODS-" and values["-ENABLEDMODS-"]:
            selected_mod = values["-ENABLEDMODS-"][0]
            enabled_mods.remove(selected_mod)
            disabled_mods.append(selected_mod)
            window["-ENABLEDMODS-"].update(values=enabled_mods)
            window["-DISABLEDMODS-"].update(values=disabled_mods)
        if event == "-DISABLEDMODS-" and values["-DISABLEDMODS-"]:
            selected_mod = values["-DISABLEDMODS-"][0]
            disabled_mods.remove(selected_mod)
            enabled_mods.append(selected_mod)
            window["-DISABLEDMODS-"].update(values=disabled_mods)
            window["-ENABLEDMODS-"].update(values=enabled_mods)

        if event == "Go":
            if values["-SOURCE-"] and values["-DESTINATION-"]:
                copy_mods_thread(mods_folder, mod_list, destination, window["-ENABLEDMODS-"])

    window.close()


if __name__ == "__main__":
    main()
