ano_nasc = int(input('Digite o ano de nascimento: '))

idade = 2024 - ano_nasc

print(f'Quem nasceu em {ano_nasc} tem {idade} anos em 2024.')

if idade < 18:
    print(f'Com {idade} anos: Ainda vai se alistar ao serviço militar.\nFaltam {18 - idade} anos para o alistamento.\nSeu alistamento será em {ano_nasc + 18}.')
elif idade == 18:
    print(f'Com {idade} anos: Está na hora de se alistar ao serviço militar.\nCompareça à junta militar mais próxima de você')
else:
    print(f'Com {idade} anos: Já passou do tempo de se alistar ao serviço militar.\nVocê deveria ter se alistado em {ano_nasc + 18}.')
