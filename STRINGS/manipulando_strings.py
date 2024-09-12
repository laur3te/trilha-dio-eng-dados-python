curso = "pYtHOn"

print(curso.upper()) #Letra maiscula

print(curso.lower()) #Letra minúscula

print(curso.title()) #O primeiro caracter fica maisculo

print(curso.strip()) #Remove espaços brancos 

print(curso.lstrip()) #Remove os espaços brancos da esquerda

print(curso.rstrip()) #Remove os espaços brancos da direita

print("index: ", curso.find("t")) #Retorna a posição da primeira ocorrência

print(curso.center(10, " ")) #Números de caracteres que vai ocupar

print(".".join(curso)) #Concatenação de strings. Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'


Pi = 3.14159

print(f"Valor de PI: {Pi:.2f}")

print(f"Valor de PI: {Pi:10.2f}") #O número 10 informa o total de caracteres que deve ser ocupado.