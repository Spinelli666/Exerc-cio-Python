total = totalmil = menor = cont = 0
barato = " "
while True:
    produto = str(input("Nome do Produto: ")).strip().upper()
    preco = float(input("Preço: R$"))
    cont += 1
    total += preco
    if preco > 1000:
        totalmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print("{:-^40}".formart("   FIM DO PROGRAMA   "))
print(f"O total da compra foi R${total:10.2f}")
print(f"Temos {totalmil} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {barato} que custa R${menor:.2f}")