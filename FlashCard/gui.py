# By Shesan G
#https://github.com/pypa/setuptools/issues/1963#issuecomment-573675633
# ^ you cant export without downgrading samtools

from tkinter import *
import pandas as pd
import random


# Change this depending on your file location.
filename = "PS-Terms.xlsx"

# Parsing Excel columns
data = pd.read_excel(filename)
term = list(data["Term"])
definition = list(data["Definition"])
known = list(data["Known"])

size = len(data)

# print(data)
# # print(term)
# # print(definition)
# # print(known)
# print(len(term))
# print(len(known))


def userin():
    global userInput
    global num

    userInput = v.get()

    num = RandNum()

    RB.config(state=DISABLED)
    WB.config(state=DISABLED)

    if userInput != 0:
        clear()
        box1.insert(INSERT, Display1())
        SC.insert(INSERT, ("Score" , score))
    elif userInput == 0:
        save()

    # print(userInput)
    # print(num)


def clear():
    box1.delete(1.0, END)
    box2.delete(1.0, END)
    SC.delete(1.0, END)


# Random index for list that is not known
def RandNum():
    num = random.randint(0, size - 1)
    while known[num] == 1:
        if random.random() <= 0.25:
            known[num] = 0
            return num
        else:
            num = random.randint(0, size - 1)
    if known[num] == 0:
        return num


def Display1():
    T = term[num]
    D = definition[num]
    if userInput == 1:
        return T
    if userInput == 2:
        return D
    if userInput == 3:
        return random.choice((T, D))


def Display3():
    box2.delete(1.0, END)
    if userInput == 1:
        box2.insert(INSERT, (definition[num]))
    if userInput == 2:
        box2.insert(INSERT, (term[num]))
    if userInput == 3:
        box2.insert(INSERT, (term[num] + "\n" + definition[num]))

    RB.config(state=NORMAL)
    WB.config(state=NORMAL)


def Correct():
    global score
    known[num] = 1
    score += 1
    userin()


def Wrong():
    global score
    known[num] = 0
    score += 1
    userin()



# Saves the file back in original excel
def save():
    data = {"Term": term, "Definition": definition, "Known": known}
    result = pd.DataFrame(data)

    writer = pd.ExcelWriter(filename)
    result.to_excel(writer, index=False, sheet_name="Sheet1")
    workbook = writer.book
    worksheet = writer.sheets["Sheet1"]
    worksheet.set_column(0, 0, 50)
    worksheet.set_column(1, 1, 100)

    writer.save()


# Variables
userInput = 1
num = 0
score = 0


##################################################################################
#Tkinter Main#
##################################################################################

mainwin = Tk()

mainwin.title("Flash Cards App. By Shesan G")

v = IntVar()

Radiobutton(
    mainwin, text="Terms", width=10, variable=v, value=1, indicatoron=0, command=userin
).grid(row=0, column=0, pady = (10,0))
Radiobutton(
    mainwin,
    text="Definitions",
    width=10,
    variable=v,
    value=2,
    indicatoron=0,
    command=userin,
).grid(row=0, column=1, pady = (10,0))
Radiobutton(
    mainwin,
    text="Mix of Both",
    width=10,
    variable=v,
    value=3,
    indicatoron=0,
    command=userin,
).grid(row=0, column=2, pady = (10,0))
Radiobutton(
    mainwin, text="SAVE", width=10, variable=v, value=0, indicatoron=0, command=userin
).grid(row=0, column=3, pady = (10,0), padx = 10)


Label(mainwin, text="Input Area").grid(row=1, column=0, sticky=W, pady=(10, 0))
box1 = Text(mainwin, height=5)
box1.grid(row=2, columnspan=3, sticky=W + E, padx=10)

Button(mainwin, text="Show Answer", command=Display3).grid(row=3, column=1)

Label(mainwin, text="Output Area").grid(row=3, column=0, sticky=W, pady=(10, 0))
box2 = Text(mainwin, height=5)
box2.grid(row=4, columnspan=3, sticky=W + E, padx=10)


Label(mainwin, text="Did you get the Term/Definition:").grid(
    row=5, column=0, sticky=W, pady=(10, 0)
)
RB = Button(mainwin, text="Right?", width=5, command=Correct)
RB.grid(row=6, column=0, sticky=W, padx=(70, 0), pady=10)
WB = Button(mainwin, text="Wrong?", width=5, command=Wrong)
WB.grid(row=6, column=0, sticky=E, padx=(0, 70), pady=10)

# Label(mainwin, text="Score:").grid(row=6, column=2)
SC = Text(mainwin, height=1, width=10)
SC.grid(row=6, column=3)

mainwin.mainloop()

