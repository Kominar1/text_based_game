import pathlib
from item import *
from entity import *


# Windows path: e:/Projects/text_game/game/rooms/
#Linux path: /home/kominar/Visual Studio/Projects/text_game/game/rooms/

#Gets current directory
directory = pathlib.PurePath(pathlib.Path(__file__)).parent

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
        self.alt1_ = False
        self.alt2_ = False

    #Contents fucntions
    def addContents(self, item):
        self.contents_.append(item)
    def getContents(self):
        i = 0
        string = "The current items in the room are: \n"
        for x in self.contents_:
            string += self.contents_[i].getName() + '\n'
            i+=1
        return string
    def searchContents(self, item):
        for i in range(len(self.contents_)):
            if (self.contents_[i].getName() == item):
                return True
    def removeContents(self, item):
        self.contents_.remove(item)
        if item.getNum() == 1:
            self.alt1_ = True
        elif item.getNum() == 2:
            self.alt2_ = True
        

    #Enemy functions
    def addEnemy(self, enemy):
        self.enemies_.append(enemy)
    def getEnemies(self):
        string = ''
        for i in range(len(self.enemies_)):
            string += self.enemies_[i].getName()
        return string
    def removeEnemies(self, enemy):
        self.enemies_.remove(enemy)
    def searchEnemies(self, name):
        for i in range(len(self.enemies_)):
            if (self.enemies_[i].getName() == name):
                return self.enemies_[i]
        return False
    
    #Description functions
    def getDiscription(self):
        with open(directory.joinpath('rooms', self.roomName_, self.roomName_ + '_description.txt')) as f:
            lines = f.readlines()
        f.close()
        return listToStr(lines)
    def getLook(self):
        if self.alt1_ == True and self.alt2_ == False:
            with open(directory.joinpath('rooms', self.roomName_, self.roomName_ + '_look_alt1.txt')) as f:
                lines = f.readlines()
            f.close()
            return listToStr(lines)
        elif self.alt2_ == True and self.alt1_ == False:
            with open(directory.joinpath('rooms', self.roomName_, self.roomName_ + '_look_alt2.txt')) as f:
                lines = f.readlines()
            f.close()
            return listToStr(lines)
        elif self.alt1_ == True and self.alt2_ == True:
            with open(directory.joinpath('rooms', self.roomName_, self.roomName_ + '_look_alt3.txt')) as f:
                lines = f.readlines()
            f.close()
            return listToStr(lines)
        elif self.alt1_ == False and self.alt2_ == False:
            with open(directory.joinpath('rooms', self.roomName_, self.roomName_ + '_look.txt')) as f:
                lines = f.readlines()
            f.close()
            return listToStr(lines)

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

def listToStr(list):
   
    # initialize an empty string
    str1 = ""
   
    # traverse in the string 
    for ele in list:
        str1 += ele 
   
    # return string 
    return str1