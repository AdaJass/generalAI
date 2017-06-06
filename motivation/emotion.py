"""
This file provide model for emothion.
"""
import sqlite3
con = sqlite3.connect('../generalAI.db')
para=dict(con.execute("select * from emotion"))
print(para.a)

class Emotion():
    """Emotion base class"""
    def __init__(self):
        self.select_rate  = para['select_rate']
        self.init_value   = para['init_value']
        self.curent_vuale = para['current_value']
        self.stable       = para['stable']
        self.change_fun   = para['change_fun']
        
        pass


