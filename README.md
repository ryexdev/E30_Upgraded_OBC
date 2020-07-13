# E30_Upgraded_OBC
https://desertbot.io/blog/headless-pi-zero-w-wifi-setup-windows

Run the usual updates/upgrades. Upgrade will take some time (45+ minutes on a Pi Zero)
```
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt update
sudo apt upgrade
sudo apt-get update -y
sudo apt-get upgrade -y
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
https://raspberrypiwiki.com/index.php?title=2.8_inch_Touch_Screen_for_Pi_zero&mobileaction=toggle_view_mobile
```
cd ~/
sudo git clone https://github.com/tianyoujian/MZDPI.git
cd MZDPI/vga
sudo nano mzp280v01br-autoinstall-online
```
Change display_rotate as needed. 2 or 4 works for vertical.
We are using "4".
```
sudo chmod +x mzp280v01br-autoinstall-online
sudo ./mzp280v01br-autoinstall-online
reboot
sudo nano /etc/X11/xorg.conf.d/99-calibration.conf
```
Change these options
```
Section "InputClass"
        Identifier      "calibration"
        MatchProduct    "ADS7846 Touchscreen"
        Option  "Calibration"   "195 3895 240 3813"
        Option  "SwapAxes"      "1"
        Option "InvertX"        "False"
        Option "InvertY"        "True"
EndSection
```
Run on startup to change blueing issue
```
sudo nano /etc/rc.local

sudo raspi-gpio set 8 a2
sudo raspi-gpio set 7 a2
```

Install Guizero for PY Graphics program
```
sudo pip3 install guizero
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
sudo pip3 install gps
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

Auto Run program
```
sudo nano /home/pi/.config/lxsession/LXDE-pi/autostart
@python3 /home/pi/Desktop/V1-PZ_GP.py
```

```
DISPLAY=:0 python3 V1-PZ_GP.py
sudo killall python3

sudo nano ./.config/lxsession/LXDE-pi/autostart
@python3 /home/pi/Desktop/V1-PZ_GP.py
```

Trouble Shooting
```
udo apt-get purge python3
sudo apt update
sudo apt-get install python3
```
