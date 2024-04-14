somaidade = 0
mediaidade = 0
maioridadeH = 0
nomevelho = ""
totmulher = 0

for i in range(1, 5):
    print(f"----- {i}ª PESSOA -----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    if i == 1 and sexo in 'Mm':
        maioridadeH = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadeH:
        maioridadeH = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher += 1

mediaidade = somaidade / 4
print(f"A média de idade do grupo é de {mediaidade} anos.")
print(f"O homem mais velho tem {maioridadeH} anos e se chama {nomevelho}.")
print(f"Ao todo são {totmulher} mulheres com menos de 20 anos.")