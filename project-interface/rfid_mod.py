from time import sleep
import RPi.GPIO as GPIO
import sys
from mfrc522 import SimpleMFRC522
#GPIO.setwarnings(False)
reader = SimpleMFRC522()
#702455483582
#659916243695
base = []
def check_valide(ID):
    for i in range(2):
        if base[i].ID == ID:
            return base[i]
    return None
class user():
    def __init__(self,ID,name,credit):
        self.ID = ID
        self.name = name
        self.credit = credit
        base.append(self)
        
"""try:
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        azzedine = user(702455483582,"azzedine lakhdar",350)
        houssam = user(659916243695,"houssam elhazami",9000000)
        if check_valide(id) != None:
            actual_user = check_valide(id)
            print("hello %s\n" % (actual_user.name))
        else:
            print("user not allowed")
        sleep(0.01)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise"""
