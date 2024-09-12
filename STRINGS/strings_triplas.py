nome = "Kaylane"
linguagem = "Java"
idade = "22"

mensagem = f'''
    Olá meu nome é {nome}, tenho {idade} anos.
    Sou estudante de {linguagem}.
    Estou aprendendo a manipular strings.
    '''

print(mensagem) #Preserva os espaços estabelecidos.


print(
    '''
    - - - - - - - - - MENU - - - - - - - - - 
            1 - Inserir novo registro
            2 - Deletar registro
            3 - Visualizar registro
            4 - Pesquisar registro
            5 - Sair
    - - - - - - - - - - - - - - - - - - - - -
'''
)

# Strings em múltiplas linhas 