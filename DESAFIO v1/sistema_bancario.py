# Variáveis: 
saldo = 0
saques_diario = 0
extrato = " "
LIMITE_SAQUES = 3
LIMITE_DIARIO = 500
depositos = [] 
valores_sacados = [] # Deve ficar de fora do loop para evitar a reinicialização
total_sacado_diario = 0

while True:
    print( """ - - - - - MENU - - - - - 
[1] - DEPOSITAR 
[2] - SACAR
[3] - EXTRATO
[0] - SAIR
- - - - - - - - - - - - - 
    """)
    opcao = int(input("OPERAÇÃO: "))

    if opcao == 1:
        print("> DEPOSITO")
        valor_deposito = float(input("Digite o valor do depósito: R$ "))
        if valor_deposito < 0: # Filtra e impede valores negativos
            print("Valor INVÁLIDO!")
            continue
        else:
            saldo += valor_deposito # Soma o valor depositado ao saldo 
            depositos.append(valor_deposito) # Adiciona o valor depositado na lista "depositos"
            print(f"O valor R$ {valor_deposito} foi depositado!") 

    elif opcao == 2:
        print("> SACAR")
        valor_saque = float(input("Digite o valor para o saque: R$ "))
        if valor_saque < 0:
            print("Saque INVÁLIDO!") # Impossibilita de retirar valores negativos
            continue
        else:
            if valor_saque > saldo: # Analisa se o valor sacado é maior que o saldo em conta
                print("Valor não disponível na conta!")
                continue

            if saques_diario >= LIMITE_SAQUES: # Verifica se a quant. de saques diários está fora do limite.
                print("Limite de saques diários atingido!")
                continue
            
            elif saques_diario < LIMITE_SAQUES: # Verifica se a quant. de saques diários está dentro dos limites, se sim: 
                if valor_saque >= LIMITE_DIARIO: # Observa se o valor do saque é maior ou igual ao limite diário de saque
                    print("O valor sacado ultrapassa o limite diário!")
                    continue
                saques_diario += 1 # Conta mais um ao saques realizados no dia 
                valores_sacados.append(valor_saque)
                saldo -= valor_saque # Subtrai o valor sacado do saldo
                total_sacado_diario += valor_saque # Soma os valores sacados no dia 
                print(f"O valor R$ {valor_saque} foi sacado!\nSaques realizados: {saques_diario}/{LIMITE_SAQUES}")
            
    elif opcao == 3:
        print("> EXTRATO")
        print(f"Saldo atual: R$ {saldo}")
        print(f"Depósitos realizados: {depositos}")
        print(f"Saques realizados: {valores_sacados}")
        print(f"Quantidade de saques realizados: {saques_diario}/{LIMITE_SAQUES}")
        print(f"Total sacado hoje: R$ {total_sacado_diario}")
        print(f"Total disponível para saque hoje: R$ {LIMITE_DIARIO - total_sacado_diario}")

    elif opcao == 0:
        print("\n> SAIR\nFechando sistema...")
        break
    else:
        print("Opção INVÁLIDA! Tente novamente.")
        continue