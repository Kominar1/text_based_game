import time
import sys
from tkinter import TRUE
from item import *

def delay_print(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class Room:
    def __init__(self, roomName, roomId):
        self.roomName_ = roomName
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

    def move(self, room):
        if (self.toTheRight == room) or (self.toTheLeft == room) or (self.upAhead == room) or (self.behind == room):
            return True
    

    roomName_ = ""
    roomId_ = 0
    contents_ = []
    #What rooms you can move to
    toTheRight = ""
    toTheLeft = ""
    upAhead = ""
    behind = ""
