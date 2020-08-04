from tkinter import *
from datetime import date
import time as t

mainWindow = Tk()
mainWindow.title("Todo List")
mainWindow.geometry("500x500")
mainWindow['padx'] = 8
mainWindow['pady'] = 8

titleLabel = Label(mainWindow, text="Title")
titleLabel.grid(row=1, column=1, sticky="w")

titleField = Entry(mainWindow)
titleField.grid(row=1, column=2)

descriptionLabel = Label(mainWindow, text="Description")
descriptionLabel.grid(row=2, column=1)

descriptionField = Text(mainWindow, width=15, height=10)
descriptionField.grid(row=2, column=2, sticky="w")

dateFrame = LabelFrame(mainWindow, text="Select Date(dd:mm:yy)")
dateFrame.grid(row=1, column=3)
dateFrame['padx'] = 5
dateFrame['pady'] = 5

daySpinner = Spinbox(dateFrame, width=3, value=tuple(range(1, 31)))
daySpinner.grid(row=0, column=0)
daySpinner.delete(0, "end")
daySpinner.insert(0, date.today().day)

monthSpinner = Spinbox(dateFrame, width=4, value=tuple(range(1, 12)))
monthSpinner.grid(row=0, column=1)
monthSpinner.delete(0, "end")
monthSpinner.insert(0, date.today().month)

yearSpinner = Spinbox(dateFrame, width=5, value=tuple(range(2020, 2100)))
yearSpinner.grid(row=0, column=2)
yearSpinner.delete(0, "end")
yearSpinner.insert(0, date.today().year)

timeFrame = LabelFrame(mainWindow, text="Select Time(hh:mm:ss)")
timeFrame.grid(row=2, column=3)
timeFrame['padx'] = 5
timeFrame['pady'] = 5

hourSpinner = Spinbox(timeFrame, width=3, value=tuple(range(1, 25)), textvariable=2)
hourSpinner.grid(row=0, column=0)
hourSpinner.delete(0, "end")
hourSpinner.insert(0, t.localtime(t.time()).tm_hour)

minuteSpinner = Spinbox(timeFrame, width=4, value=tuple(range(1, 60)))
minuteSpinner.grid(row=0, column=1)
minuteSpinner.delete(0, "end")
minuteSpinner.insert(0, t.localtime(t.time()).tm_min)

secondSpinner = Spinbox(timeFrame, width=5, value=tuple(range(1, 60)))
secondSpinner.grid(row=0, column=2)
secondSpinner.delete(0, "end")
secondSpinner.insert(0, t.localtime(t.time()).tm_sec)

okButton = Button(mainWindow, text="Ok", bg="#77aaff", fg="white")
okButton.grid(row=4, column=2, sticky="e")

cancelButton = Button(mainWindow, text="Cancel", bg="#ffaa77", fg="white")
cancelButton.grid(row=4, column=3, sticky="w")

mainWindow.mainloop()
