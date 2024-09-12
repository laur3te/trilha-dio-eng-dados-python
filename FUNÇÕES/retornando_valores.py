numero = int(input("Insira um número: "))

def calcular_soma (numeros_soma):
    return sum(numeros_soma)

def retorna_antecessor_e_sucessor (numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def ola_mundo():
    print("Olá mundo!")

print(retorna_antecessor_e_sucessor(numero))
print(ola_mundo()) #Função sem retorno - NONE.
print(calcular_soma([20, 80, 91]))