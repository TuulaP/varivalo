#!/usr/bin/python

from phue import Bridge
from time import sleep

from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.
homeip = os.getenv('HOMEIP')


b = Bridge(ip=homeip, config_file_path=".python_hue")


# Get the bridge state (This returns the full dictionary that you can explore)
print(b.get_api())


# Prints if light 1 is on or not
print(b.get_light(1, 'on'))

#b.set_light(1,'on', False)
b.set_light(1,'on', True)


command =  {'transitiontime' : 300, 'on' : True, 'bri' : 254}
b.set_light(1, command)


# do the rainbow
lights = b.get_light_objects()
#lights = lights[0]  # just 1 light;)

if 3>6:

    totalTime = 30 # in seconds
    transitionTime = 1 # in seconds

    maxHue = 65535
    hueIncrement = maxHue / totalTime

    for light in lights:
        light.transitiontime = transitionTime * 10
        light.brightness = 254
        light.saturation = 254
        # light.on = True # uncomment to turn all lights on

    hue = 0
    while True:
        for light in lights:
            light.hue = hue

        hue = (hue + hueIncrement) % maxHue

        sleep(transitionTime)

# ----------------------------------

b.set_light(1,'on', False)



