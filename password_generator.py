from tkinter import *
import random


def generate_password(length: int, random_type: str):
	if random_type == "number":
		return random.randint(0, 10 ** length)
	else:
		lower_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
					   't',
					   'u', 'v', 'w', 'x', 'y', 'z']
		upper_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
					   'T',
					   'U', 'V', 'W', 'X', 'Y', 'Z']
		if random_type == "string":
			password = ""
			for i in range(0, length):
				l_u = random.randint(0, 1)
				index = random.randint(0, 25)
				if l_u == 0:
					password += lower_alpha[index]
				else:
					password += upper_alpha[index]
			return password
		else:
			special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+', '/', '\\', ';', ':',
							',',
							'.',
							'>', '<', '?', '~']
			number = list(range(0, 10))
			password = ""
			for i in range(0, length):
				l_u_s_n = random.randint(0, 3)
				index = random.randint(0, 25)
				if l_u_s_n == 0:
					password += lower_alpha[index]
				elif l_u_s_n == 1:
					password += upper_alpha[index]
				elif l_u_s_n == 2:
					random_number = random.randint(0, 23)
					password += special_char[random_number]
				else:
					random_number = random.randint(0, 9)
					password += str(number[random_number])
			return password


mainWindow = Tk()
mainWindow.title("Password Generator")
mainWindow.geometry("400x200")
mainWindow.resizable(width=False, height=False)
mainWindow['padx'] = 8
mainWindow['pady'] = 8

mainTitleLabel = Label(mainWindow, text="Password Generator", font=16)
mainTitleLabel.grid(row=0, column=1, sticky="w")

inputLabel = Label(mainWindow, text="Password length")
inputLabel.grid(row=1, column=0, sticky="e")

lengthSpinner = Spinbox(mainWindow, values=tuple(range(6, 20)), width=3)
lengthSpinner.grid(row=1, column=1, sticky="w")

outputLabel = Label(mainWindow, text="Password", foreground="#3eef3f", font=("Helvetica", 16))
outputLabel.grid(row=2, column=1, columnspan=3, sticky="w")
outputLabel['padx'] = 25

choiceInput = LabelFrame(mainWindow, text="Password Type")
choiceInput.grid(row=1, column=4)

optionsInt = IntVar()
optionsInt.set(1)

numberRadioButton = Radiobutton(choiceInput, text="Number", value=1, variable=optionsInt)
charRadioButton = Radiobutton(choiceInput, text="String", value=2, variable=optionsInt)
alphaNumericRadioButton = Radiobutton(choiceInput, text="AlphaNumeric", value=3, variable=optionsInt)

numberRadioButton.grid(row=0, column=0, sticky="w")
charRadioButton.grid(row=1, column=0, sticky="w")
alphaNumericRadioButton.grid(row=2, column=0, sticky="w")


def on_button_click():
	if optionsInt.get() == 1:
		outputLabel.config(text=generate_password(int(lengthSpinner.get()), "number"))
	elif optionsInt.get() == 2:
		outputLabel.config(text=generate_password(int(lengthSpinner.get()), "string"))
	else:
		outputLabel.config(text=generate_password(int(lengthSpinner.get()), "alpha"))


numberRadioButton['command'] = on_button_click
charRadioButton['command'] = on_button_click
alphaNumericRadioButton['command'] = on_button_click

lengthSpinner['command'] = on_button_click

generateButton = Button(mainWindow, text="Generate", command=on_button_click)
generateButton.grid(row=3, column=1)

mainWindow.mainloop()
