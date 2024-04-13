print("=" * 20)
print("10 TERMOS DE UMA PA")
print("=" * 20)

termo = int(input("Digite o primeiro termo da PA: ")) 
razao = int(input("Digite a razão da PA: "))
decimo = termo + (10 - 1) * razao	# Fórmula do enésimo termo de uma PA

for i in range(termo, decimo + razao, razao):
    print(f"{i}", end=" -> ")
print("ACABOU!")