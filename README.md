# Apollo Soyuz Demo

Demonstration of the IMU sensor on the Sense HAT by [Serge Schneider](https://github.com/XECDesign).

Assumes the [Sense HAT Python library](https://github.com/RPi-Distro/python-sense-hat) has been installed.

## Requirements

- Python [pi3d](https://pypi.python.org/pypi/pi3d) module

Python 3:

```bash
sudo apt-get install python3-pip
sudo pip-3.2 install pi3d
```

Python 2:

```bash
sudo apt-get install python-pip
sudo pip install pi3d
```

## Usage

```bash
git clone git://github.com/astro-pi/apollo-soyuz
cd apollo-soyuz
sudo python3 soyuz.py
```

Pi 1 users will have to wait 3 to 4 minutes for this to load. For Pi 2 users it's about 30 seconds.

Pick up the Astro Pi and start moving it around when you see the spacecraft appear on screen.

This is a good demonstration of pitch, roll and yaw.

## Keys

- `a` toggle accelerometer on/off
- `g` toggle gyroscope on/off
- `m` toggle magnetometer compass on/off
- `+` increase yaw offset
- `-` decrease yaw offset
- `Esc` quit
