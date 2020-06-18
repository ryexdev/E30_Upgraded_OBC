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



```
sudo apt install xscreensaver
```
Menu -> Preferences -> Screensaver

Disable Screen Saver


```
http://arduino.esp8266.com/stable/package_esp8266com_index.json
https://raw.githubusercontent.com/damellis/attiny/ide-1.6.x-boards-manager/package_damellis_attiny_index.json
http://digistump.com/package_digistump_index.json
https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
https://arduino.esp8266.com/stable/package_esp8266com_index.json
```

GPS
```
sudo apt-get install python gpsd gpsd-clients
```
Test using ```cgps```, should output info on command line
