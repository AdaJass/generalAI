"""
This file define all the data from input sensor.
"""
import numpy as np

#temperature C
temperature=20

#eyes, every element is an image, so it is a image series
eyes=[[0],[0],[0],[0],[0]]

#energy
energy=20

#force
ALL_FORCE_SENSOR = 10000
force_unit={'direction':[0,0,-1], 'strength':9}
force=[force_unit for x in range(ALL_FORCE_SENSOR)]
