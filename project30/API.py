from tkinter import *
import Database
import checkNamePass


def Get_name_pass():
    name = entry_name.get().strip()
    password = entry_pass.get().strip()
    return name, password

def Send():
    asw = Get_User()
    DelWidget()
    if asw:
        frame = Frame(main_root, width=405, height=400, background="grey")
        frame.place(x=0, y=0)
        button_back = Button(frame, text="Back", command=frame.destroy)
        button_back.place(x=3, y=3)
        text_api = Text(frame, width=50, height=23)
        text_api.place(y=30)
        button_save = Button(frame, text="Save",
        command=lambda:Database.CreateText(Get_name_pass()[0],
        Get_name_pass()[1], text_api.get("1.0", "end")))
        button_save.place(x=368, y=3)
        text_api.insert("1.0", Get_User()[-1])
    else:
        label_info = Label(main_root, text="Não é possível entrar na conta ou as credencias estão incorretas",
        foreground="red", wraplength=100)
        label_info.config(font=("sans", 9))
        label_info.place(x=270, y=160)

def Get_User():
    name, password = Get_name_pass()
    asw = Database.Get_Account(name, password)
    return asw

def DelWidget():
    try:
        widgets = main_root.winfo_children()
        if "label" in str(widgets[-1]):
            widgets[-1].destroy()
    except:
        pass

def Create_Accnt():
    DelWidget()
    name, password = Get_name_pass()
    check_name = checkNamePass.Check(name)
    check_pass = checkNamePass.Check(password)
    if check_name and check_pass:
        asw = bool(Get_User())
        text_color = checkNamePass.Check_Account_asw(asw)
        if asw == False:
            try:
                Database.CreateAccount(name, password)
            except Exception as error:
                if "name" in str(error):
                    label_info = Label(main_root, text="Name too long",
                    foreground="red", wraplength=100)
                    label_info.config(font=("sans", 9))
                    label_info.place(x=270, y=170)
                    return None
                elif "password" in str(error):
                    label_info = Label(main_root, text="Password too long",
                    foreground="red", wraplength=100)
                    label_info.config(font=("sans", 9))
                    label_info.place(x=270, y=170)
                    return None
                else:
                    label_info = Label(main_root, text="Unexpected error",
                    foreground="red", wraplength=100)
                    label_info.config(font=("sans", 9))
                    label_info.place(x=270, y=170)
                    return None
        if text_color:
            label_info = Label(main_root, text=text_color[0],
            foreground=text_color[1])
            label_info.config(font=("sans", 9))
            label_info.place(x=270, y=170)
    info = checkNamePass.Info(check_name=check_name, check_password=check_pass)
    print(info)
    if info:
        label_info = Label(main_root, text=info,
        foreground="red", wraplength=100)
        label_info.config(font=("sans", 9))
        label_info.place(x=270, y=170)

main_root = Tk()
main_root.title("Login App")
main_root.geometry("405x400")
label_name = Label(main_root, text="Name:")
label_name.config(font=("sans"))
label_name.place(x=70, y=150)
entry_name = Entry(main_root, width=23)
entry_name.place(x=120, y=150)
label_pass = Label(main_root, text="Password:")
label_pass.config(font=("sans"))
label_pass.place(x=40, y=200)
entry_pass = Entry(main_root, width=23)
entry_pass.place(x=120, y=200)
button_send = Button(main_root, text="Login", width=6, command=Send)
button_send.place(x=330, y=370)
button_register = Button(main_root, text="Create Account", width=12,
command=Create_Accnt)
button_register.bind("<Return>", Create_Accnt)
button_register.place(x=20, y=370)
main_root.mainloop()
