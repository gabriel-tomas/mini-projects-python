import random
from tkinter import *
from tkinter import Canvas
from threading import Thread as Td
from time import sleep
from emoji import emojize

cookies = 0
cookies_per_click = 1
BACKGROUND_INFO_BUY = "#5e411b"
quit_app = False
boosts = [17, 100, 400, 1100]
clicks_boosts = [0.2, 0.4, 0.5, 1.1]
pos = [[20, 0], [50, 0], [80, 0], [100, 0], [150, 0],
        [230, 0], [300, 0], [400, 0], [500, 0], [580, 0],
        [550, 0], [350, 0], [60, 0], [120, 0], [200, 0],
        [520, 0], [450, 0], [350, 0], [450, 0]]
speeds = [2, 3, 4, 5, 6, 7, 8]
kill_time = {2:310, 3:205, 4:155, 5:125, 6:102, 7:88, 8:77}


def Move_Cookie(canvas, posx, speed, time_kill):
    cookie_item = canvas.create_oval(posx, -24, posx + 24, 0, fill="#b5754a")
    def Move_cookie(canvas, speed, time_kill):
        c = 0
        while True:
            c += 1
            if quit_app:
                break
            canvas.move(cookie_item, 0, speed)
            sleep(0.005)
            if c == time_kill:
                c = 0
                canvas.delete(cookie_item)
                break
    Move_cookie(canvas=canvas, speed=speed, time_kill=time_kill)

def Cookies():
    c = 0
    while True:
        c += 1
        if quit_app:
            break
        sleep(0.08)
        position = random.choice(pos)
        speed = random.choice(speeds)
        kill = kill_time[speed]
        x, y = position
        Td(target=Move_Cookie, args=(cookie_canvas, x, speed, kill)).start()

def Init_Cookies():
    Td(target=Cookies).start()

def Click_Cookie(position):
    global cookies

    cookies += cookies_per_click
    cookies_label["text"] = f"Cookies: {cookies:.2f}"
    chance_golden_cookie = random.randint(0, 3)
    if chance_golden_cookie == 1:
        Golden_Cookie()
    if cookies >= 120:
        Clear_Cookies()
    

def Buy_Boosts_Cookies(buy, clicks_quant):
    global cookies
    global cookies_per_click

    if cookies >= buy:
        cookies -= buy
        cookies_per_click += clicks_quant
        cookies_label["text"] = f"Cookies: {cookies:.2f}"
        cookies_per_click_label["text"] = f"Cookies \np/ click: {cookies_per_click:.2f}"
        Increase_Cookies_Booster(buy)
    else:
        print("Não é possível comprar")

def Increase_Cookies_Booster(buy):
    for i, boost in enumerate(boosts):
        if boost == buy:
            boosts[i] += boost / 6
            clicks_boosts[i] += clicks_boosts[i] / 8
    print(clicks_boosts)
    print(boosts)
    click_label["text"] = f"{boosts[0]:.2f}{emojize(':cookie:')}"
    grandpa_label["text"] = f"{boosts[1]:.2f}{emojize(':cookie:')}"
    farm_label["text"] = f"{boosts[2]:.2f}{emojize(':cookie:')}"
    industry_label["text"] = f"{boosts[3]:.2f}{emojize(':cookie:')}"

def Clear_Cookies():
    global cookies

    with open("project24/Cookies.txt", "w", encoding="utf-8") as last_cookies:
        last_cookies.write(str(cookies))
    del cookies
    with open("project24/Cookies.txt", "r", encoding="utf-8") as new_cookies:
        cookies = new_cookies.readline()
    cookies = float(cookies)

def Quit_App():
    global quit_app

    root.destroy()
    quit_app = True

def Golden_Cookie():
    x, y = random.randint(24, 550), random.randint(24, 550)
    gold_cookie_canvas = Canvas(root, width=24, height=24, background="#ffd500")
    gold_cookie_canvas.place(x=x, y=y)
    gold_cookie_canvas.bind("<Button-1>", lambda event: Init_Bonus_Golden_Cookie(event, gold_cookie_canvas))
    Td(target=Time_Golden_Cookie, args=(gold_cookie_canvas,)).start()

def Time_Golden_Cookie(object):
    print(object)
    sleep(4)
    object.destroy()

def Bonus_Golden_Cookie():
    global cookies_per_click
    
    last_value_cookie = cookies_per_click
    cookies_per_click = cookies_per_click * 10
    cookies_per_click_label["text"] = f"Cookies \np/ click: {cookies_per_click:.2f} x10{emojize(':cookie:')}"
    sleep(10)
    cookies_per_click = last_value_cookie
    cookies_per_click_label["text"] = f"Cookies \np/ click: {cookies_per_click:.2f}"

