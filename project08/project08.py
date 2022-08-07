from tkinter import *
y_main_window = 500
x_main_window = 720
dict_moneys = {}

def Next():
    list_box_moneys.delete(0, END)
    moneys_200 = 0
    moneys_100 = 0
    moneys_50 = 0
    moneys_20 = 0
    moneys_10 = 0
    moneys_5 = 0
    moneys_2 = 0
    moneys_1 = 0
    money_n = 200
    money = float(entry_money.get())
    while True:
        if money - money_n < 0:
            money_n = 100
        if money - money_n < 0:
            money_n = 50
        if money - money_n < 0:
            money_n = 20
        if money - money_n < 0:
            money_n = 10
        if money - money_n < 0:
            money_n = 5
        if money - money_n < 0:
            money_n = 2
        if money - money_n < 0:
            money_n = 1
        money -= money_n
        if money_n == 200:
            moneys_200 += 1
        if money_n == 100:
            moneys_100 += 1
        if money_n == 50:
            moneys_50 += 1
        if money_n == 20:
            moneys_20 += 1
        if money_n == 10:
            moneys_10 += 1
        if money_n == 5:
            moneys_5 += 1
        if money_n == 2:
            moneys_2 += 1
        if money_n == 1:
            moneys_1 += 1
        if money == 0:
            break
        
    dict_moneys[200] = moneys_200
    dict_moneys[100] = moneys_100
    dict_moneys[50] = moneys_50
    dict_moneys[20] = moneys_20
    dict_moneys[10] = moneys_10
    dict_moneys[5] = moneys_5
    dict_moneys[2] = moneys_2
    dict_moneys[1] = moneys_1
    for key, value in dict_moneys.items():
        if value > 0:
            if value > 1:
                moneys_str = 'notas'
            else:
                moneys_str = 'nota'
            list_box_moneys.insert(END,
            f'{value} {moneys_str} de {key}$')

def Buttons():
    def buttondelete():
        entry_money.delete(
        len(entry_money.get())-1)
    def button0():
        entry_money.insert(END, 0)
    def button1():
        entry_money.insert(END, 1)
    def button2():
        entry_money.insert(END, 2)
    def button3():
        entry_money.insert(END, 3)
    def button4():
        entry_money.insert(END, 4)
    def button5():
        entry_money.insert(END, 5)
    def button6():
        entry_money.insert(END, 6)
    def button7():
        entry_money.insert(END, 7)
    def button8():
        entry_money.insert(END, 8)
    def button9():
        entry_money.insert(END, 9)
    button_next = Button(main_window,
    image=image_buttonnext, bd=0,
    width=60, command=Next)
    button_delete = Button(main_window,
    image=image_buttondelete, bd=0,
    width=60, command=buttondelete)
    button_0 = Button(main_window, text='0',
    height=2, width=4, command=button0)
    button_1 = Button(main_window, text='1',
    height=2, width=4, command=button1)
    button_2 = Button(main_window, text='2',
    height=2, width=4, command=button2)
    button_3 = Button(main_window, text='3',
    height=2, width=4, command=button3)
    button_4 = Button(main_window, text='4',
    height=2, width=4, command=button4)
    button_5 = Button(main_window, text='5',
    height=2, width=4, command=button5)
    button_6 = Button(main_window, text='6',
    height=2, width=4, command=button6)
    button_7 = Button(main_window, text='7',
    height=2, width=4, command=button7)
    button_8 = Button(main_window, text='8',
    height=2, width=4, command=button8)
    button_9 = Button(main_window, text='9',
    height=2, width=4, command=button9)
    button_7.place(x=130, y=150)
    button_8.place(x=185, y=150)
    button_9.place(x=245, y=150)
    button_4.place(x=130, y=205)
    button_5.place(x=185, y=205)
    button_6.place(x=245, y=205)
    button_1.place(x=130, y=260)
    button_2.place(x=185, y=260)
    button_3.place(x=245, y=260)
    button_0.place(x=185, y=315)
    button_delete.place(x=310, y=98)
    button_next.place(x=312, y=150)

main_window = Tk()
main_window.geometry(
f'{x_main_window}x{y_main_window}')
main_window.resizable(0, 0)
main_window.title('$')
entry_money = Entry(main_window, width=23)
entry_money.place(x=100, y=100, height=29)
entry_money.config(font=(10))
image_buttondelete = PhotoImage(
file=('project08/delete.png'))
image_buttonnext = PhotoImage(
file=('project08/next.png'))
list_box_moneys = Listbox(main_window,
width=35, height=22)
list_box_moneys.place(x=380, y=50)
list_box_moneys.config(font=(13))
Buttons()
main_window.mainloop()
