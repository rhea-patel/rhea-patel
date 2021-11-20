from tkinter import *
from ttkthemes import ThemedStyle
from tkinter import messagebox
import tkinter.ttk as ttk
from numerizer import numerize
import speech_recognition as sr
import math
from threading import Thread
import time

parent_window = Tk()
parent_window.title('Voice Calculator')
parent_window.geometry('500x400')
theme= ThemedStyle(parent_window).set_theme('breeze')
style_b = ttk.Style().configure('W.TButton', font=('Helvetica', 10, 'bold'), bd=20, focuscolor=parent_window.cget('background'), background=parent_window.cget('background') )

def light():
    parent_window.config(background='white')
    ThemedStyle(parent_window).set_theme('breeze')
    label1.config(bg=parent_window.cget('background'), fg='gray')
    label2.config(bg=parent_window.cget('background'), fg='gray')
    tap_label.config(bg=parent_window.cget('background'), fg='gray')
    voice_button.config(bg=parent_window.cget('background'), fg='black')

def dark():
    parent_window.config(background='cyan')
    ThemedStyle(parent_window).set_theme('black')
    label1.config(bg=parent_window.cget('background'), fg='black')
    label2.config(bg=parent_window.cget('background'), fg='black')
    tap_label.config(bg=parent_window.cget('background'), fg='black')
    voice_button.config(bg=parent_window.cget('background'), fg='black')

bgbutton1 = ttk.Radiobutton(parent_window, text='Light', command=lambda: light(), style='W.TButton')
bgbutton2 = ttk.Radiobutton(parent_window, text='Dark', command=lambda: dark(), style='W.TButton')
bgbutton1.grid(row=0, column=2, ipady=5, pady=10)
bgbutton2.grid(row=1, column=2, ipady=5, pady=10)

label1 = Label(parent_window, text='             ', bg=parent_window.cget('background'), font=("Helvetica", 20, 'bold'), justify='left')
label2 = Label(parent_window, text='           ', bg=parent_window.cget('background'), font=("Times", 20, 'bold'), justify='left')
label1.grid(row=2, column=0, ipady=5, pady=10)
label2.grid(row=3, column=0, ipady=5, pady=10)


def multiply(*args):

    for i in args:

        if i == args[0]:

            product = 1

        product = i * product

    return 'Result: '+str(product)


def divide(a, b):

    try:

        division = a/b

        return division

    except:

        print('Division by zero is undefined')

def subtract(a, b):

    return a-b

def factorial(n, x=None):

    try:

        return math.factorial(n)

    except:

        print('Number should be a whole number')

def square_root(n, x=None):

    try:

        return math.sqrt(n)

    except:

        print('Number should be positive')

def sin(n, x=None):

    deg = math.radians(n)

    return math.sin(deg)

def cos(n, x=None):
    deg = math.radians(n)

    return math.cos(deg)

def tan(n, x=None):
    deg = math.radians(n)

    return math.tan(deg)

def cot(n, x=None):
    deg = math.radians(n)

    return 1/(math.tan(deg))

def sec(n, x=None):
    deg = math.radians(n)

    return 1/(math.cos(deg))

def cosec(n, x=None):
    deg = math.radians(n)

    return 1/(math.sin(deg))

def power(base, raised):

    return math.pow(base, raised)

def log(x, base=None):

    try:

        try:
            return math.log(x, base)

        except:

            return math.log(x)

    except:

        print('Undefined')

