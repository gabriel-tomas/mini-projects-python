import os
from posixpath import basename
from tkinter import *
from tkinter.messagebox import askquestion

state_document = False
name_file = ''
list_files_added = []
file_cursor = 0
file_selected = ''

root = Tk()
root.geometry('600x380')
root.config(background='#404040')
root.title('OnNote')
root.iconbitmap('project01/icons/icon.ico')
root.resizable(0, 0)
frame_right = Frame(root, height=380, width=150, background='#262626')
frame_right.place(x=450, y=0)

def delete_note():
    remove = ''

    delete_select = list_files.curselection()[0]
    for i, file_delete in enumerate(list_files_added):
        if i == int(delete_select):
            remove = file_delete
    del list_files_added[int(delete_select)]
    print(list_files_added)
    
    with open(f'project01/files_created.txt', 'r', encoding='utf-8') as line_for_remove:
        lines_remove = line_for_remove.readlines()
    with open(f'project01/files_created.txt', 'w+', encoding='utf-8') as remove_line:
        for i, remove_in_list in enumerate(lines_remove):
            print(f'\033[32m{remove_in_list}\n{remove}')
            if remove_in_list == remove:
                list_files.delete(i)
                os.remove(remove_in_list[:-1])
            else:
                remove_line.write(remove_in_list)

def write_note_activate():
    global state_document
    global file_cursor
    global file_selected

    file_cursor = list_files.curselection()[0]
    for i, archive in enumerate(list_files_added):
        if int(file_cursor) == i:
            file_selected = archive
    state_document = False
    write_note()

def write_note():
    global state_document
    global file_selected
    
    frame_scroll_write = Frame(root, height=389, width=20)
    frame_scroll_write.place(x=580, y=0)
    window_write = Frame(root, background='#262626', height=380, width=580)
    window_write.place(x=0, y=0)
    text_write = Text(window_write, height=23, width=72,
    background='#262626', highlightthickness=0, bd=0, foreground='#ffffff')
    text_write.place(x=0, y=28)
    if state_document == False:
        print(file_selected)
        with open(f'{file_selected[:-1]}', 'r+', encoding='utf-8') as file_selected_read:
            lines_selected = file_selected_read.readlines()
        for line_select in lines_selected:
            print(line_select)
            text_write.insert(END, line_select)
    scrollbar_text_write = Scrollbar(frame_scroll_write)
    scrollbar_text_write.pack(fill=Y, ipady=165)
    scrollbar_text_write.config(command=text_write.yview)
    text_write.config(yscrollcommand=scrollbar_text_write.set)
    label_return = Label(window_write, text='Return', background='#262626',
    foreground='#ffffff')
    label_return.place(x=28, y=5)
    label_return.config(font=('sans', 8))
    def return_no_save():
        ask = askquestion(title='Warning',
        message='You no saved this file. If you not save the file the alterations make now not saved. If not writed anything press yes.', icon='warning')
        if ask == 'yes':
            frame_scroll_write.destroy()
            window_write.destroy()

    button_return = Button(window_write, image=image_write_note_return,
    background='#262626', activebackground='#262626', highlightthickness=0,
    bd=0, command=return_no_save)
    button_return.place(x=3, y=3)
    label_save = Label(window_write, text='Save', background='#262626',
    foreground='#ffffff')
    label_save.place(x=520, y=5)
    def save_note_writed():
        global file_selected

        if state_document:
            text_writed = text_write.get(1.0, END)
            with open(f'project01/files/{name_file}.txt', 'a+', encoding='utf-8') as write_note:
                write_note.write(text_writed)
        else:
            text_writed = text_write.get(1.0, END)
            print(str(file_selected))
            with open(f'{str(file_selected[:-1])}', 'w+', encoding='utf-8') as trunc:
                trunc.truncate()
            with open(f'{file_selected[:-1]}', 'a+', encoding='utf-8') as write_note_documente:
                write_note_documente.write(text_writed)
        frame_scroll_write.destroy()
        window_write.destroy()
    button_save = Button(window_write, image=image_save_note,
    background='#262626', activebackground='#262626',
    highlightthickness=0, bd=0, command=save_note_writed)
    button_save.place(x=550, y=3)

