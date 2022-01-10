import stud
import time

class vor():              
    def vor1():
        stud.cur.execute(f'UPDATE game SET coin = {100}, hp = {200}, mp = {50}, lvl = {1}, exp = {0} WHERE login = "{stud.User_login}"')
        stud.con.commit()
        vor.vor2()
    def lvl_check():
        for i in stud.cur.execute('SELECT exp FROM game'):
            print(f'у вас {i} опыта для 2 уровня надо 50')
            if i[0] > 50:
                print('Поздравляем вы получили 2 уровень')
            if i[0] < 50:
                vor.vor2()
    def vor2():
        try:
            deistvie = input('выберете действие:\nохота\nкража\nаптечка\nстатистика персонажа - "инф"\n')
            if deistvie == "охота":
                hunt()
            if deistvie == "инф":
                cheack()
            if deistvie == "кража":
                lif()
            if deistvie == "аптечка":
                stud.heal()
            if deistvie == "выход":
                exit()
        except AttributeError:   
            return vor.vor2()
        else:
            print('ошибка ввода')
            return vor.vor2()
    def vor3():
        try:
            deistvie = input('выберете действие:\nохота\nкража\nаптечка\nстатистика персонажа - "инф"\n')
            if deistvie == "охота":
                hunt2()
            if deistvie == "инф":
                cheack()
            if deistvie == "кража":
                lif2()
            if deistvie == "аптечка":
                stud.heal()
            if deistvie == "выход":
                exit()
        except AttributeError:   
            return vor.vor2()
        else:
            print('ошибка ввода')
            return vor.vor2()
def lif():
    a = stud.random.randint(1,3)
    if a == 1:
        print('Идет кража подождите 2 секунды')
        time.sleep(2)
        stud.cur.execute(f'UPDATE game SET coin = coin +20, exp = exp +10 WHERE login = "{stud.User_login}"')
        stud.con.commit()
        print('Поздравляем Охота прошла успешно')
        print("вы получили 10 монет")
        return stud.vor.lvl_check()
    if a == (2):
        print('Идет охота подождите 3 секунды')
        time.sleep(3)
        stud.cur.execute(f'UPDATE game SET hp = hp -10, exp = exp +5 WHERE login = "{stud.User_login}"')
        stud.con.commit()
        print('Охота провалена')
        print(f'вы потеряли 10 Hp')
        return stud.vor.lvl_check()
    if a == (3):
        print('Идет кража подождите 2 секунды')
        time.sleep(2)
        stud.cur.execute(f'UPDATE game SET coin = coin +20, exp = exp +10 WHERE login = "{stud.User_login}"')
        stud.con.commit()
        print('Поздравляем Охота прошла успешно')
        print("вы получили 10 монет")
        return stud.vor.lvl_check()

    

def hunt():
    a = stud.random.randint(1,3)
    if a == 1:
        print('Идет охота подождите 3 секунды')
        time.sleep(3)
        stud.cur.execute(f'UPDATE game SET coin = coin +10, exp = exp +1 WHERE login = "{stud.User_login}"')
        stud.con.commit()
        print('Поздравляем Охота прошла успешно')
        print("вы получили 10 монет")
        return stud.vor.lvl_check()
    if a == (2):
        print('Идет охота подождите 3 секунды')
        time.sleep(3)
        stud.cur.execute(f'UPDATE game SET hp = hp -10, exp = exp +1 WHERE login = "{stud.User_login}"')
        stud.con.commit()
        print('Охота провалена')
        print(f'вы потеряли 10 Hp')
        return stud.vor.lvl_check()
    if a == (3):
        print('Идет охота подождите 3 секунды')
        time.sleep(3)
        stud.cur.execute(f'UPDATE game SET hp = hp -10, exp = exp +1 WHERE login = "{stud.User_login}"')
        stud.con.commit()
        print('Охота провалена')
        print(f'вы потеряли 10 Hp')
        return stud.vor.lvl_check()
def lif2():
    a = stud.random.randint(1,3)
    if a == 1:
        print('Идет кража подождите 2 секунды')
        time.sleep(2)
        stud.cur.execute(f'UPDATE game SET coin = coin +50, exp = exp +40 WHERE login = "{stud.User_login}"')
        stud.con.commit()
        print('Поздравляем Охота прошла успешно')
        print("вы получили 50 монет")
        return stud.vor.lvl_check()
    if a == (2):
        print('Идет охота подождите 3 секунды')
        time.sleep(3)
        stud.cur.execute(f'UPDATE game SET hp = hp -40, exp = exp +20 WHERE login = "{stud.User_login}"')
        stud.con.commit()
        print('Охота провалена')
        print(f'вы потеряли 40 Hp')
        return stud.vor.lvl_check()
    if a == (3):
        print('Идет кража подождите 2 секунды')
        time.sleep(2)
        stud.cur.execute(f'UPDATE game SET coin = coin +20, exp = exp +10 WHERE login = "{stud.User_login}"')
        stud.con.commit()
        print('Поздравляем Охота прошла успешно')
        print("вы получили 10 монет")
        return stud.vor.lvl_check()
def hunt2():
    a = stud.random.randint(1,3)
    if a == 1:
        print('Идет охота подождите 3 секунды')
        time.sleep(3)
        stud.cur.execute(f'UPDATE game SET coin = coin +30, exp = exp +80 WHERE login = "{stud.User_login}"')
        stud.con.commit()
        print('Поздравляем Охота прошла успешно')
        print("вы получили 10 монет")
        return stud.vor.lvl_check()
    if a == (2):
        print('Идет охота подождите 3 секунды')
        time.sleep(3)
        stud.cur.execute(f'UPDATE game SET hp = hp -60, exp = exp +50 WHERE login = "{stud.User_login}"')
        stud.con.commit()
        print('Охота провалена')
        print(f'вы потеряли 10 Hp')
        return stud.vor.lvl_check()
    if a == (3):
        print('Идет охота подождите 3 секунды')
        time.sleep(3)
        stud.cur.execute(f'UPDATE game SET hp = hp -60, exp = exp +80 WHERE login = "{stud.User_login}"')
        stud.con.commit()
        print('Охота провалена')
        print(f'вы потеряли 10 Hp')
        return stud.vor.lvl_check()
    
def cheack():
    for i in stud.cur.execute('SELECT * FROM game'):
        print (f'Пользователь {i[0]} имеет {i[1]} монет, {i[2]} Здоровья, {i[3]} маны, уровень {i[4]}, опыта {i[5]}')
        return vor.vor2()