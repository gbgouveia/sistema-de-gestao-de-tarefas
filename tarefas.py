import relatorios
import usuarios

lista_tarefas = []

def criar_tarefa(voltar):
    while True:
            print("\n===================================")
            print("            MENU TAREFAS           ")
            print("===================================")
            print("1. Criar Tarefa")
            print("2. Listar Tarefas")
            print("3. Voltar ao Menu Principal")
            print("===================================")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                criador_de_tarefa()
            elif opcao == "2":
                gerenciar_tarefas()
            elif opcao == "3":
                return voltar
            else:
                print("Opção inválida. Tente novamente.")


# ===================== CRIAR NOVA TAREFA ======================

def criador_de_tarefa():
    global lista_tarefas

    while True:
        print("\n=========== CADASTRAR NOVA TAREFA ===========")

        titulo = input("Título da tarefa: ").strip()
        descricao = input("Descrição: ").strip()
        prioridade = input("Prioridade (Alta, Média, Baixa): ").strip().capitalize()
        data_limite = input("Data limite (DD/MM/AAAA): ").strip()
        status = input("Status (Pendente ou Concluída): ").strip().capitalize()
        usuario = input("Para quem é esta tarefa? (login do usuário): ").strip()
         
        tarefa = {
             "Título": titulo,
            "Descrição": descricao,
            "Prioridade": prioridade,
            "Data Limite": data_limite,
             "Status": status,
            "Usuário": usuario
        }

        lista_tarefas.append(tarefa)
        print("Tarefa cadastrada com sucesso!")

        continuar = input("Deseja cadastrar outra tarefa? (s/n): ").lower()
        if continuar != 's':
            break


# ===================== GERENCIAR TAREFAS ======================

def gerenciar_tarefas():
    global lista_tarefas

    if not lista_tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    
    print("\n=========== LISTA DE TAREFAS ===========")
    for i, tarefa in enumerate(lista_tarefas, start=1):
         print(f"{i}. {tarefa['Título']} | {tarefa['Descrição']} | Prioridade: {tarefa['Prioridade']} | "
              f"Data: {tarefa['Data Limite']} | Status: {tarefa['Status']} | Usuário: {tarefa['Usuário']}")
    print("=========================================")

    print("\nDigite o número da tarefa para editar ou '0' para voltar.")
    opcao = input("Escolha uma opção: ")
    if opcao == "0":
        return
    else:
        try:
            indice = int(opcao) - 1
            if 0 <= indice < len(lista_tarefas):
                editar_tarefa(indice)
            else:
                print("Opção invalida")
        except ValueError:
            print("Entrada invalida. Use numeros.")


# ===================== EDITAR TAREFA ======================

def editar_tarefa(indice):
    global lista_tarefas

    tarefa = lista_tarefas[indice]
    print(f"\nEditando tarefa: {tarefa['Título']}")

    titulo = input(f"Novo título ({tarefa['Título']}): ") or tarefa['Título']
    descricao = input(f"Nova descrição ({tarefa['Descrição']}): ") or tarefa['Descrição']
    prioridade = input(f"Nova prioridade ({tarefa['Prioridade']}): ") or tarefa['Prioridade']
    data_limite = input(f"Nova data limite ({tarefa['Data Limite']}): ") or tarefa['Data Limite']
    status = input(f"Novo status ({tarefa['Status']}): ") or tarefa['Status']
    usuario = input(f"Novo usuário ({tarefa['Usuário']}): ") or tarefa['Usuário']

    lista_tarefas[indice] = {
        "Título": titulo,
        "Descrição": descricao,
        "Prioridade": prioridade,
        "Data Limite": data_limite,
        "Status": status,
        "Usuário": usuario
    }

    print("Tarefa atualizada com sucesso!")

# ===================== EXCLUIR TAREFA ======================

def excluir_tarefa(indice):
    global lista_tarefas

    if 0 <= indice < len(lista_tarefas):
        tarefa = lista_tarefas.pop(indice)
        print(f"Tarefa '{tarefa['Título']}' excluída com sucesso!")

    else:
        print(f"\nÍndice {indice} fora do intervalo. Nenhuma tarefa excluída.")

# ===================== FILTRAR POR STATUS ======================

def filtrar_tarefas_por_status(status):
    global lista_tarefas
    filtradas = [t for t in lista_tarefas if t['Status'].lower() == status.lower()]

    if not filtradas:
        print(f"Nenhuma tarefa com status '{status}'.")
    else:
         print(f"\nTarefas com status '{status}':")
    for t in filtradas:
            print(f"- {t['Título']} | {t['Descrição']} | Usuário: {t['Usuário']}")


# ===================== FILTRAR POR PRIORIDADE ======================

def filtrar_por_prioridade(prioridade):
    global lista_tarefas

    filtradas = [t for t in lista_tarefas if t['Prioridade'].lower() == prioridade.lower()]

    if not filtradas:
        print(f"Nenhuma tarefa com prioridade '{prioridade}'.")

    else:
        print(f"\nTarefas com prioridade '{prioridade}':")
        for t in filtradas:
            print(f"- {t['Título']} | {t['Descrição']} | Usuário: {t['Usuário']}")


