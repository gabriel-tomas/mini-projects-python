import mysql.connector


def ConnectDatabase(host="localhost", user="root", password="94945049Abcd", database="logins"):
    connection = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = connection.cursor()
    return connection, cursor

def DisconnectDatabase(connection, cursor):
    connection.close()
    cursor.close()

connection, cursor = ConnectDatabase()

def CreateAccount(name, password):
    try:
        comando = f"insert into pessoas values (default, '{name}', '{password}', default);"
        cursor.execute(comando)
        connection.commit()
    except Exception as error:
        raise error

def Get_Account(name, password):
    comando = "select * from pessoas;"
    cursor.execute(comando)
    rows = cursor.fetchall()
    for row in rows:
        if name in row and password in row:
            return row

def CreateText(name, password, text):
    id = Get_Account(name, password)[0]
    comando = f"update pessoas set texto = '{text}' where id = '{id}';"
    cursor.execute(comando)
    connection.commit()
    
    