def Init_Bonus_Golden_Cookie(position, object):
    object.destroy()
    Td(target=Bonus_Golden_Cookie).start()


root = Tk()
root.title("Click Cookie")
root.resizable(0, 0)
root.geometry("850x600")
frame_info_buy = Frame(root, width=250, height=600, background=BACKGROUND_INFO_BUY)
frame_info_buy.place(x=600, y=0)
infos_label = Label(frame_info_buy, text="Coust", background=BACKGROUND_INFO_BUY)
infos_label.config(font=("Courier", 9))
infos_label.place(x=140, y=0)
click = Button(frame_info_buy, text="Buy", foreground="green", background=BACKGROUND_INFO_BUY,
                activebackground=BACKGROUND_INFO_BUY, bd=0, command=lambda: Buy_Boosts_Cookies(boosts[0], clicks_boosts[0]))
click.config(font=("Courier", 8))
click.place(x=20, y=20)
click_label_text = Label(frame_info_buy, text="Click", background=BACKGROUND_INFO_BUY)
click_label_text.config(font=("Courier", 10))
click_label_text.place(x=70, y=20)
click_label = Label(frame_info_buy, text=f"{boosts[0]:.2f}{emojize(':cookie:')}", background=BACKGROUND_INFO_BUY)
click_label.config(font=("Courier", 10))
click_label.place(x=150, y=20)
grandpa = Button(frame_info_buy, text="Buy", foreground="green", background=BACKGROUND_INFO_BUY,
                activebackground=BACKGROUND_INFO_BUY, bd=0, command=lambda: Buy_Boosts_Cookies(boosts[1], clicks_boosts[1]))
grandpa_label = Label(frame_info_buy, text=f"{boosts[1]:.2f}{emojize(':cookie:')}", background=BACKGROUND_INFO_BUY)
grandpa_label.config(font=("Courier", 10))
grandpa_label.place(x=150, y=50)
grandpa_label_text = Label(frame_info_buy, text="Grandpa", background=BACKGROUND_INFO_BUY)
grandpa_label_text.config(font=("Courier", 10))
grandpa_label_text.place(x=70, y=50)
grandpa.place(x=20, y=50)
grandpa.config(font=("Courier", 8))
farm = Button(frame_info_buy, text="Buy", foreground="green", background=BACKGROUND_INFO_BUY,
            activebackground=BACKGROUND_INFO_BUY, bd=0, command=lambda: Buy_Boosts_Cookies(boosts[2], clicks_boosts[2]))
farm_label = Label(frame_info_buy, text=f"{boosts[2]:.2f}{emojize(':cookie:')}", background=BACKGROUND_INFO_BUY)
farm_label.config(font=("Courier", 10))
farm_label.place(x=150, y=80)
farm_label_text = Label(frame_info_buy, text="Farm", background=BACKGROUND_INFO_BUY)
farm_label_text.config(font=("Courier", 10))
farm_label_text.place(x=70, y=80)
farm.config(font=("Courier", 8))
farm.place(x=20, y=80)
industry = Button(frame_info_buy, text="Buy", foreground="green", background=BACKGROUND_INFO_BUY,
                activebackground=BACKGROUND_INFO_BUY, bd=0, command=lambda: Buy_Boosts_Cookies(boosts[3], clicks_boosts[3]))
industry_label = Label(frame_info_buy, text=f"{boosts[3]:.2f}{emojize(':cookie:')}", background=BACKGROUND_INFO_BUY)
industry_label.config(font=("Courier", 10))
industry_label.place(x=150, y=110)
industry_label_text = Label(frame_info_buy, text="Industry", background=BACKGROUND_INFO_BUY)
industry_label_text.config(font=("Courier", 10))
industry_label_text.place(x=70, y=110)
industry.config(font=("Courier", 8))
industry.place(x=20, y=110)
cookie_canvas = Canvas(root, width=600, height=600)
cookie_canvas.place(x=0, y=0)
cookie_canvas.bind("<Button-1>", Click_Cookie)
cookies_label = Label(frame_info_buy, text=f"Cookies: {cookies}", background=BACKGROUND_INFO_BUY)
cookies_label.config(font=("Courier", 10))
cookies_label.place(x=20, y=570)
cookies_per_click_label = Label(frame_info_buy, text=f"Cookies \np/ click: {cookies_per_click}",
                                background=BACKGROUND_INFO_BUY, justify=LEFT)
cookies_per_click_label.config(font=("Courier", 10))
cookies_per_click_label.place(x=20, y=520)
Init_Cookies()
root.wm_protocol("WM_DELETE_WINDOW", Quit_App)
root.mainloop()
