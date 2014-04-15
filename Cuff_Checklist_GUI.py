from Tkinter import *
import tkMessageBox

# initialise main window
def init(win):
	win.title("Glove TMG Flexible Cuff Checklist")
	win.minsize(600, 400)
	btnA.pack()
	btnB.pack()
	btnC.pack()
	btnD.pack()
	btnE.pack()

# find button callback
def checklist():
	tkMessageBox.showinfo("Checklist", "The checklist worked!")
def comms():
	tkMessageBox.showinfo("Communication", "The comm app worked!")
def camera():
	tkMessageBox.showinfo("Camera", "The camera worked!")
def terrainMap():
	tkMessageBox.showinfo("Map", "The map worked!")
def status():
	tkMessageBox.showinfo("Suit Status", "The suit status app worked!")

# create top-level window object
win = Tk()

# create a widget
checklistApp = PhotoImage(file="/home/pi/Desktop/NASA Cuff Checksheet/icons/checklist.gif")
btnA = Button(win, image=checklistApp, command=checklist)
commsApp = PhotoImage(file="/home/pi/Desktop/NASA Cuff Checksheet/icons/comms.gif")
btnB = Button(win, image=commsApp, command=comms)
cameraApp = PhotoImage(file="/home/pi/Desktop/NASA Cuff Checksheet/icons/camera.gif")
btnC = Button(win, image=cameraApp, command=camera)
mapsApp = PhotoImage(file="/home/pi/Desktop/NASA Cuff Checksheet/icons/maps.gif")
btnD = Button(win, image=mapsApp, command=terrainMap)
statusApp = PhotoImage(file="/home/pi/Desktop/NASA Cuff Checksheet/icons/status.gif")
btnE = Button(win, image=statusApp, command=status)

# initialise and start main loop
init(win)
mainloop()
