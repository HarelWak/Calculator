from tkinter import *

app = Tk()

app.title("Calculator")
app.geometry("500x600")
app.resizable(False, False)

label = Label(app, text="Calculator", font=("Arial", 20))
label.pack()
    
text = Text(app, width="60", height="5")
text.pack()

def reset():
    text.delete(1.0, END)

reset_button = Button(app, text='Reset', command=reset, width='16', height='5')
reset_button.place(x=8, y=124)

def change_sign():
    try:
        content = text.get(0.0, END)
        text.delete(1.0, END)
        text.insert(0.0, str(0 - float(content)))
    except:
        text.delete(1.0, END)
        text.insert(0.0, "ERROR")

change_sign_button = Button(app, text='+/-', command=change_sign, width='16', height='5')
change_sign_button.place(x=129, y=124)

def percent():
    try:
        content = text.get(0.0, END)
        text.delete(1.0, END)
        text.insert(0.0, str(float(content) / 100))
    except:
        text.delete(1.0, END)
        text.insert(0.0, "ERROR")

precent_button = Button(app, text='%', command=percent, width='16', height='5')
precent_button.place(x=250, y=124)

# Operations
sign = ''
num1 = 0

def set_sign(new_sign):
    global sign
    global num1

    if new_sign == '=':
        operation()
        sign = ''
    else:
        sign = new_sign
        num1 = float(text.get(1.0, END).strip())
        text.delete(1.0, END)

def operation():
    global sign

    try:
        num2 = float(text.get(1.0, END).strip())
        result = 0

        if sign == '/':
            result = num1 / num2
        elif sign == '*':
            result = num1 * num2
        elif sign == '-':
            result = num1 - num2
        elif sign == '+':
            result = num1 + num2

        text.delete(1.0, END)
        text.insert(1.0, str(result))
    except:
        text.delete(1.0, END)
        text.insert(1.0, "ERROR")


division_button = Button(app, text='/', command=lambda operation='/': set_sign(operation), width='16', height='5')
division_button.place(x=371, y=124)

multiplication_button = Button(app, text='*', command=lambda operation='*': set_sign(operation), width='16', height='5')
multiplication_button.place(x=371, y=210)

subtraction_button = Button(app, text='-', command=lambda operation='-': set_sign(operation), width='16', height='5')
subtraction_button.place(x=371, y=296)

addition_button = Button(app, text='+', command=lambda operation='+': set_sign(operation), width='16', height='5')
addition_button.place(x=371, y=382)

equal_button = Button(app, text='=', command=lambda operation='=': set_sign(operation), width='16', height='5')
equal_button.place(x=371, y=468)

# Digits
def set_digit(new_digit):
    text.insert(END, new_digit)

seven_button = Button(app, text='7', command=lambda operation='7': set_digit(operation), width='16', height='5')
seven_button.place(x=8, y=210)

eight_button = Button(app, text='8', command=lambda operation='8': set_digit(operation), width='16', height='5')
eight_button.place(x=129, y=210)

nine_button = Button(app, text='9', command=lambda operation='9': set_digit(operation), width='16', height='5')
nine_button.place(x=250, y=210)

four_button = Button(app, text='4', command=lambda operation='4': set_digit(operation), width='16', height='5')
four_button.place(x=8, y=296)

five_button = Button(app, text='5', command=lambda operation='5': set_digit(operation), width='16', height='5')
five_button.place(x=129, y=296)

six_button = Button(app, text='6', command=lambda operation='6': set_digit(operation), width='16', height='5')
six_button.place(x=250, y=296)

one_button = Button(app, text='1', command=lambda operation='1': set_digit(operation), width='16', height='5')
one_button.place(x=8, y=382)

two_button = Button(app, text='2', command=lambda operation='2': set_digit(operation), width='16', height='5')
two_button.place(x=129, y=382)

three_button = Button(app, text='3', command=lambda operation='3': set_digit(operation), width='16', height='5')
three_button.place(x=250, y=382)

zero_button = Button(app, text='0', command=lambda operation='0': set_digit(operation), width='33', height='5')
zero_button.place(x=8, y=468)

point_button = Button(app, text='.', command=lambda operation='.': set_digit(operation), width='16', height='5')
point_button.place(x=250, y=468)

app.mainloop()