def voice():

    with sr.Microphone() as source:

        def animation():

            anime = 0

            while text:

                label1.config(text='Listening' + '.' * anime)

                time.sleep(0.2)

                anime += 1

                if anime == 4:
                    anime = 0

        r = sr.Recognizer()

        text = True

        ani = Thread(target=animation, daemon=True)

        ani.start()

        audio = r.listen(source)

        text0 = r.recognize_google(audio)

        text = False

        label1.config(text=text0)

        val = []

        text1 = text0.split()

        if 'hundred' in text1 or 'million' in text1 or 'billion' in text1:

            for i in range(len(text1)):

                try:
                    if not text1[i].isdigit():

                        text1[i] = numerize(text1[i]).replace(',', '')

                except:
                    pass

        try:

            if 'multiply' in text1:

                for i in text1:

                    if i.replace('.', '').isdigit():

                        if '.' in i:

                            val.append(float(i))

                        else:

                            val.append(int(i))

                label2.config(text=multiply(*val))

            if 'divide' in text1:

                for i in text1:

                    if i.replace('.', '').isdigit():

                        if '.' in i:

                            val.append(float(i))

                        else:

                            val.append(int(i))

                label2.config(text=divide(val[0], val[1]))

            if 'subtract' in text1:

                for i in text1:

                    if i.replace('.', '').isdigit():

                        if '.' in i:

                            val.append(float(i))

                        else:

                            val.append(int(i))

                label2.config(text=subtract(val[0], val[1]))

            if 'root' in text1:

                if numerize('million') in text1 or numerize('billion') in text1:

                    for x in range(len(text1)):

                        if text1[x].isdigit():
                            text1[x] = text1[x + 1].replace(text1[x + 1][0], text1[x])

                            text1.pop()

                            break

                for i in text1:

                    if i.replace('.', '').isdigit():

                        if '.' in i:

                            val.append(float(i))

                        else:

                            val.append(int(i))

                label2.config(text=square_root(val[0]))

            if 'log' in text1:

                for i in text1:

                    if numerize('million') in text1 or numerize('billion') in text1:

                        text1[1] = text1[2].replace(text1[2][0], text1[1])
                        text1.pop(2)

                    if i.replace('.', '').isdigit():

                        if '.' in i:

                            val.append(float(i))

                        else:

                            val.append(int(i))

                try:

                    label2.config(text=log(val[0], val[1]))

                except:

                    label2.config(text=log(val[0]))

            if 'sin' in text1:

                for i in text1:

                    if i.replace('.', '').isdigit():

                        if '.' in i:

                            val.append(float(i))

                        else:

                            val.append(int(i))

                label2.config(text=sin(val[0]))

            if 'cos' in text1:

                for i in text1:

                    if i.replace('.', '').isdigit():

                        if '.' in i:

                            val.append(float(i))

                        else:

                            val.append(int(i))

                label2.config(text=cos(val[0]))

            if 'tan' in text1:

                for i in text1:

                    if i.replace('.', '').isdigit():

                        if '.' in i:

                            val.append(float(i))

                        else:

                            val.append(int(i))

                label2.config(text=tan(val[0]))

            if 'cosec' in text1:

                for i in text1:

                    if i.replace('.', '').isdigit():

                        if '.' in i:

                            val.append(float(i))

                        else:

                            val.append(int(i))

                label2.config(text=cosec(val[0]))

            if 'sec' in text1:

                for i in text1:

                    if i.replace('.', '').isdigit():

                        if '.' in i:

                            val.append(float(i))

                        else:

                            val.append(int(i))

                label2.config(text=sec(val[0]))

            if 'cot' in text1:

                for i in text1:

                    if i.replace('.', '').isdigit():

                        if '.' in i:

                            val.append(float(i))

                        else:

                            val.append(int(i))

                label2.config(text=cot(val[0]))

            if 'raised' in text1 or 'power' in text1:

                for i in text1:

                    if i.replace('.', '').isdigit():

                        if '.' in i:

                            val.append(float(i))

                        else:

                            val.append(int(i))

                label2.config(text=power(val[0], val[1]))

            if 'factorial' in text1:

                for i in text1:

                    if i.replace('.', '').isdigit():

                        if '.' in i:

                            val.append(float(i))

                        else:

                            val.append(int(i))

                label2.config(text=factorial(val[0]))

        except:

            messagebox.showerror('Invalid', 'Provide Valid Statement And Value')
def voice_thread():

    voice_thread = Thread(target=voice, daemon=True)

    voice_thread.start()

mic = PhotoImage(file='mic.png')
voice_button = Button(parent_window, command=voice_thread, image=mic, borderwidth=0, width='60', height='60' )
tap_label = Label(parent_window, text='Tap To Speak', font=(" Concert One", 24, 'bold'), justify='center')
tap_label.grid(row=5, column=1, ipady=5,)
voice_button.grid(row=4, column=1, ipady=5, pady=10)
parent_window.mainloop()






