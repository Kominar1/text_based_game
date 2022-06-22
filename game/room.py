import time
import sys
from tkinter import TRUE
from item import *
from entity import *

# Windows path: e:/Projects/text_game/game/rooms/
#Linux path: /home/kominar/Visual Studio/Projects/text_game/game/rooms/


def delay_print(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class Room:
    def __init__(self, roomName, roomId, toTheRight, toTheLeft, upAhead, behind):
        self.roomName_ = roomName
        self.roomId_ = roomId
        self.contents_ = []
        self.enemies_ = []
        self.toTheRight_ = toTheRight
        self.toTheLeft_ = toTheLeft
        self.upAhead_ = upAhead
        self.behind_ = behind
        
    #Contents fucntions
    def addContents(self, item):
        self.contents_.append(item)
    def getContents(self):
        i = 0
        print("The current items in the room are: ")
        for x in self.contents_:
            print(self.contents_[i].getName())
            i+=1
    def searchContents(self, item):
        i = 0
        for x in self.contents_:
            if (self.contents_[i].getName() == item):
                return True
            i+=1
    def removeContents(self, item):
        self.contents_.remove(item)

    #Enemy functions
    def addEnemy(self, enemy):
        self.enemies_.append(enemy)
    def getEnemies(self):
        i = 0
        for x in self.enemies_:
            print(self.enemies_[i].getName())
            i+=1   
    def removeEnemies(self, enemy):
        self.enemies_.remove(enemy)
    
    #Description functions
    def getDiscription(self):
        with open('e:/Projects/text_game/game/rooms/' + self.roomName_ + '/' + self.roomName_ + '_description.txt') as f:
            lines = f.readlines()
            delay_print(lines)
    def getLook(self):
        with open('e:/Projects/text_game/game/rooms/' + self.roomName_ + '/' + self.roomName_ + '_look.txt') as f:
            lines = f.readlines()
            delay_print(lines)
    def getLookAlt(self):
        with open('e:/Projects/text_game/game/rooms/' + self.roomName_ + '/' + self.roomName_ + '_look_alt.txt') as f:
            lines = f.readlines()
            delay_print(lines)

    #Adjasent room functions
    def getTheRight(self):
        return self.toTheRight_
    def getTheLeft(self):
        return self.toTheLeft_
    def getAhead(self):
        return self.upAhead_
    def getBehind(self):
        return self.behind_
    
    def getName(self):
        return self.roomName_
    def move(self, room):
        if (self.toTheRight_ == room) or (self.toTheLeft_ == room) or (self.upAhead_ == room) or (self.behind_ == room):
            return True
        else:
            return False

    roomName_ = ""
    roomId_ = 0
    contents_ = []
    enemies_ = []
    #What rooms you can move to
    toTheRight_ = ""
    toTheLeft_ = ""
    upAhead_ = ""
    behind_ = ""
