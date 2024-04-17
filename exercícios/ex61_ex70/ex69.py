print("-=-" * 10)
print("     CADASTRE UMA PESSOA      ")
print("-=-" * 10)

maior_idade = 0
homens = 0
mulheres_menor_idade = 0

while True:
    print("-" * 20)
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    while sexo not in "MmFf":
        print("Opção inválida! Digite M para masculino ou F para feminino.")
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    if idade > 18:
        maior_idade += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheres_menor_idade += 1
    print("-" * 20)
    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    while continuar not in "SsNn":
        print("Opção inválida! Digite S para sim ou N para não.")
        continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {maior_idade}")
print(f"Ao todo temos {homens} homens cadastrados.")
print(f"E temos {mulheres_menor_idade} mulheres com menos de 20 anos.")
