a = input("Digite qualquer coisa: ")

print(f"O tipo primitivo desse valor é {type(a)}")
print(f"Só tem espaços? {a.isspace()}")     # A função isspace() retorna True se todos os caracteres da string são espaços
print(f"É um número? {a.isnumeric()}")      # A função isnumeric() retorna True se todos os caracteres da string são numéricos
print(f"É alfabético? {a.isalpha()}")       # A função isalpha() retorna True se todos os caracteres da string são alfabéticos
print(f"É alfanumérico? {a.isalnum()}")     # A função isalnum() retorna True se todos os caracteres da string são alfanuméricos
print(f"Está em maiúsculas? {a.isupper()}") # A função isupper() retorna True se todos os caracteres da string são maiúsculos
print(f"Está em minúsculas? {a.islower()}") # A função islower() retorna True se todos os caracteres da string são minúsculos
print(f"Está capitalizada? {a.istitle()}")  # Capitalizada é quando a primeira letra é maiúscula e as outras são minúsculas