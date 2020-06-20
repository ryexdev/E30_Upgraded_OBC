# E30_Upgraded_OBC
Run the usual updates/upgrades. Upgrade will take some time (45+ minutes on a Pi Zero)
```
sudo apt-get update
sudo apt update
sudo apt upgrade
sudo apt-get update
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
NO IDEA WHICH ONE WORKS
https://raspberrypiwiki.com/index.php?title=2.8_inch_Touch_Screen_for_Pi_zero&mobileaction=toggle_view_mobile
```
cd ~/
sudo git clone https://github.com/tianyoujian/MZDPI.git
cd MZDPI/vga
sudo chmod +x mzdpi-vga-autoinstall-online
sudo ./mzdpi-vga-autoinstall-online

sudo chmod +x mzp280v01br-autoinstall-online
sudo ./mzp280v01br-autoinstall-online


sudo chmod +x mzdpi-vga-autoinstall-offline 
sudo ./mzdpi-vga-autoinstall-offline 
```
cd ~/
git clone https://github.com/tianyoujian/MZDPI.git
cd MZDPI/vga
sudo chmod +x mzdpi-vga-autoinstall-online
sudo ./mzdpi-vga-autoinstall-online
sudo reboot
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



```
sudo apt install xscreensaver
```
Menu -> Preferences -> Screensaver

Disable Screen Saver


GPS
```
sudo apt-get install python gpsd gpsd-clients
pip3 install gps
```
Test using ```cgps```, should output info on command line

Disable Cursor
```
sudo apt install unclutter
```
Reboot
```
unclutter -idle 0
```
