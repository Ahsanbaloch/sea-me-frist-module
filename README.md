# Documentation

Username: pushforce
Password: pushforce

## For the evaluation we need "How to assemble and setup PiRacer"

## Assembly Manual (ToDo: Step-by-step guide)
https://www.waveshare.com/wiki/PiRacer_Assembly_Manual
(We had problems with the steering setup, so maybe some emphasis there.)

## Pins on RaspberryPi (Connect WaveShare Extension with Pi)
https://www.heise.de/ratgeber/Raspberry-GPIO-Pins-beim-Booten-initialisieren-4782030.html
![image](https://github.com/user-attachments/assets/d3c51b6d-1626-4ef8-b6f1-5a068d44ca26)

## OS - Flushed Raspian (64-bit, full)
Install RaspberryPi Imager (sudo snap install rpi-imager)
Run (rpi-imager)

## Controls:
https://github.com/Lagavulin9/piracer-cpp
https://github.com/SEA-ME-COSS/DES-PiRacer-Assembly
Notes: What did we install? Which configurations an settings did we change?

https://github.com/twyleg/piracer_py
### Install dependencies:
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

### Enable i2c and camera
sudo raspi-config
i2c: Interface Options > I2C
Camera: Interface Options > Camera --> did not find it

### Install piracer-py package
cd ~
mkdir piracer_test/
cd piracer_test/
python3 -m venv venv
source venv/bin/activate

pip install piracer-py

Then: Copy example from that tutorial and change PiRacerPro to PiRacerStandard


## DockeyCar for autonomous driving when someone is bored :)


## Resources
Here we can add the resources when text is written.
