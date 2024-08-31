menu = """
    =================================
    =        Sistema Bancario       =
    =================================
    = 1 - Depositar Dinheiro        =
    = 2 - Sacar Dinheiro            =
    = 3 - Ver Extrato               =
    = 4 - Sair                      =
    =================================
"""
LIMITE_SAQUE_DIARIO = 500
LIMITE_QUANTIDADE_SAQUE = 3
saldo = 0
quantidade_saque_realizado = 0
numero_trasacao = 0
extrato = {}

while True:
    print(menu)  
    try: 
        opcao = int(input("    Entre com a opção desejada: "))
    except ValueError:
        print("\n\n***    Opção inválida. Por favor, tente novamente.   ***\n")
        continue
    if opcao == 1:     # deposito 
        try:       
            valor = float(input("\n    Qual valor você deseja depositar? R$ "))
        except ValueError:
            print("\n***   Valor inválido   ***")
            continue
        if valor > 0:
            saldo += valor
            numero_trasacao += 1
            extrato[str(numero_trasacao) + " - Deposito"] = valor
            print(f"\n\n    Saldo atual: R${saldo:.2f}\n") 
            continue
        else:
            print("\n***    Valor inválido. Por favor, tente novamente.   ***\n")
        
    
    elif opcao == 2:    # saque
        if quantidade_saque_realizado >= LIMITE_QUANTIDADE_SAQUE:
            print(f"\n***   Limite de saque diário {LIMITE_DE_SAQUE_DIARIO } atingido! Não pode ser realizado.   ***\n")
            continue
        try:
            valor = float(input("\n    Qual valor você deseja sacar? R$ "))
        except ValueError:
            print("\n***   Valor inválido   ***")
            continue
        if  valor > saldo:
            print("\n***       Saldo insuficiente! Não pode ser realizado.   ***\n")
            continue
        if  valor > LIMITE_SAQUE_DIARIO:
            print("\n***       Limite de valor do saque diário atingido! Não pode ser realizado.   ***\n")
            continue
        if valor > 0:    
            saldo -= valor
            numero_trasacao += 1            
            extrato[str(numero_trasacao) + ' - Saque'] = valor
            quantidade_saque_realizado += 1
            print(f"\n\n    Saldo atual: R${saldo:.2f}\n") 
        else: 
            print("\n***   Valor inválido   ***")
    elif opcao == 3:
        print("\n\n===========\n= EXTRATO =\n===========")
        for movimento,valor in extrato.items():
            print(f'{movimento} R$ {valor:.2f}')
        print(f"\n\n    Saldo atual: R${saldo:.2f}\n") 
        
    elif opcao == 4:
        print("\n\nAté logo.\n\n--------------")
        break
    else:
        print("\n\n***   Opção inválida. Por favor, tente novamente.   ***\n")        
        

        
        
        
        
