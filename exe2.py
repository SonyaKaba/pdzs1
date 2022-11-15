#Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.



print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
x = int(input('x= '))
y = int(input('y= '))
z = int(input('z= '))
print('¬(x ⋁ y ⋁ z) = ¬x ⋀ ¬y ⋀ ¬z')

def perdicat():
    left = not(x or y or z)
    right = not x and not y and not z
    result = left == right
    if result == True:
        print('true')
    else: 
        print('false')

perdicat()
