import random
import PySimpleGUI as sg

# list shuffling
import random

colours = ['Black', 'White']
choices = random.choice(colours)
if choices == "Black":
    var = "White"
elif choices == "White":
    var = "Black"

# gui

sg.theme("DarkAmber")
# This is the windows contents.
layout = [[sg.Text(
    "Hello! This is a simple chess colour decider, used to help you when you can't decide what piece you want to play! It's easy! Just Write the name of Player1 in the first box and Player2 in the other!")],
          [sg.Input(key='-INPUT-')],
          [sg.Input(key='-INPUT1-')],
          [sg.Text(size=(150, 2), key='-OUTPUT-')],
          [sg.Button('Randomize!', bind_return_key=True), sg.Button('Cancel.')]]

# Create the window
window = sg.Window('Chess Colour Decider', layout)

# This is the events (button presses) and values (input) infinite loop.
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Cancel.':
        break
    # Output a message to the window
    window['-OUTPUT-'].update(values['-INPUT-'] + ' plays the ' + choices + ' pieces and ' + values['-INPUT1-'] + ' plays the ' + var + ' pieces!')

# Finish up by removing from the screen
window.close()
