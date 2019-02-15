from PySimpleGUI import *
# Define your window here (it's a list of lists)
layout = [[Text('Row 1')],
          [Text('Row 2 '), Checkbox('Checkbox 1', OK()), Checkbox('Checkbox 2'), OK()]]
window = Window('Simple data entery window').Layout(layout)
button, values = window.Read()

# print(button, values[0], values[1])
Popup('The GUI returned:', button, values[0], values[1])
