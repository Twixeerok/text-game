
import time
import random
import sqlite3
from hero import vor as v
from hero import var as q

con = sqlite3.connect('data.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS game(login TEXT, coin BIGINT, hp BIGINT, mp BIGINT, lvl INT, exp BIGINT, class TEXT)')
con.commit()

def reg():
    print('для начала игры нужно пройти регистрацию')
    User_login = input('login: ')

    cur.execute(f"SELECT login FROM game WHERE login = '{User_login}'")
    if cur.fetchone() is None:
        choose = input(f'Добро пожаловать {User_login}, выберете класс: охотник, вор ')  
        cur.execute(f"INSERT INTO game VALUES (?, ?, ?, ?, ?, ?, ?)",(User_login, 0, 0, 0, 0, 0, choose))
        con.commit()
        print('Пользователь зарегестрирован')
        if choose == "вор":
            print('вы выбрали класс вор') 
            v.vor.vor1()
        if choose == "охотник":
            print('вы выбрали класс охотник') 
            q.var.var1()
        else:
            print('такая запись уже имеется!')
            for value in cur.execute("SELECT * FROM game"):
                print (value)
        
class game():        
    def game():
        global User_login
        User_login = input('log in: ')
        cur.execute(f'SELECT login FROM game WHERE login = "{User_login}"')
        if cur.fetchone() is None:
            print('такого логина не существует')
            reg()
        else:
            hero_check()
        

def hero_check():
    for value in cur.execute(f'SELECT class FROM game WHERE login = "{User_login}"'):
        if value[0] == 'вор':
            v.vor.lvl_check()
        if value[0] == 'охотник':
            q.var.lvl_check()
        else:
            print('ошибка')

def heal():
    print('аптечка на 20 хп стоит 5 монет, на 50 хп 10 монет')
    a = input('1 или 2 ')
    if a == '1':
        cur.execute(f'UPDATE game SET coin = coin -5, hp = hp +20 WHERE login = "{User_login}"')
        con.commit()
        print('вы восстановили 20 хп')
        return v.vor.vor2()
    if a == '2':
        cur.execute(f'UPDATE game SET coin = coin -10, hp = hp +50 WHERE login = "{User_login}"')
        con.commit()
        print('вы восстановили 50 хп')
        return v.vor.vor2()



def exit():
    print("Выход из игры")



             





    
