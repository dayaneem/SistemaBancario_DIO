def menu():
    menu = """
    ########### BANCO ###########
    #                           #
    #      [d] Depositar        # 
    #      [s] Sacar            #
    #      [e] Extrato          #
    #      [n] Novo usuário     #
    #      [c] Nova conta       #
    #      [q] Sair             #
    #                           #
    #############################

    Digite a opção desejada: """
    return input(menu)

def depositar(saldo, valor_deposito, extrato, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        print(f"Depósito de R$ {valor_deposito:.2f} foi realizado com sucesso!")
        extrato += f"Depósito no valor de R$ {valor_deposito:.2f}.\n"
    else:
        print("Impossível depositar um valor negativo. Tente novamente.")
    return saldo, extrato

def sacar(*, saldo, valor_saque, extrato, numero_saques, limite_por_saque, LIMITE_SAQUES):
    if numero_saques < LIMITE_SAQUES:
        if valor_saque > 0:
            if valor_saque <= saldo:
                if valor_saque > limite_por_saque:
                    print(f"Não foi possível realizar a operação. Seu limite de saque é de R$ {limite_por_saque:.2f}.")
                else:
                    print(f"Saque de R$ {valor_saque:.2f} foi realizado com sucesso")
                    saldo -= valor_saque
                    extrato += f"Saque no valor de R$ {valor_saque:.2f}.\n"
                    numero_saques += 1
            else:
                print(f"Não foi possível realizar a operação. Seu saldo atual é de R$ {saldo:.2f}.")
        else:
            print("Impossível sacar um valor negativo. Tente novamente.")
    else:
        print(f"Você atingiu o número limite de 3 saques diários. Tente novamente amanhã.")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("### Extrato ###")
    print(extrato)
    print(f"Seu saldo atual é de R$ {saldo:.2f}.")

def novo_usuario(usuarios):
    #inserir teste de CPF
    if cpf_novo in lista_cpf:
        print("Erro: CPF já cadastrado.")
    else:
        lista_cpf.append(cpf_novo)
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
        endereco = input("Informe o endereço completo: ")

        usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf":cpf_novo, "endereco":endereco})
        print("Usuário cadastrado com sucesso!")
        print(usuarios)

#def filtrar_usuario(cpf_novo, usuarios, usuario):
        #usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf_novo]
        #return usuarios_filtrados[0] if usuarios_filtrados else None

def filtrando_usuario(cpf_novo, usuarios, usuario):
    for usuario in usuarios:
        if cpf_novo == usuario["cpf"]:
            return False
            usuario = ['nome']
        else:
            return True


def nova_conta(cpf_novo, numero_conta, usuario):
    usuario = filtrando_usuario(cpf_novo, usuarios, usuario)
    if usuario:
        numero_conta += 1
        return {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("CPF não cadastrado. Cadastre um novo cliente.\n")
        novo_usuario(usuarios)
    return numero_conta, usuario

def listar_contas(contas):
    for conta in contas_bancarias:
        linha = (f"""
            Agência: {conta["AGENCIA"]}
            C/C: {conta["numero_conta"]}
            Titular: {conta["usuario"]["nome"]}
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
        print("### Depósito ###")
        valor_deposito = float(input("Digite o valor que deseja depositar: "))

        saldo, extrato = depositar(saldo, valor_deposito, extrato)

    elif opcao == "s":
        print("### Saque ###")
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
        print("### Cadastro de novo cliente ###")
        cpf_novo = input("Informe o número do CPF (apenas números): ")
        novo_usuario(usuarios)

    elif opcao == "c":
        print("### Cadastro de nova conta ###")
        cpf_novo = input("Informe o número do CPF: ")
        contas_bancarias = nova_conta(cpf_novo, numero_conta, usuario)
        contas.append(contas_bancarias)

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "q":
        print("Você está saindo do sistema bancário. Obrigado pela preferência.")
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a opção desejada.")
