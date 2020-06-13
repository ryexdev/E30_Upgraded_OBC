# E30_Upgraded_OBC
Run the usual updates/upgrades
```
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
