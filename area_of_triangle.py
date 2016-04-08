import math
a = int(input('Введите длину первой стороны: '))
b = int(input('Введите длину второй стороны: '))
c = int(input('Введите длину третьей стороны: '))
p = (a+b+c)/2

print(math.sqrt(p*(p-a)*(p-b)*(p-c)))