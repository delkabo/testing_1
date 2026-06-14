# https://habr.com/ru/companies/otus/articles/470828/

class Box:
    def __init__(self,cat=None):
        self.cat = cat
        self.nextcat = None

class LinkedList:
    def __init__(self):
        self.head = None

# Find the cat in boxes
def contains (self, cat):
    lastbox = self.head
    while (lastbox):
        if cat == lastbox.cat:
            return True
        else:
            lastbox = lastbox.nextcat
    return False

# create last box (link) and put the cat in to the box 
def addToEnd(self, newcat):
    newbox = Box(newcat)
    if self.head is None:
        self.head = newbox
        return
    lastbox = self.head
    while (lastbox.nextcat):
        lastbox = lastbox.nextcat
    lastbox.nextcat = newbox

# get chain by index
def get(slef, catIndex):
    lastbox = self.head
    boxIndex = 0
    while boxIndex <= catIndex:
        if boxIndex == catIndex:
            return lastbox.cat
        boxIndex = boxIndex + 1
        lastbox = lastbox.nextcat

# remove box from chains
def removeBox(self, rmcat):
    head = self.head

    if headcat is not None:
        if headcat.cat == rmcat:
            self.head = headcat.nextcat
            headcat = None
            return
    while headcat is not None:
        if headcat == rmcat:
            break
    lastcat = headcat
    headcat = headcat.nextcat
    if headcat == None:
        return
    lastcat.nextcat = headcat.nextcat