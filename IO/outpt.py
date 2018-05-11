"""require module PyUserInput from https://github.com/PyUserInput/PyUserInput
 
 this module provide output api help to control character.
"""


from pymouse import PyMouse
from pykeyboard import PyKeyboard

__MS = PyMouse()
__KB = PyKeyboard()
__Current_Pressed_Keys = []
def moveForward():
    __KB.press_key('w')    
    __Current_Pressed_Keys.append('w')
    pass

def moveLeft():
    __KB.press_key('a')    
    __Current_Pressed_Keys.append('a')
    pass

def moveRight():
    __KB.press_key('d')    
    __Current_Pressed_Keys.append('d')
    pass

def moveBack():
    __KB.press_key('s')    
    __Current_Pressed_Keys.append('s')
    pass

def somersaultForward():
    __KB.press_keys([__KB.shift_key,'w'])   
    __KB.release_key('w')
    __KB.release_key(__KB.shift_key) 
    pass
def somersaultLeft():
    __KB.press_keys([__KB.shift_key,'a'])   
    __KB.release_key('a')
    __KB.release_key(__KB.shift_key) 
    pass
def somersaultRight():
    __KB.press_keys([__KB.shift_key,'d'])   
    __KB.release_key('d')
    __KB.release_key(__KB.shift_key) 
    pass
def somersaultBack():
    __KB.press_keys([__KB.shift_key,'s'])   
    __KB.release_key('s')
    __KB.release_key(__KB.shift_key) 
    pass

def skill_1():
    __KB.press_key('1')
    __KB.release_key('1')
def skill_2():
    __KB.press_key('2')
    __KB.release_key('2')
def skill_3():
    __KB.press_key('3')
    __KB.release_key('3')
def skill_4():
    __KB.press_key('4')
    __KB.release_key('4')
def skill_5():
    __KB.press_key('5')
    __KB.release_key('5')
def skill_6():
    __KB.press_key('6')
    __KB.release_key('6')
def skill_7():
    __KB.press_key('7')
    __KB.release_key('7')
def skill_8():
    __KB.press_key('8')
    __KB.release_key('8')
def skill_9():
    __KB.press_key('9')
    __KB.release_key('9')
def skill_0():
    __KB.press_key('0')
    __KB.release_key('0')
   

def skill_11():
    __KB.press_key('q')
    __KB.release_key('q')
def skill_12():
    __KB.press_key('r')
    __KB.release_key('r')
def skill_13():
    __KB.press_key('t')
    __KB.release_key('t')
def skill_14():
    __KB.press_key('y')
    __KB.release_key('y')

def skill_left_1():
    __KB.press_keys([__KB.control_key,'1'])   
    __KB.release_key('1')
    __KB.release_key(__KB.control_key) 
def skill_left_2():
    __KB.press_keys([__KB.control_key,'2'])   
    __KB.release_key('2')
    __KB.release_key(__KB.control_key) 
def skill_left_3():
    __KB.press_keys([__KB.control_key,'3'])   
    __KB.release_key('3')
    __KB.release_key(__KB.control_key) 
def skill_left_4():
    __KB.press_keys([__KB.control_key,'4'])   
    __KB.release_key('4')
    __KB.release_key(__KB.control_key) 
def skill_left_5():
    __KB.press_keys([__KB.control_key,'5'])   
    __KB.release_key('5')
    __KB.release_key(__KB.control_key) 
def skill_left_6():
    __KB.press_keys([__KB.control_key,'6'])   
    __KB.release_key('6')
    __KB.release_key(__KB.control_key) 
def skill_left_7():
    __KB.press_keys([__KB.control_key,'7'])   
    __KB.release_key('7')
    __KB.release_key(__KB.control_key) 
def skill_left_8():
    __KB.press_keys([__KB.control_key,'8'])   
    __KB.release_key('8')
    __KB.release_key(__KB.control_key) 
def skill_left_9():
    __KB.press_keys([__KB.control_key,'9'])   
    __KB.release_key('9')
    __KB.release_key(__KB.control_key) 
def skill_left_10():
    __KB.press_keys([__KB.control_key,'0'])   
    __KB.release_key('0')
    __KB.release_key(__KB.control_key) 
def skill_left_11():
    __KB.press_keys([__KB.alt_key,'1'])   
    __KB.release_key('1')
    __KB.release_key(__KB.alt_key) 
def skill_left_12():
    __KB.press_keys([__KB.alt_key,'2'])   
    __KB.release_key('2')
    __KB.release_key(__KB.alt_key) 
def skill_left_13():
    __KB.press_keys([__KB.alt_key,'3'])   
    __KB.release_key('3')
    __KB.release_key(__KB.alt_key) 
def skill_left_14():
    __KB.press_keys([__KB.alt_key,'4'])   
    __KB.release_key('4')
    __KB.release_key(__KB.alt_key) 
def skill_left_15():
    __KB.press_keys([__KB.alt_key,'5'])   
    __KB.release_key('5')
    __KB.release_key(__KB.alt_key) 
def skill_left_16():
    __KB.press_keys([__KB.alt_key,'6'])   
    __KB.release_key('6')
    __KB.release_key(__KB.alt_key) 
def skill_left_17():
    __KB.press_keys([__KB.alt_key,'7'])   
    __KB.release_key('7')
    __KB.release_key(__KB.alt_key) 
def skill_left_18():
    __KB.press_keys([__KB.alt_key,'8'])   
    __KB.release_key('8')
    __KB.release_key(__KB.alt_key) 
def skill_left_19():
    __KB.press_keys([__KB.alt_key,'9'])   
    __KB.release_key('9')
    __KB.release_key(__KB.alt_key) 
def skill_left_20():
    __KB.press_keys([__KB.alt_key,'0'])   
    __KB.release_key('0')
    __KB.release_key(__KB.alt_key) 
def skill_left_21():
    __KB.press_keys([__KB.control_key,'q'])   
    __KB.release_key('q')
    __KB.release_key(__KB.control_key) 
def skill_left_22():
    __KB.press_keys([__KB.control_key,'e'])   
    __KB.release_key('e')
    __KB.release_key(__KB.control_key) 
def skill_left_23():
    __KB.press_keys([__KB.control_key,'r'])   
    __KB.release_key('r')
    __KB.release_key(__KB.control_key) 
def skill_left_24():
    __KB.press_keys([__KB.control_key,'t'])   
    __KB.release_key('t')
    __KB.release_key(__KB.control_key) 
def skill_left_25():
    __KB.press_keys([__KB.control_key,'y'])   
    __KB.release_key('y')
    __KB.release_key(__KB.control_key) 

def turnLeft():    
    pass

def turnRight():
    pass

def trunOver():
    pass

def turnDegree(angle):
    pass


if __name__ == '__main__':
    # somersaultForward()
    # moveForward()
    # skill_F5()
    print(__KB.function_keys)
