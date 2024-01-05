import PySimpleGUI as sg
import subprocess
import os

sg.theme('DarkTeal8')

def run_script(script_path):
    venv_activate = os.path.join('venv', 'Scripts', 'activate')   #run within venv
    command = f'call {venv_activate} && python "{script_path}"'
    subprocess.Popen(command, shell=True)

layout = [                                           #gui layout
    [sg.Text('Select a Python script to run:')],
    [sg.InputText(key='-SCRIPT-'), sg.FileBrowse()],
    [sg.Button('Run Script'), sg.Button('Exit')]
]

window = sg.Window('', layout)     #creates window

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':      #close, cancel script
        break
    elif event == 'Run Script':
        script_path = values['-SCRIPT-']
        
        if script_path.lower().endswith('.py'):
            os.environ.pop('PATH', None)  
            run_script(script_path)
        else:
            sg.popup_error('Please select a Python script (.py)')

window.close()
