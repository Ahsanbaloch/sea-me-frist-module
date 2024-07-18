# Documentation
PiRacer Login (Username: pushforce, Password: pushforce)

## Notes & ToDos
- For the evaluation we need "How to assemble and setup PiRacer"
- CONTROLS: Implement controls --> Test controls with test script rc_example.py
- Switch from Python to CPP for controls? (to discuss)
- CAMERA: Settings of RaspberryPi (Interface Options > Camera enable) --> Test camera with test script camera_grab_example.py
- More documentation on Assembly? (maybe we can do our own graphics for assembly/architecture)
- More examples available --> https://github.com/SEA-ME-COSS/DES-PiRacer-Assembly/tree/main/examples
- Can we switch here from Python to CPP or is it easier to use Python for now? (to discuss)
- PiRacer Libraries (vehicles, gamepad, camera) --> I think we need to understand that better for the future
- OpenCV Library (cv2) --> I think we need to understand that better for the future
- DockeyCar for autonomous driving when someone is bored :) --> https://github.com/autorope/donkeycar

## Assembly Manual
Parts: Motor, Wheels, Servo, Servo Pull Bar, PiRacer Expansion Board, Camera

Connections:
- Motors and Servo --> Extension Board
- Extension Board --> Raspberry Pi
- Camera --> Raspberry Pi

<img src="https://github.com/user-attachments/assets/490b7d3b-79d7-492b-992d-83b935f73ce0" width="800"> </img>

This is from tutorial, maybe we can do it nicer!

### Pins on RaspberryPi (Connect WaveShare Extension with RaspberryPi)
<img src="https://github.com/user-attachments/assets/d3c51b6d-1626-4ef8-b6f1-5a068d44ca26" width="800"> </img>

## Setup PiRacer

### Install and run RaspberryPi Imager (64-bit, full)
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

### Controls
Notes: What did we install? Which configurations an settings did we change?

## Validation
- Run some examples and make a video :)

## Resources
- Assembly Manual (https://www.waveshare.com/wiki/PiRacer_Assembly_Manual)
- PiRacer Py (https://github.com/twyleg/piracer_py)
- PiRacer C++ (https://github.com/Lagavulin9/piracer-cpp)
- Assembly Manual COSS (https://github.com/SEA-ME-COSS/DES-PiRacer-Assembly)
- RaspberryPi PINs (https://www.heise.de/ratgeber/Raspberry-GPIO-Pins-beim-Booten-initialisieren-4782030.html)
