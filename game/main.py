from functions import *
from entity import *
from item import *
from room import *
from window import*
import PySimpleGUI as sg

#Creating player
player = Player("Player", "basement")

#Creating rooms

rooms = makeMap("map")
items = makeMap("item")

dead = False
first = True

layout = [
    [sg.Menu(menuLayout())],
    [sg.Text(printHelp(), key = '-DESCRIPTION-')],
    [sg.Input(key = '-INPUT-'), sg.Button('Submit', key = '-SUBMIT-')]
]

window = sg.Window('Dimensions', layout)
    
while(dead != True):
    currentRoom = searchRooms(rooms, player.getCurrentRoom())
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    
    if event == '-SUBMIT-':
        choice = values['-INPUT-'].strip().lower()

    if "start" in choice:
        start = True

    if start:
        if(first == True):
            window['-DESCRIPTION-'].update(currentRoom.getDiscription())
            first = False

        if "move" in choice:
            first = True

        if "load" in choice:
            first = True

        window['-DESCRIPTION-'].update(getChoice(choice, player, rooms, items))

if dead:
    print("You died!")
window.close()
