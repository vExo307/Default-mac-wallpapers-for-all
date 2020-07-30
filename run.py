import os
import os.path
import sys

currentenviorment = "unk"

def cli():
    print("\nPlease choose an option:")
    print("[1] Install wallpapers, and remove default wallpapers\n[2] Install wallpapers alongside default wallpapers\n[3] Custom install\n[4] Restore defaults\n[5] Exit")
    uinput = input("Option: ")

    if(str(uinput).isdigit() == False):
        sys.exit("Invalid Input ")

    if(int(uinput) > 5 or int(uinput) < 1):
        sys.exit("Invalid Input ")


#Check for folder, so we don't mess anything up
os.system("clear")
print("Mac Wallpapers For All")
print("v1.0 | github.com/vExo307/Default-mac-wallpapers-for-all\n")
print("Checking for default wallpapers")
if(os.path.isdir("/usr/share/wallpapers")):
    currentenviorment = "KDE"
    print("Found default wallpapers, detected enviroment KDE")
    cli()
else:
    sys.exit("Could not find a enviroment ")

