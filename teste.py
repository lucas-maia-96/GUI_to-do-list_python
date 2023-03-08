import PySimpleGUI as sg

sg.theme('SystemDefaultForReal')

col1 = [[sg.Text('Vertical')],
        [sg.Radio('A', 'group 1', key='VA', enable_events=True)],
        [sg.Radio('B', 'group 1', key='VB', enable_events=True)]
        ]

col2 = [[sg.Text('Horizontal'),
         sg.Radio('A', 'group 2', key='HA', enable_events=True),
         sg.Radio('B', 'group 2', key='HB' , enable_events=True)
         ]]

layout = [[sg.Column(col1), sg.VSeparator(), sg.Column(col2)]]

window =sg.Window('Columns', layout, resizable=True, finalize=True)
while True:  # The Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break

window.close()

"""https://stackoverflow.com/questions/65083402/pysimplegui-align-rows-on-different-columns"""