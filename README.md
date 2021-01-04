# E30_Upgraded_OBC
https://desertbot.io/blog/headless-pi-zero-w-wifi-setup-windows

Run the usual updates/upgrades. Upgrade will take some time (45+ minutes on a Pi Zero)
```
sudo apt update -y
sudo apt full-upgrade -y
sudo apt update -y
```
Install screen driver (and rotates it 90*)
```
cd ~/
git clone https://github.com/tianyoujian/MZDPI.git
cd MZDPI/vga
sudo chmod +x mzdpi-vga-autoinstall-online
sudo ./mzdpi-vga-autoinstall-online
sudo reboot
```
Change display_rotate to "4"
echo "display_rotate=4" >> /boot/tmp.txt
```
cd MZDPI/vga
sudo nano mzdpi-vga-autoinstall-online
```
Edit file
```
sudo nano /etc/X11/xorg.conf.d/99-calibration.conf
```
Replace entire contents with this
```
Section "InputClass"
        Identifier      "calibration"
        MatchProduct    "ADS7846 Touchscreen"
        Option  "Calibration"   "195 3895 240 3813"
        Option  "SwapAxes"      "0"
        Option "InvertX"        "False"
        Option "InvertY"        "True"
EndSection
```
Install Guizero for PY Graphics program
```
sudo pip3 install guizero
```

Install Font;_
* https://www.1001fonts.com/digital-7-font.html
* /home/pi in the file explorer
* Create a new folder and name it “.fonts”
* Paste the font files into the “.fonts” folder you just created

Menu -> Preferences (or RPI Setup) -> Localisation -> Set your timezone

```
sudo apt install xscreensaver
```
Menu -> Preferences -> Screensaver

Disable Screen Saver

GPS
```
sudo apt-get install python gpsd gpsd-clients
```
```
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

Release IP
```
Open a terminal and su - to root.
Type ifconfig to show the current IP address that you received from DHCP.
Type dhcpcd -k to send the appropriate signals to dhcpcd.
Now bring the interface back up by typing ifup eth0.
Type ifconfig to show the new IP address.
```
