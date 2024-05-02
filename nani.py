from random import randint

num = randint(1,2)


while True:
    print('Угадай число от 1 до 2')
    guess = int(input('Введите число: '))
    
    if guess == num:
        print('Молодец, возьми с полки пирожок')
        break
    else:
        print('Неверно, пробуй ещё')