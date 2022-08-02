from functions import *
from entity import *
from item import *
from room import *
import PySimpleGUI as sg

#Creating player
player = Player("Player", "basement")

#Creating rooms

rooms = makeMap("map")
items = makeMap("item")

dead = False
first = True

menu = [
    ['File', ['Save', 'Load']],
    ['Player', ['Health', 'Inventory', 'Equiped']]
]

layout = [
    [sg.Menu(menu)],
    [sg.Text(printHelp(), key = '-DESCRIPTION-')],
    [sg.Input(key = '-INPUT-', do_not_clear= False), sg.Button('Submit', key = '-SUBMIT-', bind_return_key = True, button_color=('white', 'orange'))]
]

window = sg.Window('Dimensions', layout)
choice = ""
    
while(dead != True):
    event, values = window.read()
    if event == '-SUBMIT-':
        choice = values['-INPUT-'].strip().lower()
    
    if event == 'Load':
        load(items, player)
        first = True
        start = True
        sg.popup('You succesfully loaded!')

    window['-DESCRIPTION-'].update(getChoice(choice, player, rooms, items))
    currentRoom = searchRooms(rooms, player.getCurrentRoom())   

    if event == sg.WIN_CLOSED:
        break
    
    if "start" in choice:
        start = True

    if start:
        if "move" in choice:
            first = True

        if(first == True):
            window['-DESCRIPTION-'].update(currentRoom.getDiscription())
            first = False

        if event == 'Save':
            save(player)
            sg.popup('You succesfully saved!')


if dead:
    print("You died!")
window.close()
