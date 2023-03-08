import PySimpleGUI as sg

sg.theme("Black")

def feet_inches_to_meters(feet, inches):
    m = feet*0.3048 + inches*0.0254
    return m

label1 = sg.Text("Enter feet", size=8)
input1 = sg.InputText(key="feet")

label2= sg.Text("Enter inches", size=8)
input2 = sg.InputText(key="inches")

buttom3 = sg.Button("Convert", size=8)
buttom4 = sg.Button("Exit", size=8)
output_text = sg.Text(key="output")

window = sg.Window("Conversor", 
                   layout= [[label1, input1],
                            [label2, input2], 
                            [buttom3, buttom4, output_text]])

while True:
        event, values = window.read()
        print(event)
        print(values)
        if event == "Convert":
                try:
                        meters = feet_inches_to_meters(float(values["feet"]), float(values["inches"]))
                        window["output"].update(value=str(meters) + " m")
                except ValueError:
                        sg.popup("Please provide two NUMBERS.", font=("Helvetica", 16))
        elif event == "Exit":
                break
        elif event == sg.WIN_CLOSED:
                break
        
        
        
window.close()