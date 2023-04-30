import random

digits = '0123456789'
lletters = 'abcdefghijklmnopqrstuvwxyz'
uletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
spec = '!#$%&*+-=?@^'
chars = ''

def words_to_number(word):
    zapros = word.lower().split()
    word = word.lower()
    d = {'один' : 1, 'два' : 2, 'три' : 3, 'четыре' : 4, 'пять' : 5, 'шесть' : 6, \
        'семь' : 7, 'восемь' : 8, 'девять' : 9, 'десять' : 10, 'одиннадцать' : 11, \
        'двенадцать' : 12, 'тринадцать' : 13, 'четырнадцать' : 14, 'пятнадцать' : 15, \
        'шестнадцать' : 16, 'семнадцать' : 17, 'восемнадцать' : 18,  'девятнадцать' : 19}
    d2 = {'двадцать' : 20, 'тридцать' : 30, 'сорок' : 40, 'пятьдесят' : 50, \
          'шестьдесят' : 60, 'семьдесят' : 70, 'восемьдесят' : 80,  'девяносто' : 90}

    if 100 > len(zapros) > 1 :
        if zapros[1] == 'длина':
            if zapros[0] in d:
                return d[zapros[0]]
            else:
                print('\n' + 'Некорректная длина пароля!')
                return step_two()
        else:
            return d2[zapros[0]] + d[zapros[1]] 
    elif len(zapros) == 1:
        if word in d2:
            return d2[word]
        elif word in d:
            return d[word]
        else:
            print('\n' + 'Некорректное число паролей!')
            return step_one()
    else:
        print('\n' + 'Некорректное число паролей!')
        return step_one()

def step_one():  
    print('\n' + 'Какое количество паролей сгенерировать? (99 максимум)')
    global count_password
    count_password = input('Количество паролей: ').strip()
    if count_password.isdigit() == False:
        count_password = words_to_number(count_password)
        return step_two()
    else:
        count_password = int(count_password)
        if 0 > count_password or count_password > 99:
            print('\n' + 'Некорректное число паролей!')
            return step_one()
        else:
            return step_two()

def step_two(): 
    print('\n' + 'Какой длины должен быть пароль? (19 максимум)')
    global len_password
    len_password = input('Количество символов: ').strip()
    if len_password.isdigit() == False:
        len_password = words_to_number(len_password + ' длина')
    else:
        len_password = int(len_password)
        if 0 > len_password or len_password > 19:
            print('\n' + 'Некорректная длина пароля!')
            return step_two()
        
        
step_one()


print('\n' + 'Включить цифры? Да/Нет')
digits_password = input('Да/Нет: ').strip()
if digits_password.lower() == 'да':
    chars += digits

print('\n' + 'Включить прописные буквы? Да/Нет')
lletters_password = input('Да/Нет: ').strip()
if lletters_password.lower() == 'да':
    chars += lletters

print('\n' + 'Включить заглавные буквы? Да/Нет')
uletters_password = input('Да/Нет: ').strip()
if uletters_password.lower() == 'да':
    chars += uletters

print('\n' + 'Включить символы? Да/Нет')
spec_password = input('Да/Нет: ').strip()
if spec_password.lower() == 'да':
        chars += spec

print('\n' + 'Исключить неоднозначные символы? (il1Lo0O) Да/Нет')
sletter_password = input('Да/Нет: ').strip()
if sletter_password.lower() == 'да':
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')

def generate_password(char, length):
    return random.sample(char, length)

for _ in range(count_password):
    print('\n' + 'Сгенерированный пароль:', end='')
    print(*generate_password(chars, len_password), sep='')


    # был какой-то баг с большими числами...