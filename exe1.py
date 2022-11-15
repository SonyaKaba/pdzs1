# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, 
# является ли этот день выходным


print('enter day number: ')
a = input()
if int(a) < 6:
    print('Go to work, mr. Meeseeks!')
if int(a) >= 6 < 8:
    print('mr. Meeseeks doesnt work')
if int(a) >= 8:
    print('Nice joke, mr. Meeseeks')

