
# MO2-Extractor

![image](https://github.com/VeryFunnyMonkey/MO2-Extractor/assets/62693226/97735661-6473-443a-bcb7-abe699d7ab07)


 Mod Organizer 2 Extractor, used to extract raw files from modlist.

I created this to be used on the Steam Deck, where Mod Organizer 2 doesn't work too well. I use this program and grab the raw mod files and drop it in the Data folder for the game im modding.

I've only tested this for a handful of mods, I didn't have any issues with the mods I tested but I could see mods that utilise some MO2 features maybe not working.

## Usage
1. Click Source - select a modlist.txt from a MO2 profile.
2. Click Destination - select a folder that the mod files will be extracted to - ⚠️⚠️⚠️ **THIS WILL OVERWRITE ANYTHING IN THE FOLDER** ⚠️⚠️⚠️
3. The files will begin to be copied across, once complete a popup will appear letting you know.

## Downloading the Latest Release

1. Navigate to the [Releases](https://github.com/VeryFunnyMonkey/MO2-Extractor/releases) page of this repository.
2. Look for the latest release. The releases are tagged and include brief notes about what changes were made.
3. Under the release notes and assets, click on the asset that corresponds with your platform and download it.

## Required Libraries:
pysimplegui==4.60.5

## Manual Compilation

### Linux
To compile the program, you will need to have the following installed:
```bash
    sudo apt-get install python3 python3-pip python3-venv
```
Then you can create a virtual environment and install the required libraries:
```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
```
Then you can run the program with:
```bash
    python mo2Extractor.py
```

### Windows
To compile the exe is using psgcompiler with the following flags
```ps1
    --onedir --console --workpath "C:/dev/mo2Extractor/psc_mo2Extractor_tmp" --distpath "C:/dev/mo2Extractor" --specpath "C:/dev/mo2Extractor" "C:/dev/mo2Extractor/mo2Extractor.py"
```
## KNOWN ISSUES:
 - Currently the UI will freeze during copying, it will still copy the files in the background however. When it is complete a message will still appear.

## TODO:
 - Allow for the browsing of mods, allowing the user to tick/untick mods in the modlist.
 - Test some bigger modlists, and see if there's any mods that don't extract well.
 - Rewrite the UI in another GUI, PySimpleGui is a bit annoying.

Feel free to branch, fork, make PRs, I'd love to see what people can come up with for it.
