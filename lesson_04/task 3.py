import random
n = random.randint(1, 5)
answer = int(input('введите число: '))
while answer != n:
    print('попробуйте еще раз.')
    answer = int(input('введите число: '))
print('вы угадали!')
