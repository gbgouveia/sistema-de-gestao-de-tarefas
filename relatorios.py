import tarefas

def relatorio(voltar):
    while True:
        print("\n========== RELATÓRIOS ==========")
        print("1. Ver tarefas por Status")
        print("2. Ver tarefas por Prioridade")
        print("3. Ver tarefas por Usuário")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tarefas_por_status()
        elif opcao == "2":
            tarefas_por_prioridade()
        elif opcao == "3":
            tarefas_por_usuario()
        elif opcao == "4":
            return voltar
        else:
            print("Opção inválida, tente novamente.")

def tarefas_por_status():
    print("\n----------------- TAREFAS POR STATUS -----------------")
    status = input("Digite o status (Pendente ou Concluída): ").capitalize()

    # Debug: conferir lista completa e valor buscado
    print(f"DEBUG - Status buscado: {status}")
    print(f"DEBUG - Lista atual de tarefas: {tarefas.lista_tarefas}")

    tarefas_filtradas = [
        tarefa for tarefa in tarefas.lista_tarefas 
        if tarefa.get('Status', '').capitalize() == status
    ]

    if not tarefas_filtradas:
        print(f"Nenhuma tarefa encontrada com status '{status}'.")
    else:
        for t in tarefas_filtradas:
            print(f"{t.get('Tarefa', 'N/A')} - {t.get('Descrição', 'N/A')} - Prioridade: {t.get('Nivel de Prioridade', 'N/A')} - Data Limite: {t.get('Data Limite', 'N/A')} - Status: {t.get('Status', 'N/A')} - Usuário: {t.get('Usuario', 'N/A')}")

def tarefas_por_prioridade():
    prioridade = input("Digite a prioridade (Alta, Média, Baixa): ").capitalize()

    # Debug: conferir lista completa e valor buscado
    print(f"DEBUG - Prioridade buscada: {prioridade}")
    print(f"DEBUG - Lista atual de tarefas: {tarefas.lista_tarefas}")

    filtradas = [t for t in tarefas.lista_tarefas if t.get('Nivel de Prioridade', '').capitalize() == prioridade]
    if not filtradas:
        print(f"Nenhuma tarefa com prioridade '{prioridade}'.")
        return
    for t in filtradas:
        print(f"{t.get('Tarefa', 'N/A')} - {t.get('Descrição', 'N/A')} - Prioridade: {t.get('Nivel de Prioridade', 'N/A')} - Data Limite: {t.get('Data Limite', 'N/A')} - Status: {t.get('Status', 'N/A')} - Usuário: {t.get('Usuario', 'N/A')}")

def tarefas_por_usuario():
    usuario = input("Digite o nome/login do usuário: ").lower()

    # Debug: conferir lista completa e valor buscado
    print(f"DEBUG - Usuário buscado: {usuario}")
    print(f"DEBUG - Lista atual de tarefas: {tarefas.lista_tarefas}")

    filtradas = [t for t in tarefas.lista_tarefas if t.get('Usuario', '').lower() == usuario]
    if not filtradas:
        print(f"Nenhuma tarefa para o usuário '{usuario}'.")
        return
    for t in filtradas:
        print(f"{t.get('Tarefa', 'N/A')} - {t.get('Descrição', 'N/A')} - Prioridade: {t.get('Nivel de Prioridade', 'N/A')} - Data Limite: {t.get('Data Limite', 'N/A')} - Status: {t.get('Status', 'N/A')} - Usuário: {t.get('Usuario', 'N/A')}")
               