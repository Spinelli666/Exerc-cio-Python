frase = str(input("Digite seu nome completo: "))

print(f"Seu nome em maiúsculas é: {frase.upper()}")
print(f"Seu nome em minúsculas é: {frase.lower()}")
print(f"Seu nome tem ao todo {len(frase) - frase.count(' ')} letras")
print(f"Seu primeiro nome tem {frase.find(' ')} letras")