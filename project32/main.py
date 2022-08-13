def dupletter(string):
    string = string.replace(" ", "")
    n_dupletter = 0
    for i, l in enumerate(string):
        for i_check, l_check in enumerate(string):
            if i_check >= i:
                if l_check == l:
                    n_dupletter += 1
                if n_dupletter == 2:
                    return True
        if n_dupletter < 2:
            n_dupletter = 0
    return False

dppltt = dupletter("Hello, World!")
print(dppltt)
