preco = float(input("Preço da compra: R$"))

print(f"Formas de pagamento:")
print(f"[1] À vista dinheiro/cheque: 10% de desconto")
print(f"[2] À vista no cartão: 5% de desconto")
print(f"[3] 2x no cartão: preço formal")
print(f"[4] 3x ou mais no cartão: 20% de juros")

opcao = int(input("Qual é a opção? "))

if opcao == 1:
    total = preco - (preco * 10 / 100)
    print(f"Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.")
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print(f"Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.")
elif opcao == 3:
    total = preco
    parcela = preco / 2
    print(f"Sua compra será parcelada em 2x de R${parcela:.2f} sem juros")
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    parcelas = int(input("Quantas parcelas? "))
    parcela = total / parcelas
    print(f"Sua compra será parcelada em {parcelas}x de R${parcela:.2f} com juros")
else:
    total = preco
    print("Opção inválida de pagamento. Tente novamente!")