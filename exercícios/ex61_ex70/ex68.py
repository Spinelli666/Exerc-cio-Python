from random import randint

print("-=-" * 10)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("-=-" * 10)

vitorias = 0

while True:
    
    tipo = str(input("Par ou ímpar? [P/I] ")).strip().upper()[0]
    while tipo not in "PpIi":
        print("Opção inválida! Digite P para par ou I para ímpar.")
        tipo = str(input("Par ou ímpar? [P/I] ")).strip().upper()[0]
    jogador = int(input("Digite um valor: "))
    computador = randint(0, 10)
    total = jogador + computador
    print("-" * 20)
    print(f"Você jogou {jogador} e o computador {computador}. Total é: {total}.", end=" ")
    print("Deu par!" if total % 2 == 0 else "Deu ímpar!")
    print("-" * 20)
    if tipo == "P":
        if total % 2 == 0:
            print("Você venceu!")
            vitorias += 1
        else:
            print("Você perdeu!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Você venceu!")
            vitorias += 1
        else:
            print("Você perdeu!")
            break
    print("Vamos jogar novamente...")
print(f"GAME OVER! Você venceu {vitorias} vezes.")