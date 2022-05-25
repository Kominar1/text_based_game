import time
import sys
from player import *
from item import *
from room import *


def delay_print(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

player = Player("Kominar")