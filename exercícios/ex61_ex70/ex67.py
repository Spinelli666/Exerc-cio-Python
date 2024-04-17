number = 0

while True:
    number = int(input("Digite um número: "))
    if number < 0:
        break
    print(f"-" * 10)
    for c in range(1, 11):
        print(f"{number} x {c} = {number * c}")
    print(f"-" * 10)

print(f"Programa encerrado!")