#!/usr/bin/python3
from sense_hat import SenseHat
import math
import pi3d

sense = SenseHat()

display = pi3d.Display.create()
cam = pi3d.Camera.instance()

shader = pi3d.Shader("mat_light")

model = pi3d.Model(
    file_string="apollo-soyuz.obj",
    name="model", x=0, y=-1, z=40, sx=1, sy=1, sz=1)

model.set_shader(shader)

cam.position((0, 20, 0))
cam.point_at((0, -1, 40))
keyb = pi3d.Keyboard()

compass = gyro = accel = True
sense.set_imu_config(compass, gyro, accel)

yaw_offset = 72

while display.loop_running():
    o = sense.get_orientation_radians()
    if o is None:
        pass

    pitch = o["pitch"]
    roll = o["roll"]
    yaw = o["yaw"]

    yaw_total = yaw + math.radians(yaw_offset)

    sin_y = math.sin(yaw_total)
    cos_y = math.cos(yaw_total)

    sin_p = math.sin(pitch)
    cos_p = math.cos(pitch)

    sin_r = math.sin(roll)
    cos_r = math.cos(roll)

    abs_roll = math.degrees(math.asin(sin_p * cos_y + cos_p * sin_r * sin_y))
    abs_pitch = math.degrees(math.asin(sin_p * sin_y - cos_p * sin_r * cos_y))

    model.rotateToZ(abs_roll)
    model.rotateToX(abs_pitch)
    model.rotateToY(math.degrees(yaw_total))
    model.draw()

    keypress = keyb.read()

    if keypress == 27:
        keyb.close()
        display.destroy()
        break
    elif keypress == ord('m'):
        compass = not compass
        sense.set_imu_config(compass, gyro, accel)
    elif keypress == ord('g'):
        gyro = not gyro
        sense.set_imu_config(compass, gyro, accel)
    elif keypress == ord('a'):
        accel = not accel
        sense.set_imu_config(compass, gyro, accel)
    elif keypress == ord('='):
        yaw_offset += 1
    elif keypress == ord('-'):
        yaw_offset -= 1
