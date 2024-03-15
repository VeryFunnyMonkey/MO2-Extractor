
# MO2-Extractor
 Mod Organizer 2 Extractor, used to extract raw files from modlist.

I created this to be used on the Steam Deck, where Mod Organizer 2 doesn't work too well. I use this program and grab the raw mod files and drop it in the Data folder for the game im modding.

I've only tested this for a handful of mods, I didn't have any issues with the mods I tested but I could see mods that utilise some MO2 features maybe not working.

## Usage
1. Click Source - select a modlist.txt from a MO2 profile.
2. Click Destination - select a folder that the mod files will be extracted to - !!!THIS WILL OVERWRITE ANYTHING IN THE FOLDER!!!
3. The files will begin to be copied across, once complete a popup will appear letting you know.

## Required Libraries:

    pysimplegui=4.60.5


The precompiled exe is using psgcompiler with the following flags

    --onedir --console --workpath "C:/dev/mo2Extractor/psc_mo2Extractor_tmp" --distpath "C:/dev/mo2Extractor" --specpath "C:/dev/mo2Extractor" "C:/dev/mo2Extractor/mo2Extractor.py"

## TODO:
 - Allow for the browing of mods, allowing the user to tick/untick mods in the modlist.
 - Test some bigger modlists, and see if there's any mods that don't extract well.
 - Rewrite the UI in another GUI, PySimpleGui is a bit annoying.

Feel free to branch, fork, make PRs, I'd love to see what people can come up with for it.
