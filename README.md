# E30_Upgraded_OBC
https://www.raspberrypi.org/software/

Use "Rasberry Pi Imager"

Place an empty file called "SSH" into memory drive root (see downloads)

Place a file with the contents below named "wpa_supplicant.conf" into memory drive root (see downloads)
```
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
network={
  ssid="Zeke"
  psk="beer4pass"
}
```

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
```
Change the following values
```
cd MZDPI/vga
sudo nano mzdpi-vga-autoinstall-online
```
Change "swapxy" below to "0"
```
echo "dtoverlay=ads7846,penirq=27,swapxy=0,xmin=200,xmax=3850,ymin=200,ymax=3850" >> /boot/tmp.txt
```
```
echo "display_rotate=4" >> /boot/tmp.txt
```
```
echo "framebuffer_width=480" >> /boot/tmp.txt
```
```
echo "framebuffer_height=640" >> /boot/tmp.txt
```
Reload your changes
```
cd MZDPI/vga
sudo chmod +x mzdpi-vga-autoinstall-online
sudo ./mzdpi-vga-autoinstall-online
sudo reboot
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
sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
```
```
@python3 /home/pi/Desktop/V1-PZ_GP.py
```

Trouble Shooting
```
sudo apt-get purge python3

DISPLAY=:0 python3 Desktop/V1-PZ_GP.py

sudo killall python3
```

