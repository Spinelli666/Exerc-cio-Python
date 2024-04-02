largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

area = largura * altura
tinta = area / 2

print(f"A parede tem dimensões de {largura:.2f}m x {altura:.2f}m, totalizando uma área de {area:.2f}m².")
print(f"Para pintar uma parede de {area:.2f}m², você precisará de {tinta:.2f}L de tinta.")