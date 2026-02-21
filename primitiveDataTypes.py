valor = input("Digite algo: ")

print("É alfanumérico?", valor.isalnum())
print("É somente letras?", valor.isalpha())
print("É somente números?", valor.isnumeric())
print("É somente letras MAIÚSCULAS?", valor.isupper())
print("É somente letras minúsculas?", valor.islower())
print("Contém apenas espaços?", valor.isspace())
print("Está capitalizado (Ex: Python)?", valor.istitle())
