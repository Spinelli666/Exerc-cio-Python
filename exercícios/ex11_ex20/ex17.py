import math
'''from math import hypot'''

cat_op = float(input("Digite o valor do cateto oposto: "))
cat_adj = float(input("Digite o valor do cateto adjacente: "))

hip = math.hypot(cat_op, cat_adj)

print(f"A hipotenusa é: {hip:.2f}")