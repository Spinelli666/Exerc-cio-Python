maior = 0
menor = 0

for i in range (1, 6):
    peso = float(input(f"Digite o peso da {i}ª pessoa: "))
    if i == 1:
        maior = i
        menor = i
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso lido foi de {maior}Kg")
print(f"O menor peso lido foi de {menor}Kg")
