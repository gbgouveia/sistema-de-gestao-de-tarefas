def usuarios(voltar):
    while True:
        print("===================================")
        print("         MENU USUARIOS             ")
        print("===================================")
        print("1. Cadastrar novo usuário")
        print("2. Listar usuários")
        print("3. Ativar/Inativar usuário")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_novo_usuário()
        elif opcao == "2":
            listar_usuários()
        elif opcao == "3":
           ativar_inativar_usuário()
        elif opcao == "4":
           return voltar
        else:
            print("Opção inválida. Tente novamente.")


lista_usuarios = []

def cadastrar_novo_usuário():
    
    while True:
        print("----------------------- CRIAR USUÁRIO ----------------------------")

        nome = input("Nome Completo: ")
        login = input("login: ")
        status = input("Ativo ou Inativo: ")
        
       
        
        usuario = {
            "Nome": nome,
            "Login": login,
            "status": status,
            
        }

        # Adicionar na lista de alunos
        lista_usuarios.append(usuario)
        print("Usuário criado com sucesso!!")

        continuacao = input("Quer cadastrar um novo usuário? (s/n): ").lower()
        if continuacao == "n":
            return 
           


def listar_usuários():
    if not lista_usuarios:
        print("Nenhum usuário cadastrado.")
        return

    print("----------------------- LISTA DE USUÁRIOS ----------------------------")
    for i, usuario in enumerate(lista_usuarios, start=1):
        print(f"{i}. {usuario['Nome']} - {usuario['Login']} - {usuario['status']}")


def ativar_inativar_usuário(indice):

    print("----------------------- ATIVAR/INATIVAR USUÁRIO ----------------------------")
    
    Nome = input("Digite o nome do usuário que deseja ativar/inativar (ou digite 'voltar' para sair): ")
    usuario = ativar_inativar_usuário [indice]
    print(f"Status: {usuario['usuario']}")
    status_do_usuario = input("status ativo/inativo (deixe em branco para manter): ") or usuario.get('status', '')
status = input("status (deixe em branco para manter): ") or ativar_inativar_usuário.get('descricao', '')
 