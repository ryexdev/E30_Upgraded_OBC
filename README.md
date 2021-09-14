# E30_Upgraded_OBC

## Intro
Welcome to my project! Thanks for checking it out. I will be updating this code on a routine basis, please fork if you'd like to develop and not receive breaking changes. If you have any questions shoot me an email at 
RyanHendersonContact@gmail.com

https://www.linkedin.com/pulse/weekend-projects-digital-dash-ryan-henderson/

https://hackaday.com/2021/03/11/raspberry-pi-hitches-a-ride-in-a-1989-bmw-dashboard/

If you find this project useful, please feel free to buy me a cup of coffee!

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate?hosted_button_id=HEU4DWYXZJ77E)

## Code
https://www.raspberrypi.org/software/

Use "Rasberry Pi Imager", install OS Lite

Place an empty file called "SSH" into memory drive root

Place a file with the contents below named "wpa_supplicant.conf" into memory drive root
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

Run the usual updates/upgrades
```
sudo apt-get update && sudo apt-get upgrade -y
sudo apt install git -y
sudo apt install python3-pip -y
sudo apt-get install python3-tk -y
sudo apt-get install python gpsd gpsd-clients -y
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install --no-install-recommends raspberrypi-ui-mods lxsession -y
sudo apt-get install --no-install-recommends xserver-xorg x11-xserver-utils xinit openbox -y
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


```
sudo apt install xscreensaver
```
Menu -> Preferences -> Screensaver

Disable Screen Saver


GPS
```
sudo pip3 install gps
```
Test using ```cgps```, should output info on command line


Disable Cursor
```
sudo apt install unclutter
```
Edit the following file
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
Place the following line into the file above
```
@python3 /home/pi/Desktop/E30_Upgraded_OBC/V1-PZ_GP.py
```

Download Program
```
cd Desktop
sudo git clone https://github.com/ryanredbaron/E30_Upgraded_OBC
sudo reboot
```

Trouble Shooting
```
cd Desktop/E30_Upgraded_OBC;sudo git pull --all;sudo reboot

DISPLAY=:0 python3 Desktop/E30_Upgraded_OBC/V1-PZ_GP.py

DISPLAY=:0 python3 V1-PZ_GP.py

sudo killall python3
```
