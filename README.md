# Documentation

## Notes
- Implement controls.
- Switch from Python to CPP for control
- For the evaluation we need "How to assemble and setup PiRacer"
- PiRacer Login (Username: pushforce, Password: pushforce)
- More documentation on Assembly?
- Settings of RaspberryPi (Interface Options > Camera enable) 

## Assembly Manual
Parts: Motor, Wheels, Servo, Servo Pull Bar, PiRacer Expansion Board, Camera
Connections:
- Motors and Servo --> Extension Board
- Extension Board --> Raspberry Pi
- Camera --> Raspberry Pi
![PiRacer](https://github.com/user-attachments/assets/490b7d3b-79d7-492b-992d-83b935f73ce0)
This is from tutorial, maybe we can do it nicer!

## Pins on RaspberryPi (Connect WaveShare Extension with Pi)
https://www.heise.de/ratgeber/Raspberry-GPIO-Pins-beim-Booten-initialisieren-4782030.html
![image](https://github.com/user-attachments/assets/d3c51b6d-1626-4ef8-b6f1-5a068d44ca26)

## Install and run RaspberryPi Imager (64-bit, full)
```bash
sudo snap install rpi-imager
rpi-imager
```

### Install dependencies:
```bash
sudo apt update
sudo apt install \
    gcc \
    v4l-utils \
    i2c-tools \
    raspi-config \
    python3-dev \
    python3-setuptools \
    python3-venv \
    libopencv-dev
```

### Enable i2c and camera
```bash
sudo raspi-config
```
i2c: Interface Options > I2C
Camera: Interface Options > Camera --> DID NOT FIND IT!!!!!!

### Install piracer-py package
```bash
cd ~
mkdir piracer_test/
cd piracer_test/
python3 -m venv venv
source venv/bin/activate
pip install piracer-py
```

Then: Copy example from that tutorial and change PiRacerPro to PiRacerStandard


## Controls:
Notes: What did we install? Which configurations an settings did we change?

## DockeyCar for autonomous driving when someone is bored :)

## Resources
- Assembly Manual (https://www.waveshare.com/wiki/PiRacer_Assembly_Manual)
- https://github.com/twyleg/piracer_py
- https://github.com/Lagavulin9/piracer-cpp
- https://github.com/SEA-ME-COSS/DES-PiRacer-Assembly
