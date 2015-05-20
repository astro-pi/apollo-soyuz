# Apollo Soyuz Demo

Demonstration of the IMU sensor on the Astro Pi sense HAT by [Serge Schneider](https://github.com/XECDesign).

Assumes the Astro Pi software [installation](https://github.com/astro-pi/astro-pi-hat/blob/master/README.rst) has been done.

## Requirements

- Python [pi3d](https://pypi.python.org/pypi/pi3d) module.

```bash
sudo pip install pi3d
```

## Usage

```bash
git clone https://github.com/astro-pi/apollo-soyuz.git
cd apollo-soyuz
sudo ./soyuz.py
```

Pi 1 users will have to wait 3 to 4 minutes for this to load. For Pi 2 users it's about 30 seconds.
Pick up the Astro Pi and start moving it around when you see the spacecraft appear on screen.

## Keys

- `a` toggle accelerometer on/off
- `g` toggle gyroscope on/off
- `m` toggle magnetometer compass on/off
- `+` increase yaw offset
- `-` decrease yaw offset
- `Esc` quit
