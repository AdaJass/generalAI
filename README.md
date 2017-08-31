# generalAI #

##Concept Learning Step: ##
###real concept:###
1. main.py invokes input_sensor.py
>set time interval to receive picture, voice, touch, (smell?)
2. main.py invokes conceptNet with the first step's result
>process.py A nueral network like algorithm will work with this raw data, and get an ouput, output is a group of attribute, or null
>if output is not null, approximately look up output at concept database, if no, build new concept.
>if the outout is null, will take a more look at the scene.

###virtual concept:###
