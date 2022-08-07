from tkinter import *
from os import system
from threading import Thread

def New():
    def create():
        file_name = entry_name_new.get()
        with open(f'project09/py_files/{file_name}.py',
        'w', encoding='utf-8') as create:
            create.seek(0, 0)
    window_new = Toplevel(root)
    window_new.geometry('300x140')
    button_create_new = Button(window_new, text='Create', command=create)
    entry_name_new = Entry(window_new, width=33)
    button_create_new.place(x=250, y=110)
    entry_name_new.place(x=45, y=50)
def save_code():
    with open('project09/py_files/main.py',
    'w', encoding='utf-8') as write_lines:
        write_lines.write(editor.get(1.0, END))

def run_code():
    cmd_run = 'cd project09/py_files/ && python main.py'
    system(cmd_run)

def start_run_code():
    Thread(target=run_code).start()

root = Tk()
root.title('PY Code Editor')
root.geometry('808x600')
editor = Text(root, height=35, width=80, background='black', foreground='white')
editor.place(x=163, y=0)
button_save = Button(root, text='Save', command=save_code)
button_save.place(x=760, y=570)
button_run = Button(root, text='Run Code', command=start_run_code)
button_run.place(x=690, y=570)
button_create_file = Button(root, text='New', command=New)
button_create_file.place(x=10, y=570)
list_files = Listbox(root, height=35, width=26)
list_files.place(x=1, y=0)
root.mainloop()
