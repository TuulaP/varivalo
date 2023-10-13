#!/usr/bin/python

from phue import Bridge
from time import sleep

from dotenv import load_dotenv
import os
import requests
from requests.auth import HTTPBasicAuth
import atexit

chosenLight = 1   # Or to config file?


def exit_handler():
    # print("Thx and bye")
    # shut light off
    b.set_light(chosenLight, 'on', False)


atexit.register(exit_handler)

load_dotenv()  # take environment variables from .env.

homeip = os.getenv('HOMEIP')

b = Bridge(ip=homeip, config_file_path=".python_hue")


# Get the bridge state (This returns the full dictionary that you can explore)
# print(b.get_api())


# Prints if light  is on or not
# print(b.get_light(chosenLight, 'on'))

# command =  {'transitiontime' : 300, 'on' : True, 'bri' : 254}
# b.set_light(chosenLight, command)


# do the rainbow
lights = b.get_light_objects()
# lights = lights[0]  # just 1 light;)

# ----------------------------------

# Check if the specific service is up -> if not show some red color.

api_url = os.getenv('SERVICEMONITOR')

# if auth needed
# usr = os.getenv('USRN')
# sal = os.getenv('SAL')
# auth = HTTPBasicAuth(usr, sal)

# response = requests.get(api_url, auth=auth)
response = requests.get(api_url)


if response.status_code == 200:
    print("All ok")
# print(response.json())

# Blue: {"hue":46920}
# Neongreen 26920
# pink 56920
# purpleish 50920
# lightviolet 49555
# turquoise 42555
# spruce  29555

if (response.json() is True):

    if 3 > 5:  # maybe not.
        # do the rainbow
        totalTime = 20  # in seconds
        transitionTime = 1  # in seconds

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
else:
    if (b.get_light(chosenLight, 'on') is False):
        # b.set_light(1,'on', False)
        b.set_light(chosenLight, 'on', True)

    b.set_light(chosenLight, 'hue', 50920)
    sleep(5)
    b.set_light(chosenLight, 'hue', 56920)
    sleep(5)
    b.set_light(chosenLight, 'hue', 49555)
    sleep(5)
    b.set_light(chosenLight, 'hue', 50920)
