import time
import random
import string


# Вычисление процента в функции процента правильности введенных данных
def deistvie(new_strokk, strokk):
    cnt, cnt_strokk = len(strokk), 0
    for i in range(len(new_strokk)):
        if new_strokk[i] == strokk[i]:
            cnt_strokk += 1
    return round((cnt_strokk / cnt) * 100, 3)


# Функция подсчета процента правильности введенных данных

def functions_accuracy(new_strok, strok):
    if len(new_strok) < len(strok):
        return deistvie(new_strok, strok)
    elif len(new_strok) == len(strok):
        return deistvie(new_strok, strok)
    elif len(new_strok) > len(strok):
        #         new_strok = new_strok[:(len(strok) - len(new_strok))]
        lok_strok = strok
        strok = new_strok
        new_strok = lok_strok
        return deistvie(new_strok, strok)


# Функция выбора уровня сложности для генерации строки ( структурированного предложения ) из файла
def functions_2(lvl):
    if lvl == 1:
        f = open('stroki_lvl_1.txt',encoding="utf8").read()
    elif lvl == 2:
        f = open('stroki_lvl_2.txt',encoding="utf8").read()
    elif lvl == 3:
        f = open('stroki_lvl_3.txt',encoding="utf8").read()
    massiv_strok = f.split('\n')
    sentence = random.choice(massiv_strok)
    return sentence


# Функция генерации рандомной строки уровня
def functions_1_(lenn, lvl):
    if lvl == 1:
        letters = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnmЙйЦцУуКкЕеНнГгШшЩщЗзХхЪъФфЫыВвАаПпРрОоЛлДдЖжЭэЯяЧчСсМмИиТтЬьБбЮю '
        rand_string = ''.join(random.choice(letters) for i in range(lenn))
    elif lvl == 2:
        letters = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890ЙйЦцУуКкЕеНнГгШшЩщЗзХхЪъФфЫыВвАаПпРрОоЛлДдЖжЭэЯяЧчСсМмИиТтЬьБбЮю '
        rand_string = ''.join(random.choice(letters) for i in range(lenn))
    elif lvl == 3:
        letters = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnmЙйЦцУуКкЕеНнГгШшЩщЗзХхЪъФфЫыВвАаПпРрОоЛлДдЖжЭэЯяЧчСсМмИиТтЬьБбЮю1234567890!@"#№$;%^:&?*(){}[]\|<>«» '
        rand_string = ''.join(random.choice(letters) for i in range(lenn))
    return rand_string


# Функция выбора уровня сложности генерации рандомной строки
def functions_1(lvl):
    if lvl == 1: return functions_1_(random.randint(19, 20), 1)
    if lvl == 2: return functions_1_(random.randint(29, 30), 2)
    if lvl == 3: return functions_1_(random.randint(39, 50), 3)


# Обьявление переменных основной части кода ( main )

ok = True
mass_1 = ["Начало", "НАЧАЛО", "начало", "Yfxfkj", "yfxfkj", "YFXFKJ"]
mass_2 = ["Выйти", "ВЫЙТИ", "выйти", "Dsqnb", "dsqnb", "DSQNB"]

# Сердце программы
print("Игра'Клавиатурный тренажер'")
print("")
while ok:
    ok_vvod = True
    while ok_vvod:
        print("Введите 'Начало', чтобы начать игру, или 'Выйти', чтобы выйти из игры")
        vvod_1 = str(input("Ввод : "))
        if vvod_1 in mass_1 or vvod_1 in mass_2: ok_vvod = False
    ok_1 = True
    if vvod_1 in mass_1:
        while ok_1 == True:
            ok_vvod_2 = True
            while ok_vvod_2:
                print("Введите 1, чтобы выбрать уровень сложности 'Лёгкий'")
                print("Введите 2, чтобы выбрать уровень сложности 'Средний'")
                print("Введите 3, чтобы выбрать уровень сложности 'Сложный'")
                try:
                    vvod_lvl = int(input("Ввод: "))
                    if vvod_lvl == 1 or vvod_lvl == 2 or vvod_lvl == 3: ok_vvod_2 = False
                except:
                    continue
            ok_vvod_3 = True
            while ok_vvod_3:
                print("Выберите, с какими данными вы будете работать")
                print("Введите 1, чтобы генерировалась рандомная строка")
                print("введите 2,чтобы генерировалось структурированное предложение ( строка )")
                try:
                    vvod_vvod = int(input("Ввод: "))
                    if vvod_vvod == 1 or vvod_vvod == 2: ok_vvod_3 = False
                except:
                    continue

            if vvod_vvod == 1:
                stroka = functions_1(vvod_lvl)

            elif vvod_vvod == 2:
                stroka = functions_2(vvod_lvl)

            print("")
            time.sleep(1.5)
            print("3 секунды до появления строки...")
            time.sleep(1.0)
            print("2 секунды до появления строки...")
            time.sleep(1.0)
            print("1 секунда до появления строки...")
            time.sleep(1.0)
            print("...")
            time.sleep(1.0)

            print("Строка -->", stroka)
            start_time = time.time()
            new_stroka = str(input("Ввод --> "))
            finish_time = time.time()
            new_stroka_time = round(finish_time - start_time, 3)
            accuracy = functions_accuracy(new_stroka, stroka)
            print("Процент правильности введенного текста =", accuracy, "%")
            print("Время ввода строки =", new_stroka_time, "секунд")

            print("")
            ok_vvod_4 = True
            while ok_vvod_4:
                print("Нажмите 1,чтобы выйти в главное меню")
                print("Нажмите 2,чтобы продолжить играть")
                try:
                    last_vvod = int(input("Ввод: "))
                    if last_vvod == 1 or last_vvod == 2: ok_vvod_4 = False
                except:
                    continue
            if last_vvod == 2:
                ok_vvod_2 = False
                ok_vvod_3 = False
            elif last_vvod == 1:
                ok_vvod = False
                break
    elif vvod_1 in mass_2:
        break