# E30_Upgraded_OBC
Run the usual updates/upgrades
```
sudo apt-get update
sudo apt update
sudo apt upgrade
```
Install PIP
```
sudo apt install python3-pip
```
Install keyboard for various debugging
```
sudo apt install matchbox-keyboard
```
Install screen driver (and rotates it 90*)
```
sudo rm -rf LCD-show
git clone https://github.com/goodtft/LCD-show.git
chmod -R 755 LCD-show
cd LCD-show/
sudo ./MHS35-show 90
```
Install Guizero for PY Graphics program
```
pip3 install guizero
```

Menu -> Preference -> Appearance Settings

Install Font;_
* https://www.1001fonts.com/digital-7-font.html
* /home/pi in the file explorer
* Create a new folder and name it “.fonts”
* Right click > Create new > Folder, and type “.fonts”
* Paste the files into the “.fonts” folder you just created

Menu -> Preferences -> Localisation -> Set your timezone


Edit screen blank parameter
```
sudo nano /boot/cmdline.txt
```
Add "consoleblank=0" to turn screen blanking off completely

<b>Note</b> the kernel command line must be a single line of text.
