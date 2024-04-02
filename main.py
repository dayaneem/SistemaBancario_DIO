menu = """
########### BANCO ###########
#                           #
#      [d] Depositar        # 
#      [s] Sacar            #
#      [e] Extrato          #
#      [q] Sair             #
#                           #
#############################

Digite a opção desejada: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("### Depósito ###")
        valor_deposito = float(input("Digite o valor que deseja depositar: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f"Depósito de R$ {float(valor_deposito)} foi realizado com sucesso")
            extrato += f"Depósito no valor de R$ {float(valor_deposito)}.\n"
        else:
            print("Impossível depositar um valor negativo. Tente novamente.")

    elif opcao == "s":
        print("### Saque ###")
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        if numero_saques < 3:
            if valor_saque > 0:
                if valor_saque <= saldo:
                    if valor_saque > 500:
                        print(f"Não foi possível realizar a operação. Seu limite de saque é de R$ {float(limite)}.")
                    else:
                        print(f"Saque de R$ {float(valor_saque)} foi realizado com sucesso")
                        saldo -= valor_saque
                        extrato += f"Saque no valor de R$ {float(valor_saque)}.\n"
                        numero_saques += 1
                else:
                    print(f"Não foi possível realizar a operação. Seu saldo atual é de R$ {float(saldo)}.")
            else:
                print("Impossível sacar um valor negativo. Tente novamente.")
        else:
            print(f"Você atingiu o número limite de 3 saques diários. Tente novamente amanhã.")

    elif opcao == "e":
        print("### Extrato ###")
        print(extrato)
        print(f"Seu saldo atual é de R$ {float(saldo)}.")

    elif opcao == "q":
        print("Você está saindo do sistema bancário. Obrigado pela preferência.")
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a opção desejada.")
