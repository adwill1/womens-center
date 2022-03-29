#make sure to install PySimpleGUI on your laptop
#can be done easily from the command prompt/shell
#https://realpython.com/pysimplegui-python/
#https://pypi.org/project/PySimpleGUI/
#Initial install for Windows: 
#python -m pip install PySimpleGUI
#Initial install for Linux and MacOS:
#python3 -m pip install PySimpleGUI


import requests
import json
import PySimpleGUI as sg 

def get_data_from_api(): #will be changed once we determine how to access the api
    url = " https://webservice.kareo.com/services/soap/2.1/KareoServices.svc?singleWsdl" #need to fix this url once we get access
    r = requests.get(url)
    data = r.text
    dict_list = json
    data_list = list(dict_list.keys()) 
    return data_list

#def main():

# Define the window's contents
layout = [[sg.Text("What's your name?")], [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Window Title', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()