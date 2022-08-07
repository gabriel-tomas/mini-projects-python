from os import system as cmd

dic = {"abrir":"cd", "área de trabalho":"C://Users//Desktop"}
text = str(input("Digite o texto: "))

def Cmd(line):
    cmd(line)
    

def User():
    user = str(input("Digite seu nome de usuário: ")).capitalize()
    return user
    
def treat(text):
    line = ""
    for keys in dic.keys():
        if keys == "área de trabalho":
            user = User()
            dic[keys] = dic[keys][:dic[keys].rfind("//") + 1] + user + dic[keys][dic[keys].rfind("//") + 1:]
        if keys in text:
            line += dic[keys] + " "
    line = line.strip()
    print(line)
    return line

line = treat(text)
cmd(line)