def create_new():
    window_create = Toplevel(root, background='#404040')
    window_create.geometry('280x90')
    window_create.title('Create')
    window_create.iconbitmap('project01/icons/plus.ico')
    window_create.resizable(0, 0)
    label_name = Label(window_create, text='Name:', background='#404040',
    foreground='#ffffff')
    label_name.place(x=3, y=19)
    label_name.config(font=('sans', 8))
    name = Entry(window_create, width=35, highlightthickness=0, bd=0)
    name.place(x=49, y=20)
    label_save = Label(window_create, text='Save', background='#404040',
    foreground='#ffffff')
    label_save.place(x=210, y=60)
    label_save.config(font=('sans', 8))
    def save_note():
        global state_document
        global name_file

        name_file = name.get()
        print(name_file)
        with open(f'project01/files/{name_file}.txt', 'w+', encoding='utf-8') as name_save:
            name_save.readline()
        with open(f'project01/files_created.txt', 'a+', encoding='utf-8') as files_created:
            files_created.write(f'project01/files/{name_file}.txt\n')
        list_files_added.append(f'project01/files/{name_file}.txt\n')
        list_files.insert(END, name_file)
        state_document = True
        window_create.destroy()
        write_note()
    button_save = Button(window_create, image=image_save, background='#404040',
    activebackground='#404040', highlightthickness=0, bd=0, command=save_note)
    button_save.place(x=240, y=60)

label_create = Label(frame_right, text='Create New', foreground='#cccccc',
background='#262626')
label_create.place(x=50, y=23)
label_create.config(font=('Mono', 8))
list_files = Listbox(root, height=20, width=49, background='#404040',
highlightthickness=0, bd=0, foreground='#cccccc')
frame_scroll = Frame(root, height=389, width=20)
frame_scroll.place(x=440, y=0)
scroll_list_files = Scrollbar(frame_scroll)
scroll_list_files.pack(fill=Y, ipady=165)
list_files.config(yscrollcommand=scroll_list_files.set)
scroll_list_files.config(command=list_files.yview)
list_files.place(x=0, y=0)
list_files.config(font=('sans', 12))
try:
    with open(f'project01/files_created.txt', 'r', encoding='utf-8') as files_created:
        lines_list = files_created.readlines()
    for line_added in lines_list:
        list_files_added.append(line_added)
    for i, files in enumerate(list_files_added):
        list_files.insert(i, basename(files[:-5]))
    print(list_files_added)
except:
    print('file dont exist')
image_create = PhotoImage(file=('project01/icons/create.png'))
button_create = Button(frame_right, image=image_create, background='#262626',
activebackground='#262626', highlightthickness=0, bd=0, command=create_new)
button_create.place(x=120, y=20)
image_save = PhotoImage(file=('project01/icons/save.png'))
image_save_note = PhotoImage(file=('project01/icons/save.png'))
image_write_note_return = PhotoImage(file='project01/icons/return.png')
label_edit_note = Label(frame_right, text='Edit/View', foreground='#cccccc',
background='#262626')
label_edit_note.place(x=62, y=59)
label_edit_note.config(font=('Mono', 8))
image_edit_note = PhotoImage(file=('project01/icons/edit.png'))
button_edit_note = Button(frame_right, image=image_edit_note, background='#262626',
activebackground='#262626', highlightthickness=0, bd=0,
command=write_note_activate)
button_edit_note.place(x=122, y=55)
label_delete_file = Label(frame_right, text='Delete', foreground='#cccccc',
background='#262626')
label_delete_file.place(x=77, y=99)
label_delete_file.config(font=('Mono', 8))
image_delete_file = PhotoImage(file=('project01/icons/delete.png'))
button_delete_file = Button(frame_right, image=image_delete_file, background='#262626',
activebackground='#262626', highlightthickness=0, bd=0, command=delete_note)
button_delete_file.place(x=120, y=95)
root.mainloop()
