import PySimpleGUI as sg

label1 = sg.Text("Enter feet")
input1 = sg.InputText()

label2= sg.Text("Enter inches")
input2 = sg.InputText()

buttom3 = sg.Button("Convert")

window = sg.Window("Conversor", 
                   layout= [[label1, input1],
                            [label2, input2],
                            [buttom3]])

window.read()
window.close()