import usuarios
import tarefas
import relatorios

def menu_principal():
    while True:
        print("===================================")
        print("         MENU PRINCIPAL            ")
        print("===================================")
        print("1. Gerenciar Usuários")
        print("2. Gerenciar Tarefas")
        print("3. Geranciar Relatórios")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuarios.usuarios(menu_principal)
        elif opcao == "2":
            tarefas.criar_tarefa(menu_principal)
        elif opcao == "3":
            relatorios.relatorio(menu_principal)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_principal()

