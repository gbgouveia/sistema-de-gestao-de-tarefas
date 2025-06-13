import usuarios
import tarefas

def relatorio(voltar):
    while True:
        print("===================================")
        print("         MENU RELATÓRIOS           ")
        print("===================================")
        print("1. Ver tarefas por status")
        print("2. Ver tarefas por prioridade")
        print("3. Ver tarefas por usuários")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tarefas_por_status()
        elif opcao == "2":
            tarefas_por_prioridade()
        elif opcao == "3":
           tarefas_por_usuarios()
        elif opcao == "4":
           return voltar
        else:
            print("Opção inválida. Tente novamente.")

def tarefas_por_status():
    
    print("----------------------------- TAREFAS POR PENDÊNCIA ---------------------------------------")
    tarefas.filtrar_tarefas_por_status('pendente')

def tarefas_por_prioridade():
    
    print("----------------------------- TAREFAS POR PRIORIDADE -----------------------------")
    tarefas.prioridade()

def tarefas_por_usuarios():
    print("----------------------------- TAREFAS POR USUÁRIO -----------------------------")
    usuarios_encontrados = set(t["Usuario"] for t in tarefas.lista_tarefas)
    for usuario in usuarios_encontrados:
        print(f"\n--- Tarefas do usuário: {usuario} ---")
        tarefas_do_usuario = [t for t in tarefas.lista_tarefas if t.get("Usuario") == usuario]
        if not tarefas_do_usuario:
            print("Nenhuma tarefa para esse usuário.")
        else:
            for t in tarefas_do_usuario:
                print(f"{t['Tarefa']} - {t['Descrição']} - Prioridade: {t['Nivel de Prioridade']} - Status: {t['Status']}") 
                