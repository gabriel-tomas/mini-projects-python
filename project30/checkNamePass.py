def Check(account):
    if len(account.strip()) == 0:
        return False
    else:
        return True

def Info(check_name, check_password):
    if not check_name and not check_password:
        return "Digite o nome e a senha"
    elif not check_password:
        return "Digite a senha"
    elif not check_name:
        return "Digite o nome"
    else:
        return None

def Check_Account_asw(asw):
    if asw == False:
        return "Conta criada", "green"
    elif asw == True:
        return "Conta já existe", "#db923d"