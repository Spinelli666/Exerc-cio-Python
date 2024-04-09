valor = float(input("Qual o valor da casa: R$"))
salario = float(input("Qual o salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento? "))

prest = valor / (anos * 12)

if prest > salario * 30 / 100:
    print(f"Para pagar uma casa de R${valor:.2f} em {anos} anos a prestação será de R${prest:.2f}")
    print("Empréstimo NEGADO!")
else:
    print(f"Para pagar uma casa de R${valor:.2f} em {anos} anos a prestação será de R${prest:.2f}")
    print("Empréstimo pode ser CONCEDIDO!")
