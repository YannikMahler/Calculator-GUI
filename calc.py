from tkinter import Tk,Button,Frame,Label

# Initialisierung des Fensters
window = Tk()
window.geometry('570x600+100+200')
window.title('GUI Calculator')
window.resizable(False,False)
window.configure(bg='#17171E')

# Bedienungsfunktionen
equation = ""

def show(value):
    global equation
    equation+=value
    result_label.config(text=equation)
    
def clear():
    global equation
    equation = ""
    result_label.config(text=equation)
    
def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    result_label.config(text=result)
    

# Ergebnisdisplay
result_label=Label(window, width=25, height=2, text="", font=("arial", 30))
result_label.pack()


# Buttons
Button(window, text="C", width=5, height=1, font=("arial", 30, "bold"), fg="#fff", bg="#0087ba", bd=1, command=lambda: clear()).place(x=10, y=105)
Button(window, text="/", width=5, height=1, font=("arial", 30, "bold"), fg="#fff", bg="#e59866", bd=1, command=lambda: show("/")).place(x=150, y=105)
Button(window, text="%", width=5, height=1, font=("arial", 30, "bold"), fg="#fff", bg="#e59866", bd=1, command=lambda: show("%")).place(x=290, y=105)
Button(window, text="*", width=5, height=1, font=("arial", 30, "bold"), fg="#fff", bg="#e59866", bd=1, command=lambda: show("*")).place(x=430, y=105)

Button(window, text="7", width=5, height=1, font=("arial", 30, "bold"), fg="#fff", bg="#2A2E36", bd=1, command=lambda: show("7")).place(x=10, y=200)
Button(window, text="8", width=5, height=1, font=("arial", 30, "bold"), fg="#fff", bg="#2A2E36", bd=1, command=lambda: show("8")).place(x=150, y=200)
Button(window, text="9", width=5, height=1, font=("arial", 30, "bold"), fg="#fff", bg="#2A2E36", bd=1, command=lambda: show("9")).place(x=290, y=200)
Button(window, text="-", width=5, height=1, font=("arial", 30, "bold"), fg="#fff", bg="#e59866", bd=1, command=lambda: show("-")).place(x=430, y=200)

Button(window, text="4", width=5, height=1, font=("arial", 30, "bold"), fg="#fff", bg="#2A2E36", bd=1, command=lambda: show("4")).place(x=10, y=300)
Button(window, text="5", width=5, height=1, font=("arial", 30, "bold"), fg="#fff", bg="#2A2E36", bd=1, command=lambda: show("5")).place(x=150, y=300)
Button(window, text="6", width=5, height=1, font=("arial", 30, "bold"), fg="#fff", bg="#2A2E36", bd=1, command=lambda: show("6")).place(x=290, y=300)
Button(window, text="+", width=5, height=1, font=("arial", 30, "bold"), fg="#fff", bg="#e59866", bd=1, command=lambda: show("+")).place(x=430, y=300)

Button(window, text="1", width=5, height=1, font=("arial", 30, "bold"), fg="#fff", bg="#2A2E36", bd=1, command=lambda: show("1")).place(x=10, y=400)
Button(window, text="2", width=5, height=1, font=("arial", 30, "bold"), fg="#fff", bg="#2A2E36", bd=1, command=lambda: show("2")).place(x=150, y=400)
Button(window, text="3", width=5, height=1, font=("arial", 30, "bold"), fg="#fff", bg="#2A2E36", bd=1, command=lambda: show("3")).place(x=290, y=400)
Button(window, text="0", width=11, height=1, font=("arial", 30, "bold"), fg="#fff", bg="#2A2E36", bd=1, command=lambda: show("0")).place(x=10, y=500)

Button(window, text=".", width=5, height=1, font=("arial", 30, "bold"), fg="#fff", bg="#2A2E36", bd=1, command=lambda: show(".")).place(x=290, y=500)
Button(window, text="=", width=5, height=3, font=("arial", 30, "bold"), fg="#fff", bg="#c65100", bd=1, command=lambda: calculate()).place(x=430, y=400)


window.mainloop()