velocidade = float(input('Qual a velocidade do carro? '))

if velocidade > 80:
    print(f'Você foi multado! O valor da multa é R${(velocidade - 80) * 7:.2f}.')
else:
    print('Você está dentro do limite de velocidade.')
