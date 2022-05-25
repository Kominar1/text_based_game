import time
import sys
from item import *

def delay_print(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class Room:
    def __init__(self, roomId, roomName):
        self.roomId_ = roomId
    
    def addContents(self, item):
        self.contents_.append(item)

    def getContents(self):
        for i in self.contents_:
            delay_print(i.getName())
            print("\n")
    
    def searchContents(self, item):
        if item.getName().lower().strip() in self.contents_:
            return True

    def removeContents(self, item):
        if self.searchContents(item.getName()):
            self.contents_.remove(item)

    

    roomName = ""
    roomId_ = 0
    contents_ = []
