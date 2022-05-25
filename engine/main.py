import time
import sys
from player import *
from item import *
from room import *


def delay_print(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)

player = Player("Kominar", "basement")
basement = Room("basement", 1, "null", "null", "hallway", "null")
flashlight = Item("flashlight", 5)
basement.addContents(flashlight)
basement.getDiscription()
basement.getLook()
basement.getLookAlt()