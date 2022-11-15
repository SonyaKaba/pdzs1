# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).


print('enter quarter:')
a = int(input('a = '))
if a == 1: 
     print("x=[0;+inf], y=[0;+inf]") 
elif a == 2:
    print("x=[0;-inf],y=[0;+inf]")
elif a == 3:
    print("x=[0;-inf];y=[0;-inf]")
elif a == 4:
    print("x=[0;+inf],y=[0;-inf]")
elif a > 5:
    print('error')