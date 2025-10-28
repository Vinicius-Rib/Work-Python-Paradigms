# Dicionário principal
republica = {}
# Lista global com os tipos de contas (pode crescer)
tipos_contas = []

def menu():
    print("\n--- SISTEMA DE GESTÃO DE CONTAS - REPÚBLICA ---")
    print("1 - Adicionar morador")
    print("2 - Cadastrar novo tipo de conta")
    print("3 - Adicionar conta a um morador")
    print("4 - Depositar dinheiro")
    print("5 - Listar contas e saldos")
    print("6 - Pagar conta")
    print("0 - Sair")


# Função para adicionar morador
def adicionar_morador():
    nome = input("Nome do morador: ").capitalize()
    if nome in republica:
        print("Este morador já está cadastrado!")
    else:
        # Cria dicionário do morador com saldo e as contas disponíveis até o momento
        republica[nome] = {
            "saldo": 0.0,
            "contas": {tipo: [] for tipo in tipos_contas}
        }
        print(f"Morador {nome} adicionado com sucesso!")


# Função para cadastrar novo tipo de conta
def cadastrar_tipo_conta():
    tipo = input("Digite o nome do novo tipo de conta: ").lower()
    if tipo in tipos_contas:
        print("Esse tipo de conta já existe!")
        return

    tipos_contas.append(tipo)

    # Adiciona a nova conta a todos os moradores já cadastrados
    for dados in republica.values():
        dados["contas"][tipo] = []

    print(f"Tipo de conta '{tipo}' cadastrado com sucesso!")


# Função para adicionar conta a um morador
def adicionar_conta():
    if not republica:
        print("Nenhum morador cadastrado ainda!")
        return
    if not tipos_contas:
        print("Nenhum tipo de conta cadastrado ainda!")
        return

    print("Escolha uma opção:")
    print("1 - Dividir a conta igualmente entre todos os moradores")
    print("2 - Atribuir a conta a um único morador")

    opcao = input("Digite 1 ou 2: ")

    if opcao == "1":
        # Dividir igualmente entre todos os moradores
        print("Tipos de conta disponíveis:")
        for i, tipo in enumerate(tipos_contas, 1):
            print(f"{i} - {tipo.capitalize()}")

        tipo_conta = input("Escolha o tipo de conta: ").lower()

        if tipo_conta in tipos_contas:
            valor_total = float(input(f"Qual o valor total da conta de {tipo_conta}: R$ "))
            valor_individual = valor_total / len(republica)

            # Adiciona o valor da conta dividida para todos os moradores
            for morador in republica:
                republica[morador]["contas"][tipo_conta].append(valor_individual)

            print(f"Conta de {tipo_conta} (R$ {valor_total:.2f}) dividida igualmente entre todos os moradores.")
        else:
            print("Tipo de conta inválido!")

    elif opcao == "2":
        # Atribuir a conta a um único morador
        nome = input("Qual morador vai ser responsável pela conta? ").capitalize()

        if nome in republica:
            print("Tipos de conta disponíveis:")
            for i, tipo in enumerate(tipos_contas, 1):
                print(f"{i} - {tipo.capitalize()}")

            tipo_conta = input("Escolha o tipo de conta: ").lower()

            if tipo_conta in tipos_contas:
                valor = float(input(f"Qual o valor da conta de {tipo_conta}: R$ "))
                republica[nome]["contas"][tipo_conta].append(valor)
                print(f"Conta de {tipo_conta} (R$ {valor:.2f}) adicionada para {nome}.")
            else:
                print("Tipo de conta inválido!")
        else:
            print("Morador não encontrado!")

    else:
        print("Opção inválida! Digite 1 ou 2.")

# Função para depósito
def depositar():
    if not republica:
        print("Nenhum morador cadastrado ainda!")
        return

    nome = input("Nome do morador: ").capitalize()
    if nome not in republica:
        print("Morador não encontrado!")
        return

    valor = float(input("Valor do depósito: R$ "))
    republica[nome]["saldo"] += valor
    print(f"Depósito de R$ {valor:.2f} feito para {nome}.")


# Função para listar contas e saldos
def listar_contas():
    if not republica:
        print("Nenhum morador cadastrado ainda!")
        return

    print("\n--- SITUAÇÃO ATUAL DA REPÚBLICA ---")
    for nome, dados in republica.items():
        print(f"\n {nome} | Saldo: R$ {dados['saldo']:.2f}")
        for tipo, lista in dados["contas"].items():
            if lista:
                print(f"  {tipo.capitalize()}: {lista}")
            else:
                print(f"  {tipo.capitalize()}: Nenhuma conta pendente")


# Função para pagar conta
def pagar_conta():
    if not republica:
        print("Nenhum morador cadastrado ainda!")
        return
    if not tipos_contas:
        print("Nenhum tipo de conta cadastrado ainda!")
        return

    nome = input("Nome do morador: ").capitalize()
    if nome not in republica:
        print("Morador não encontrado!")
        return

    print("Tipos de conta disponíveis:")
    for i, tipo in enumerate(tipos_contas, 1):
        print(f"{i} - {tipo.capitalize()}")
    opc = input("Escolha o tipo de conta para pagar: ")

    if opc.isdigit() and 1 <= int(opc) <= len(tipos_contas):
        tipo = tipos_contas[int(opc) - 1]
        if republica[nome]["contas"][tipo]:
            valor = republica[nome]["contas"][tipo].pop(0)
            if republica[nome]["saldo"] >= valor:
                republica[nome]["saldo"] -= valor
                print(f"{nome} pagou R$ {valor:.2f} da conta de {tipo}.")
            else:
                print("Saldo insuficiente para pagar a conta!")
                republica[nome]["contas"][tipo].insert(0, valor)
        else:
            print("Nenhuma conta pendente desse tipo.")
    else:
        print("Opção inválida!")


# === LOOP PRINCIPAL ===
while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_morador()
    elif opcao == "2":
        cadastrar_tipo_conta()
    elif opcao == "3":
        adicionar_conta()
    elif opcao == "4":
        depositar()
    elif opcao == "5":
        listar_contas()
    elif opcao == "6":
        pagar_conta()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")
