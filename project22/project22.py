from random import randint
from tkinter import *
vidas = 3
num_cpu = randint(0, 9)
combo_lifes = 0

class App:
    def __init__(self, root):
        root.geometry("400x500")
        self.entry = Entry(root)
        self.entry.config(font=(63))
        self.label_lifes = Label(root, text="Vidas=...")
        self.label_lifes.config(font=("Courier", 10))
        self.label_lifes.place(x=8, y=5)
        self.label = Label(root, text="")
        self.label.place(x=90, y=100)
        self.label.config(font=("Courie", 13))
        self.entry.place(x=110, y=5, width=180, height=50)
        self.submit = Button(root, text="Send", width=5, height=2, command=self.send)
        self.submit.place(x=300, y=10)
        self.button0 = Button(root, text="0", width=6, height=2, command=self.btn0)
        self.button0.place(x=180, y=450)
        self.button1 = Button(root, text="1", width=6, height=2, command=self.btn1)
        self.button1.place(x=90, y=360)
        self.button2 = Button(root, text="2", width=6, height=2, command=self.btn2)
        self.button2.place(x=180, y=360)
        self.button3 = Button(root, text="3", width=6, height=2, command=self.btn3)
        self.button3.place(x=270, y=360)
        self.button4 = Button(root, text="4", width=6, height=2, command=self.btn4)
        self.button4.place(x=90, y=270)
        self.button5 = Button(root, text="5", width=6, height=2, command=self.btn5)
        self.button5.place(x=180, y=270)
        self.button6 = Button(root, text="6", width=6, height=2, command=self.btn6)
        self.button6.place(x=270, y=270)
        self.button7 = Button(root, text="7", width=6, height=2, command=self.btn7)
        self.button7.place(x=90, y=180)
        self.button8 = Button(root, text="8", width=6, height=2, command=self.btn8)
        self.button8.place(x=180, y=180)
        self.button9 = Button(root, text="9", width=6, height=2, command=self.btn9)
        self.button9.place(x=270, y=180)
        root.mainloop()
    def btn0(self):
        self.entry.insert(END, 0)
        self.verify_oneNumber()
    def btn1(self):
        self.entry.insert(END, 1)
        self.verify_oneNumber()
    def btn2(self):
        self.entry.insert(END, 2)
        self.verify_oneNumber()
    def btn3(self):
        self.entry.insert(END, 3)
        self.verify_oneNumber()
    def btn4(self):
        self.entry.insert(END, 4)
        self.verify_oneNumber()
    def btn5(self):
        self.entry.insert(END, 5)
        self.verify_oneNumber()
    def btn6(self):
        self.entry.insert(END, 6)
        self.verify_oneNumber()
    def btn7(self):
        self.entry.insert(END, 7)
        self.verify_oneNumber()
    def btn8(self):
        self.entry.insert(END, 8)
        self.verify_oneNumber()
    def btn9(self):
        self.entry.insert(END, 9)
        self.verify_oneNumber()
    def verify_oneNumber(self):
        number = len(self.entry.get())
        print(num_cpu)
        if number > 1:
            self.entry.delete(-1)
    def send(self):
        global num_cpu
        global vidas
        global combo_lifes

        num_user = int(self.entry.get())
        if num_user > num_cpu:
            vidas -= 1
            self.label["text"] = "Mais para baixo"
            combo_lifes -= combo_lifes
            more_life = ""
        elif num_user < num_cpu:
            vidas -= 1
            self.label["text"] = "Mais para cima"
            combo_lifes -= combo_lifes
            more_life = ""
        elif num_cpu == num_user:
            self.label["text"] = "Você ganhou!!!"
            self.label["text"] = "Você ganhou mais 1 vida por acertar"
            combo_lifes += 1
            more_life = f"\n    ↑\n    +{combo_lifes}"
            vidas += 1
            num_cpu = randint(0, 9)
        if vidas == 0:
            self.label["text"] = f"Você ganhou 3 vidas por perder\nO número era [{num_cpu}]"
            vidas = 3
            num_cpu = randint(0, 9)
        self.label_lifes["text"] = f"Vidas={vidas}{more_life}"
App(Tk())
