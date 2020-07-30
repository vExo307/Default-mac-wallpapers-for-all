import os
import os.path
import sys
from shutil import copyfile

currentenviorment = "unk"

envdirectory = {
    "KDE":"/usr/share/wallpapers"
}

defaultwallpaperskde = ['SafeLanding', 'ColorfulCups', 'Volna', 'Cascade', 'Opal', 'Path', 'Elarun', 'FallenLeaf', 'Next', 'BytheWater', 'FlyingKonqui', 'Canopee', 'Cluster', 'Autumn', 'OneStandsOut', 'Kokkini', 'summer_1am', 'PastelHills', 'EveningGlow', 'Kite', 'ColdRipple', 'Grey', 'DarkestHour', 'IceCold']
macwallpaperskde = ['CatalinaSilhouette', 'HighSierra', 'CatalinaCoast', 'MojaveNight', 'YosemiteHalfDome', 'CatalinaShoreline', 'DesertDunes', 'BigSurDark', 'CatalinaDay', 'CatalinaSunset', 'YosemiteTrees', 'DesertRock', 'HalfDomeNightSky', 'DesertNightSky', 'BigSurDay', 'MojaveDay', 'Yosemite', 'BigSurNight', 'CatalinaClouds', 'DesertReflection', 'Sierra', 'DesertRockFormation', 'SierraPeaks', 'CatalinaRock', 'CatalinaEvening', 'CatalinaNight', 'DesertFlats', 'ElCapitan', 'DesertMoonlight', 'BigSurLight']
uput = "0"

def cli():
    print("\nPlease choose an option:")
    print("[1] Install wallpapers, and remove default wallpapers\n[2] Install wallpapers alongside default wallpapers\n[3] Restore defaults\n[4] Exit")
    uinput = input("Option: ")

    if(str(uinput).isdigit() == False):
        sys.exit("Invalid Input ")

    if(int(uinput) > 4 or int(uinput) < 1):
        sys.exit("Invalid Input ")
    return uinput

#Check for folder, so we don't mess anything up
os.system("clear")
print("Mac Wallpapers For All")
print("v1.0 | github.com/vExo307/mac-wallpapers-for-all\n")
print("Checking for default wallpapers")
if(os.path.isdir("/usr/share/wallpapers")):
    currentenviorment = "KDE"
    print("Found default wallpapers, detected enviroment KDE")
    uput = cli()
else:
    sys.exit("Could not find a enviroment ")

if(os.path.isdir("/usr/share/wallpapersbackup")):
    print("Backup Found, Continuing")
else:
    print("Creating backup")
    os.system("sudo mkdir /usr/share/wallpapersbackup")
    os.system("sudo cp -R " + envdirectory[currentenviorment] + " /usr/share/wallpapersbackup")

if(uput == "1"):
    print("Removing default wallpapers")
    for wallpaper in defaultwallpaperskde:
        os.system("sudo rm -R " + envdirectory[currentenviorment] + "/" + wallpaper)
        print("Removed Wallpaper " + wallpaper)
    print("Installing Mac wallpapers")
    for wallpaper in macwallpaperskde:
        os.system("sudo cp -R " + os.path.dirname(os.path.realpath(__file__)) + "/KDE/" + wallpaper + " " + envdirectory[currentenviorment])
        print("Added Wallpaper " + wallpaper)
elif(uput == "2"):
    print("Installing Mac wallpapers")
    for wallpaper in macwallpaperskde:
        os.system("sudo cp -R " + os.path.dirname(os.path.realpath(__file__)) + "/KDE/" + wallpaper + " " + envdirectory[currentenviorment])
        print("Added Wallpaper " + wallpaper)
elif(uput == "3"):
    for wall in os.listdir(envdirectory[currentenviorment]):
        if(wall in defaultwallpaperskde):
            print(wall + " is a default, ignoring")
        else:
            os.system("sudo rm -R " + envdirectory[currentenviorment] + "/" + wall)
            print(wall + " is not a default, removing")
    for wallpaper in defaultwallpaperskde:
        os.system("sudo cp -R /usr/share/wallpapersbackup/wallpapers/" + wallpaper + " " + envdirectory[currentenviorment])
        print("Added Wallpaper " + wallpaper + " From Backup") 
elif(uput == "4"):
    sys.exit("Exiting")