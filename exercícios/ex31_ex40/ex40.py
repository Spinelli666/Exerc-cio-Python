nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if 7 > media >= 5:
    print(f'Com média {media:.1f}: Reprovado')
elif media < 5:
    print(f'Com média {media:.1f}: Recuperação')
elif media >= 7:
    print(f'Com média {media:.1f}: Aprovado')