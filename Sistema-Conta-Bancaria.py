def menu():
    menu = """\n
    ============ BEM-VINDO ==============
    [d] Depositar
    [s] Sacar
    [e] Extrato
    ============ MAIS OPÇÕES ============
    [nc] Nova Conta
    [nu] Novo Usuário
    [lc] Listar Contas
    [q] Sair
    =====================================
    """
    return input(menu)

def depositar(saldo_da_conta, valor, extrato_da_conta, /):
    if valor > 0:
        saldo_da_conta = saldo_da_conta + valor
        extrato_da_conta = f"Depósito: R${valor:.2f}\n"
        print(f"\nO depósito no valor de R${valor:.2f} foi realizado com sucesso!\n")
    else:
        print("\nNão foi possível realizar a operação, o valor inserido é inválido!\n")
    return saldo_da_conta, extrato_da_conta

def sacar(*, saldo_da_conta, valor, extrato_da_conta, limite_da_conta, numeros_de_saque, limite_saques):
    excedeu_saldo_da_conta = saldo_da_conta < valor
    excedeu_limites_da_conta = limite_da_conta < valor
    excedeu_numeros_de_saque = numeros_de_saque >= limite_saques
    if excedeu_saldo_da_conta:
        print("\nO saldo da conta é insuficiente!\n")
    elif excedeu_limites_da_conta:
        print("\nO limite da conta é insuficiente!\n")
    elif excedeu_numeros_de_saque:
        print("\nO número de saques permitidos foi excedido!\n")
    elif valor > 0:
        saldo_da_conta = saldo_da_conta - valor
        extrato_da_conta += f"Saque: R${valor:.2f}\n"
        numeros_de_saque += 1
        print(f"\nO saque no valor de R${valor:.2f} foi realizado com sucesso!\n")
    else:
        print("\nO valor informado é inválido!")
    return saldo_da_conta, extrato_da_conta

def exibir_extrato(saldo_da_conta, /, *, extrato_da_conta):
    print("\n========= EXTRATO BANCARIO =========")
    print("Extrato Bancário sem movimentação" if not extrato_da_conta else extrato_da_conta)
    print(f"\nSaldo da conta: {saldo_da_conta:.2f}\n=====================")

def filtrar_usuario(cpf, usuarios_cadastrados):
    usuarios_cadastrados_filtrados = [usuario for usuario in usuarios_cadastrados if usuario["cpf"] == cpf]
    return usuarios_cadastrados_filtrados[0] if usuarios_cadastrados_filtrados else None

def cadastrar_usuario(usuarios_cadastrados):
    cpf = input("Informe somente os números do seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios_cadastrados)

    if usuario:
        print("\nUsuário com CPF já registrado!")
        return
    nome_completo = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento no formato dd-mm-aaaa: ")

    endereco = input("Informe o endereço no formato logradouro, nº, bairro, cidade-sigla estado, CEP: ")

    usuarios_cadastrados.append({"nome": nome_completo, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\nUsuário cadastrado com sucesso!\n")

def criar_conta(agencia, numero_conta, usuarios_cadastrados):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios_cadastrados)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, criação de conta encerrado!")

def listar_contas(contas_vinculadas):
    for conta in contas_vinculadas:
        linha = f"""\n
            Agência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo_da_conta = 0
    limite_da_conta = 500
    extrato_da_conta = ""
    numeros_de_saque = 0
    usuarios_cadastrados = []
    contas_vinculadas = []
    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("Digite o valor a ser depositado: "))
            saldo_da_conta, extrato_da_conta = depositar(saldo_da_conta, valor, extrato_da_conta)

        elif opcao == "s":
            valor = float(input("Digite o valor a ser sacado: "))
            saldo_da_conta, extrato_da_conta = sacar(
                saldo_da_conta = saldo_da_conta,
                valor = valor,
                extrato_da_conta = extrato_da_conta,
                limite_da_conta = limite_da_conta,
                numeros_de_saque = numeros_de_saque,
                limite_saques = LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo_da_conta, extrato_da_conta = extrato_da_conta)

        elif opcao == "nu":
            cadastrar_usuario(usuarios_cadastrados)

        elif opcao == "nc":
            numero_conta = len(contas_vinculadas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios_cadastrados)

            if conta:
                contas_vinculadas.append(conta)

        elif opcao == "lc":
            listar_contas(contas_vinculadas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, selecione a operação desejada.")

main()