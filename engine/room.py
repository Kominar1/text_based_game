class Room:
    def __init__(self, roomId):
        self.roomId_ = roomId
    
    def addContents(self, item):
        self.contents_.append(item)

    def getContents(self):
        print(*self.contents_, sep = "\n")

    def searchContents(self, item):
        if item.getName().lower().strip() in self.contents_:
            return True

    

    roomId_ = 0
    contents_ = []
