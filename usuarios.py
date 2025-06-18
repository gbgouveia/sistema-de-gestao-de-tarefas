lista_usuarios = []

def usuarios(voltar):
    while True:
        print("\n===================================")
        print("         MENU DE USUÁRIOS          ")
        print("===================================")
        print("1. Cadastrar novo usuário")
        print("2. Listar usuários")
        print("3. Ativar/Inativar usuário")
        print("4. Voltar ao Menu Principal")
        print("===================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_novo_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            ativar_inativar_usuario()
        elif opcao == "4":
            return voltar
        else:
            print("Opção inválida. Tente novamente.")


# ===================== CADASTRAR NOVO USUÁRIO ======================

def cadastrar_novo_usuario():
    while True:
        print("\n=========== CADASTRAR NOVO USUÁRIO ===========")

        nome = input("Nome: ").strip()
        login = input("Login: ").strip()

        # Verificar se o login já existe
        if any(usuario["Login"] == login for usuario in lista_usuarios):
            print("Este login já está cadastrado. Tente outro.")
            continue

        status = input("Status (Ativo/Inativo): ").strip().capitalize()
        if status not in ["Ativo", "Inativo"]:
            print("Status inválido. Use 'Ativo' ou 'Inativo'.")
            continue

        usuario = {
            "Nome": nome,
            "Login": login,
            "Status": status
        }

        lista_usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")

        continuar = input("Deseja cadastrar outro usuário? (s/n): ").lower()
        if continuar != 's':
            break


# ===================== LISTAR USUÁRIOS ======================

def listar_usuarios():
    print("\n=========== LISTA DE USUÁRIOS ===========")

    if not lista_usuarios:
        print("Nenhum usuário cadastrado.")
        return

    for i, usuario in enumerate(lista_usuarios, start=1):
        print(f"{i}. Nome: {usuario['Nome']} | Login: {usuario['Login']} | Status: {usuario['Status']}")
    
    print("===========================================")


# ===================== ATIVAR / INATIVAR USUÁRIO ======================

def ativar_inativar_usuario():
    listar_usuarios()

    if not lista_usuarios:
        return

    login = input("\nDigite o login do usuário para alterar o status (ou 'voltar' para cancelar): ").strip()
    if login.lower() == 'voltar':
        return

    for usuario in lista_usuarios:
        if usuario["Login"] == login:
            status_atual = usuario["Status"]
            print(f"Status atual de {usuario['Nome']}: {status_atual}")

            novo_status = input("Digite o novo status (Ativo/Inativo): ").strip().capitalize()
            if novo_status not in ["Ativo", "Inativo"]:
                print("Status inválido. Use 'Ativo' ou 'Inativo'.")
                return

            usuario["Status"] = novo_status
            print(f"Status de {usuario['Nome']} alterado para {novo_status}.")
            return

    print("Usuário não encontrado.")
