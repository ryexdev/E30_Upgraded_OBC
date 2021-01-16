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
  ssid="SSID"
  psk="PASSWORD"
}
```

Setup Local Timezone
```
sudo raspi-config
```

Run the usual updates/upgrades. Upgrade will take some time (45+ minutes on a Pi Zero)
```
sudo apt update -y
sudo apt full-upgrade -y
sudo apt update -y
```

Install keyboard for various debugging
```
sudo apt install matchbox-keyboard
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
Change values below
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
Reboot
```
sudo reboot
```

Install Guizero for PY Graphics program
```
sudo pip3 install guizero --force
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
```
sudo nano /etc/default/unclutter
```
Change the last line to below
```
EXTRA_OPTS="-idle 0 -display :0 -root"
```


Auto Run program
```
sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
```
```
@python3 /home/pi/Desktop/E30_Upgraded_OBC/V1-PZ_GP.py
```

Download Program
```
cd Desktop
sudo git clone https://github.com/ryanredbaron/E30_Upgraded_OBC
sudo reboot

TEST 1 - 639e52b8c47279940c7616a4aa5ba3121eedacde
TEST 2 - 713abce4b12fc26da456c3bf168c7f42d846df5f
TEST 3 - 

sudo git config credential.helper store

cd Desktop/E30_Upgraded_OBC;sudo git pull --all;sudo reboot

git reset --hard
```

Update Program
```
cd Desktop/E30_Upgraded_OBC
sudo git pull
```
HARD Reset - Deletes all local
```
sudo git reset --hard
sudo git pull --all
```
GIT Control
```
git add V1-PZ_GP.py
sudo git commit -m "Note"
sudo git push
```
Trouble Shooting
```
sudo chmod -R 777 /home/pi/Desktop/E30_Upgraded_OBC

sudo apt-get purge python3

DISPLAY=:0 python3 Desktop/E30_Upgraded_OBC/V1-PZ_GP.py
DISPLAY=:0 python3 V1-PZ_GP.py

sudo killall python3

cd
cd Desktop
git clone https://github.com/ryanredbaron/E30_Upgraded_OBC
cd E30_Upgraded_OBC
git remote update -usern
```

