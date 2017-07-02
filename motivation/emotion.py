"""
This file provide model for emothion.
"""
import sqlite3
import changefun

con = sqlite3.connect('../generalAI.db')
para=dict(con.execute("select * from emotion"))
print(para)

class Emotion():
    """
    Emotion base class
    There is two side that make emotion up and down.
    one side is directly sensor input, another side is 
    base on comprehensive of the sensor input, like sound, 
    scene.
    """
    def __init__(self):
        self.select_rate  = para['select_rate']        #the rate this emotion be selected
        self.pleasure_value   = para['pleasure_value'] #how much pleasure get from this emotion
        self.strength = para['current_value']          #the emothon strength
        self.stable       = para['stable']             #is this emotion easy to down the strength
        self.change_fun   = para['change_fun'] 
        pass

    def temperature(self, temperature):
        """
        Recieve temperature from outside, sensor,
        change the pleasure_value and strength.
        the function shoule result below figure:

            * * * * * *
          *             *
         *               *
        *                *
        horizontal axis is temperature, vertical axis
        is strength or pleasure_value
        """
        pleasure=0
        if temperature<=-50:
            #y=-(x+50)^2
            pleasure = -(temperature+50)**2

        if -50<temperature<-40:
            pleasure = 0.1*temperature+5

        if 40<temperature<50:
            pleasure = -0.1*temperature+5

        if -40<=temperature<=40:
            pleasure=1

        if temperature>=50:
            pleasure = -(temperature-50)**2

        return pleasure
        pass


    


