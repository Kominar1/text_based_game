import time
from functions import *
from entity import *
from item import *
from room import *
import PySimpleGUI as sg

directory = pathlib.PurePath(pathlib.Path(__file__)).parent

#Creating player
player = Player("Player", "basement")

#Creating rooms
rooms = makeMap("map")
items = makeMap("item")

trigger = False
dead = False
first = True
win = False

menu = [
    ['File', ['Save', 'Load']],
    ['Player', ['Health', 'Inventory', 'Equiped']],
    ['Room', ['Available']]
]

layout = [
    [sg.Menu(menu)],
    [sg.Text(printHelp(), key = '-DESCRIPTION-')],
    [sg.Input(key = '-INPUT-', do_not_clear= False), sg.Button('Submit', key = '-SUBMIT-', bind_return_key = True, button_color=('white', 'orange'))]
]

window = sg.Window('Dimensions', layout)
choice = ""
    
while(dead != True and win != True):
    event, values = window.read()
    if event == '-SUBMIT-':
        choice = values['-INPUT-'].strip().lower()
    
    if event == 'Load':
        load(items, player)
        first = True
        start = True
        sg.popup('You succesfully loaded!')

    window['-DESCRIPTION-'].update(getChoice(choice, player, rooms, window))
    currentRoom = searchRooms(rooms, player.getCurrentRoom())   

    if event == sg.WIN_CLOSED:
        break
    
    if "start" in choice:
        start = True

    if start:
        if "move" in choice:
            first = True

        if(first == True):
            if player.getCurrentRoom() == "entrance":
                if player.searchInv(player.searchItem("key")) and player.searchInv(player.searchItem("strange device")):
                    with open(directory.joinpath('rooms', 'entrance', 'entrance_description_alt1.txt')) as f:
                        lines = f.readlines()
                    f.close()
                    window['-DESCRIPTION-'].update(listToStr(lines))
                    window.refresh()
                    time.sleep(2)
                    win = True
                else:
                    window['-DESCRIPTION-'].update(currentRoom.getDiscription())
            else:
                window['-DESCRIPTION-'].update(currentRoom.getDiscription())
            first = False

        if event == 'Save':
            save(player)
            sg.popup('You succesfully saved!')

        if event == 'Inventory':
            sg.popup(inventory(player))

        if event == 'Health':
            sg.popup("Your health is at: " + str(player.getHealth()))

        if event == 'Equiped':
            sg.popup(player.checkEquiped())

        if event == 'Available':
            sg.popup(available(currentRoom))
        
        if player.searchInv(player.searchItem("key")) and player.searchInv(player.searchItem("strange device")):
            if trigger == False:
                window['-DESCRIPTION-'].update("You suddently feel the strange device moving.\nYou pick it up and look at it and see a key hole suddently on it.\nYou put the key in it and turn and the device hums to life, you have a feeling the entrance is changed.")
                trigger = True

window['-DESCRIPTION-'].update("Congradulations! You have won!")
window.refresh()
time.sleep(2)
    
window.close()
