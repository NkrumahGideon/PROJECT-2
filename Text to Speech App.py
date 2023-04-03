import PySimpleGUI as sg
import pyttsx3
layout = [
    [sg.Input(key='text'),sg.Button('Speak')],
    [sg.Text('Select Voice Type'),sg.Radio('Male','RADIO',key='-male-',default=True),
     sg.Radio('Female','RADIO',key='-female-')],

]

window =sg.Window('Text to Speech App',layout)

while True:
    event,values = window.read()
    engine = pyttsx3.init()
    
    if event== sg.WIN_CLOSED:
        break
    elif event == 'Speak':
        text = values['text']
        voices = engine.getProperty('voices') 


        if values['-male-']:
           engine.setProperty('voice', voices[0].id)
        else:
           engine.setProperty('voice', voices[1].id)
        
        engine.say(text)
        engine.runAndWait()

window.close()

