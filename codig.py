import PySimpleGUI as sg

def feet_inches_to_meters(feet, inches):
    m = feet*0.3048 + inches*0.0254
    return m

label1 = sg.Text("Enter feet")
input1 = sg.InputText(key="feet")

label2= sg.Text("Enter inches")
input2 = sg.InputText(key="inches")

buttom3 = sg.Button("Convert")
output_text = sg.Text(key="output")

window = sg.Window("Conversor", 
                   layout= [[label1, input1],
                            [label2, input2], 
                            [buttom3, output_text]])

while True:
        event, values = window.read()
        print(event)
        print(values)
        if event == "Convert":
                meters = feet_inches_to_meters(float(values["feet"]), float(values["inches"]))
                window["output"].update(value=str(meters) + " m")
        if event == sg.WIN_CLOSED:
                break
        
        
        
window.close()