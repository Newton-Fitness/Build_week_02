import PySimpleGUI as sg
from PIL import Image, ImageTk
import io
import os
import glob
sg.theme('Topanga')      # Add some color to the window

# Very basic window.  Return values using auto numbered keys
file_types = [("All files (*.*)", "*.*")]
def load_image(path, window):
    try:
        image = Image.open(path)
        image.thumbnail((400, 400))
        photo_img = ImageTk.PhotoImage(image)
        window["image"].update(data=photo_img)
    except:
        print(f"Unable to open {path}!")

def main():
	layout = [
		[sg.Text('Please enter your LoginID')],
		[sg.Text('LoginID', size=(15, 1)), sg.InputText()],
		[sg.Text('Please enter your password')],
		[sg.Text('password', size=(15, 1)), sg.InputText()],
		[sg.Submit(), sg.Cancel()],
		[sg.Image(key="-IMAGE-")],
		[
			sg.Text("Image File"),
			sg.FileBrowse(file_types=file_types),
			sg.Button("load"),
			sg.Button("Next"),

		],
	]

	window = sg.Window('Newton Fitness Interface', layout,size=(1080, 512))
	event, values = window.read()
	filename = "github.png" #values["-FILE-"]
	flag = False
	path = "/home/simple/ai/strive/team_apple_watch/dilan/Build_week_02/index_2.ico"
	load_image(path, window)
	while True:
		event, values = window.read()
		if event == "Exit" or event == sg.WIN_CLOSED:
			break
		if event == "Next":
			if flag == True:
				load_image('/home/simple/ai/strive/team_apple_watch/dilan/Build_week_02/github.png', window)
				flag = False
		if event == "load":
				flag = True

	window.close()
	print(event, values[0], values[1])


if __name__== "__main__":
	main()