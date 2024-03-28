import math
'''from math import radians, sin, cos, tan'''

angulo = float(input("Digite o ângulo que você deseja: "))

seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print(f"O ângulo de {angulo} tem o SENO de {seno:.2f}")
print(f"O ângulo de {angulo} tem o COSSENO de {cos:.2f}")
print(f"O ângulo de {angulo} tem a TANGENTE de {tan:.2f}")