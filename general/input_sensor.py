"""
This file define all the data from input sensor.
"""
import numpy as np

#temperature C
temperature=20

#eyes, every element is an image, so it is a image series, take 5 samples each time.
eyes=[[0],[0],[0],[0],[0]]

#energy, or battery
energy=20

#force, there are many force sensor on robot's body, the help to bahave and judge environment.
ALL_FORCE_SENSOR = 10000
force_unit={'direction':[0,0,-1], 'strength':9}
force=[force_unit for x in range(ALL_FORCE_SENSOR)]
