print("Gerador de PA")
print("-=" * 10)

termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
c = 1

while c <= 10:
    print(f"{termo}", end=" -> ")
    termo += razao
    c += 1
print("ACABOU!")