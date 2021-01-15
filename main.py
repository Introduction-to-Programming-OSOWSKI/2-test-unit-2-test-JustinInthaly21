def waterState(f):
    if f < 32:
        return "solid"
    elif f < 212:
        return "liquid"
    else:
        return "gas" 

def isDozen(d):
    if d % 12 == 0:
        return True
    else:
        return False

def toGerman(x):
    if x == "yes":
        return "ja"
    else:
        return "nein"

def stopLight(c):
    if c == "green":
        return "go"
   
    elif c == "yellow":
        return "slow"
    
    else:
        return "stop"
