import tkinter as tk


window = tk.Tk()
window.title("My first Program in Tkinter")
window.geometry("300x300")

label = "Hola"

def updateLabel():
    import random

    languages = ["Hello there!", "Konnichiwa", "Guten tag", "Bore Da!", "Hola", "Ciao"]
    index = random.randint(0,5)

    label = f"{languages[index]}"
    hello["text"] = label

hello = tk.Label(window, text=label)
hello.pack()

text = tk.Text(window, height=1,width=25)
text.pack()

button = tk.Button(window, text="Click me!", command=updateLabel)
button.pack()

window.mainloop()