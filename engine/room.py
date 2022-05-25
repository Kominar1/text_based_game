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
    def __init__(self, roomName, roomId, toTheRight, toTheLeft, upAhead, behind):
        self.roomName_ = roomName
        self.roomId_ = roomId
        self.toTheRight_ = toTheRight
        self.toTheLeft_ = toTheLeft
        self.upAhead_ = upAhead
        self.behind_ = behind
    
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
        if (self.toTheRight_ == room) or (self.toTheLeft_ == room) or (self.upAhead_ == room) or (self.behind_ == room):
            return True
        else:
            return False
    
    def getDiscription(self):
        with open('E:/Projects/text_game_engine/engine/rooms/' + self.roomName_ + '/' + self.roomName_ + '_description.txt') as f:
            lines = f.readlines()
            delay_print(lines)

    def getLook(self):
        with open('E:/Projects/text_game_engine/engine/rooms/' + self.roomName_ + '/' + self.roomName_ + '_look.txt') as f:
            lines = f.readlines()
            delay_print(lines)

    def getLookAlt(self):
        with open('E:/Projects/text_game_engine/engine/rooms/' + self.roomName_ + '/' + self.roomName_ + '_look_alt.txt') as f:
            lines = f.readlines()
            delay_print(lines)

    def getTheRight(self):
        return self.toTheRight_

    def getTheLeft(self):
        return self.toTheLeft_
    
    def getAhead(self):
        return self.upAhead_

    def getBehind(self):
        return self.behind_

    roomName_ = ""
    roomId_ = 0
    contents_ = []
    #What rooms you can move to
    toTheRight_ = ""
    toTheLeft_ = ""
    upAhead_ = ""
    behind_ = ""
