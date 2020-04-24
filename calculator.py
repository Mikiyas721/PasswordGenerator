import tkinter

dic = [
	{"text": "0",
	 "row": 5,
	 "column": 0,
	 "columnspan": 1
	 },
	{"text": "=",
	 "row": 5,
	 "column": 1,
	 "columnspan": 2
	 },
	{"text": "/",
	 "row": 5,
	 "column": 3,
	 "columnspan": 1
	 },
	{"text": "1",
	 "row": 4,
	 "column": 0,
	 "columnspan": 1
	 },
	{"text": "2",
	 "row": 4,
	 "column": 1,
	 "columnspan": 1
	 },
	{"text": "3",
	 "row": 4,
	 "column": 2,
	 "columnspan": 1
	 },
	{"text": "x",
	 "row": 4,
	 "column": 3,
	 "columnspan": 1
	 },
	{"text": "4",
	 "row": 3,
	 "column": 0,
	 "columnspan": 1
	 },
	{"text": "5",
	 "row": 3,
	 "column": 1,
	 "columnspan": 1
	 },
	{"text": "6",
	 "row": 3,
	 "column": 2,
	 "columnspan": 1
	 },
	{"text": "-",
	 "row": 3,
	 "column": 3,
	 "columnspan": 1
	 },
	{"text": "7",
	 "row": 2,
	 "column": 0,
	 "columnspan": 1
	 },
	{"text": "8",
	 "row": 2,
	 "column": 1,
	 "columnspan": 1
	 },
	{"text": "9",
	 "row": 2,
	 "column": 2,
	 "columnspan": 1
	 },
	{"text": "+",
	 "row": 2,
	 "column": 3,
	 "columnspan": 1
	 },
	{"text": "C",
	 "row": 1,
	 "column": 0,
	 "columnspan": 1
	 },
	{"text": "CE",
	 "row": 1,
	 "column": 1,
	 "columnspan": 1
	 },

]
mainWindow = tkinter.Tk()
mainWindow.geometry("180x180")
mainWindow.resizable(width=False, height=False)
mainWindow['padx'] = 8
mainWindow['pady'] = 8

inputField = tkinter.Entry(mainWindow)
inputField.grid(row=0, column=0, sticky='nw', columnspan=2)

buttonFrame = tkinter.Frame(mainWindow)
buttonFrame.grid(row=1, column=0, sticky='nw')

for lists in dic:
	if lists['columnspan'] == 2:
		if lists['text'] == "C":
			button = tkinter.Button(buttonFrame, text=lists['text'], width=2, background="red")
			button.grid(row=lists['row'], column=lists['column'], columnspan=lists['columnspan'])
		else:
			button = tkinter.Button(buttonFrame, text=lists['text'], width=2)
			button.grid(row=lists['row'], column=lists['column'], columnspan=lists['columnspan'])

	else:
		button = tkinter.Button(buttonFrame, text=lists['text'], width=2)
		button.grid(row=lists['row'], column=lists['column'], columnspan=lists['columnspan'])

mainWindow.mainloop()
