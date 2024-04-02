alugado = int(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))

preco = (alugado * 60) + (km * 0.15)

print(f"O total a pagar é de R${preco:.2f}.")