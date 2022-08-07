# importando as bibliotecas
from googletrans import Translator
from tkinter import *
from threading import Thread


#dicionário com as linguas
languages = {'af': 'afrikaans','sq': 'albanian','am': 'amharic','ar': 'arabic','hy': 'armenian',
'az': 'azerbaijani','eu': 'basque','be': 'belarusian','bn': 'bengali','bs': 'bosnian',
'bg': 'bulgarian','ca': 'catalan','ceb': 'cebuano','ny': 'chichewa','zh-cn': 'chinese (simplified)',
'zh-tw': 'chinese (traditional)','co': 'corsican','hr': 'croatian','cs': 'czech','da': 'danish',
'nl': 'dutch','en': 'english','eo': 'esperanto','et': 'estonian','tl': 'filipino',
'fi': 'finnish','fr': 'french','fy': 'frisian','gl': 'galician','ka': 'georgian',
'de': 'german','el': 'greek','gu': 'gujarati','ht': 'haitian creole','ha': 'hausa',
'haw': 'hawaiian','iw': 'hebrew','he': 'hebrew','hi': 'hindi','hmn': 'hmong','hu': 'hungarian',
'is': 'icelandic','ig': 'igbo','id': 'indonesian','ga': 'irish','it': 'italian','ja': 'japanese',
'jw': 'javanese','kn': 'kannada','kk': 'kazakh','km': 'khmer','ko': 'korean','ku': 'kurdish (kurmanji)',
'ky': 'kyrgyz','lo': 'lao','la': 'latin','lv': 'latvian','lt': 'lithuanian','lb': 'luxembourgish',
'mk': 'macedonian','mg': 'malagasy','ms': 'malay','ml': 'malayalam','mt': 'maltese',
'mi': 'maori','mr': 'marathi','mn': 'mongolian','my': 'myanmar (burmese)','ne': 'nepali','no': 'norwegian',
'or': 'odia','ps': 'pashto','fa': 'persian','pl': 'polish','pt': 'portuguese','pa': 'punjabi',
'ro': 'romanian','ru': 'russian','sm': 'samoan','gd': 'scots gaelic','sr': 'serbian','st': 'sesotho',
'sn': 'shona','sd': 'sindhi','si': 'sinhala','sk': 'slovak','sl': 'slovenian','so': 'somali','es': 'spanish',
'su': 'sundanese','sw': 'swahili','sv': 'swedish','tg': 'tajik','ta': 'tamil','te': 'telugu',
'th': 'thai','tr': 'turkish','uk': 'ukrainian','ur': 'urdu','ug': 'uyghur','uz': 'uzbek',
'vi': 'vietnamese','cy': 'welsh','xh': 'xhosa','yi': 'yiddish','yo': 'yoruba','zu': 'zulu'}
dest_lagn = ''
origin_lagn = ''


# função de traduzir o texto do widget Text()
def Translate():
    en_translated.delete(1.0, END)
    text = user_input.get(1.0, END)
    if bool(dest_lagn) == True and bool(origin_lagn) == True:
        traduction = Translator().translate(str(text), dest=dest_lagn, src=origin_lagn)
    elif bool(dest_lagn) == True:
        traduction = Translator().translate(str(text), dest=dest_lagn)
    elif bool(origin_lagn) == True:
        traduction = Translator().translate(str(text), dest='en', src=origin_lagn)
    else:
        traduction = Translator().translate(str(text), dest='en')
    en_translated.insert(END, traduction.text)


# função de iniciar a função de traduzir sem dar travadinhas
def Start_Translate():
    Thread(target=Translate).start()


# pegar linguagem de destino
def dest_language(value):
    global dest_lagn
    dest_lagn = value


# pegar linguagem de origem
def origin_language(value):
    global origin_lagn
    origin_lagn = value


# tela raiz, widgets e configurações
root = Tk()
root.title('tradutor')
root.resizable(0, 0)
root.geometry('600x300')
root.config(background='#4d4d4d')
user_input = Text(root, highlightthickness=0, borderwidth=1,
                  background='#8c8c8c')
en_translated = Text(root, highlightthickness=0, borderwidth=1,
                     background='#8c8c8c')
convers_lbl = Label(root, text='------------>', background='#4d4d4d')
value_default_dest = StringVar(root)
value_default_dest.set('select')
value_default_origin = StringVar(root)
value_default_origin.set('select')
menuoption_dest = OptionMenu(
    root, value_default_dest, *languages.values(), command=dest_language)
menuoption_origin = OptionMenu(
    root, value_default_origin, *languages.values(), command=origin_language)
translate_btn = Button(root, text='translate', background='#595959', borderwidth=1,
                       activebackground='#404040', command=Start_Translate)
convers_lbl.place(x=265, y=130)
convers_lbl.config(font=53)
user_input.place(x=13, y=13, height=270, width=150)
user_input.config(font=23)
en_translated.place(x=440, y=13, height=270, width=150)
en_translated.config(font=33)
translate_btn.place(x=265, y=200, width=83, height=43)
translate_btn.config(font=23)
menuoption_dest.place(x=345, y=130, width=90, height=30)
menuoption_dest.config(background='#595959', activebackground='#404040',
                        highlightthickness=0, borderwidth=1)
menuoption_origin.place(x=170, y=130, width=90, height=30)
menuoption_origin.config(background='#595959', activebackground='#404040', 
                        highlightthickness=0, borderwidth=1)
root.mainloop()
