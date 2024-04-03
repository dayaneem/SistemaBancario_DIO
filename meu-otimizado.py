def menu():
    menu = """
    ############# BANCO ############
    #                              #
    #      [d] Depositar           # 
    #      [s] Sacar               #
    #      [e] Extrato             #
    #      [n] Novo usuário        #
    #     [lu] Listar usuários     #
    #      [c] Nova conta          #
    #     [lc] Listar contas       #
    #      [q] Sair                #
    #                              #
    ################################

    Digite a opção desejada: """
    return input(menu)

def depositar(saldo, valor_deposito, extrato, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        print(f"\nDepósito de R$ {valor_deposito:.2f} foi realizado com sucesso!\n")
        extrato += f"Depósito no valor de R$ {valor_deposito:.2f}.\n"
    else:
        print("Impossível depositar um valor negativo. Tente novamente.\n")
    return saldo, extrato

def sacar(*, saldo, valor_saque, extrato, numero_saques, limite_por_saque, LIMITE_SAQUES):
    if numero_saques < LIMITE_SAQUES:
        if valor_saque > 0:
            if valor_saque <= saldo:
                if valor_saque > limite_por_saque:
                    print(f"Não foi possível realizar a operação. Seu limite de saque é de R$ {limite_por_saque:.2f}.\n")
                else:
                    print(f"\nSaque de R$ {valor_saque:.2f} foi realizado com sucesso.\n")
                    saldo -= valor_saque
                    extrato += f"Saque no valor de R$ {valor_saque:.2f}.\n"
                    numero_saques += 1
            else:
                print(f"Não foi possível realizar a operação. Seu saldo atual é de R$ {saldo:.2f}.\n")
        else:
            print("Impossível sacar um valor negativo. Tente novamente.\n")
    else:
        print(f"Você atingiu o número limite de 3 saques diários. Tente novamente amanhã.\n")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("###### Extrato ######\n")
    print(extrato)
    print(f"Seu saldo atual é de R$ {saldo:.2f}.\n")

def novo_usuario():
    if cpf_novo:
        if cpf_novo in lista_cpf:
            print("\nCPF já cadastrado.\n")
        else:
            lista_cpf.append(cpf_novo)
            nome = input("\nInforme o nome completo: ")
            data_nascimento = input("\nInforme a data de nascimento (dd/mm/aaaa): ")
            endereco = input("\nInforme o endereço completo: ")

            usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf":cpf_novo, "endereco":endereco})
            print("\nUsuário cadastrado com sucesso!\n")
            print(usuarios)

def filtrando_usuario(cpf_novo):
    for usuario in usuarios:
        if cpf_novo == usuario["cpf"]:
            return usuario["nome"]
    return False

def nova_conta(cpf_novo, numero_conta):
    usuario = filtrando_usuario(cpf_novo)
    if usuario:
        usuario_dict = {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}
        print("\nConta criada com sucesso!\n")
        print (usuario_dict)
        return usuario_dict
    else:
        print("CPF não cadastrado.\nCadastre um novo cliente.\n")
        print("###### Cadastro de nova conta ######\n")
        novo_usuario()
    return False

def listar_contas(contas):
    print("###### Listar contas ######\n")
    for conta in contas:
        linha = (f"""
            Agência: {"0001"}
            C/C: {conta["numero_conta"]}
            Titular: {conta["nome"]}
        """)
        print("=" * 100)
        print(linha)

def listar_usuarios(usuarios):
    print ("###### Listar usuários ######\n")
    for usuario in usuarios:
        linha = (f"""
            Nome: {usuario["nome"]}
            CPF: {usuario["cpf"]}
            Data de nascimento: {usuario["data_nascimento"]}
            Endereço: {usuario["endereco"]}
        """)
        print("=" * 100)
        print(linha)

saldo = 0
limite_por_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
AGENCIA = "0001"
numero_conta = 0
lista_cpf = []

while True:
    opcao = menu()

    if opcao == "d":
        print("###### Depósito ######\n")
        valor_deposito = float(input("Digite o valor que deseja depositar: "))

        saldo, extrato = depositar(saldo, valor_deposito, extrato)

    elif opcao == "s":
        print("###### Saque #######\n")
        valor_saque = float(input("Digite o valor que deseja sacar: "))

        saldo, extrato = sacar(
            saldo=saldo,
            valor_saque=valor_saque,
            extrato=extrato,
            limite_por_saque=limite_por_saque,
            numero_saques=numero_saques,
            LIMITE_SAQUES=LIMITE_SAQUES,
        )

    elif opcao == "n":
        print("###### Cadastro de novo cliente ######\n")
        cpf_novo = input("Informe o número do CPF (apenas números): ")
        novo_usuario()

    elif opcao == "c":
        print("###### Cadastro de nova conta ######\n")
        cpf_novo = input("Informe o número do CPF (apenas números): ")
        numero_conta += 1
        contas_bancarias = nova_conta(cpf_novo, numero_conta)
        contas.append(contas_bancarias)

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "lu":
        listar_usuarios(usuarios)

    elif opcao == "lc":
        listar_contas(contas)

    elif opcao == "q":
        print("\nVocê está saindo do sistema bancário. Obrigado pela preferência.")
        break

    else:
        print("\nOperação inválida. Por favor, selecione novamente a opção desejada.\n")
