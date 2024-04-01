number = int(input('Digite um número: '))

print(f'Analisando o número {number}')
unidade = number // 1 % 10
dezena = number // 10 % 10
centena = number // 100 % 10
milhar = number // 1000 % 10

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')