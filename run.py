import os
import os.path

currentenviorment = "unk"

#Check for folder, so we don't mess anything up
print("Checking for default wallpapers")
if(os.path.isdir("/usr/share/wallpapers")):
    currentenviorment = "KDE"
    print("Found default wallpapers, detected enviroment KDE")
else:
    print("Could not find a enviroment ")

