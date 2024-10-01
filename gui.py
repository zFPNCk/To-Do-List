import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")

window = sg.Window("To-Do App", layout=[[label], [input_box, add_button]])
window.read()
print("Hello Word")
window.close()