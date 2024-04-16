from time import sleep

num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))
opcao = 0

print("=-=" * 10)
while opcao != 5 :
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa ''')
    opcao = int(input("Qual é a sua opção? "))

    if opcao == 1:
        print(f"A soma entre {num1} e {num2} é {num1 + num2}")
    elif opcao == 2:
        print(f"O produto entre {num1} e {num2} é {num1 * num2}")
    elif opcao == 3:
        if num1 > num2:
            print(f"O número {num1} é maior que o número {num2}")
        elif num2 > num1:
            print(f"O número {num2} é maior que o número {num1}")
        else:
            print("Os números são iguais")
    elif opcao == 4:
        num1 = int(input("Primeiro valor: "))
        num2 = int(input("Segundo valor: "))
    else:
        print("Opção inválida. Tente novamente.")
    print("=-=" * 10)
print("Finalizando...")
sleep(2)
print("Fim do programa. Volte sempre!")