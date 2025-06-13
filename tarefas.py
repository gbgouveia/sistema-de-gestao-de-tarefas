

def criar_tarefa(voltar):
    while True:
        print("===================================")
        print("         MENU TAREFAS              ")
        print("===================================")
        print("1. Criar Tarefa")
        print("2. Listar Tarefas")
        print("3. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criador_de_tarefa()
        elif opcao == "2":
            gerenciar_tarefas()
        elif opcao == "3":
           return voltar
        elif opcao == "4":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
"""  """

lista_tarefas = []

def criador_de_tarefa():
    while True:
        print("----------------------- CRIAR TAREFA ----------------------------")

        titulo_da_tarefa = input("Nome da tarefa: ")
        descricao = input("Descrição: ")
        prioridade = input("Nivel de prioridade: Alta, Média, Baixa: ")
        data_limite = input("Data limite: ")
        pendencia = input("Pendente ou Concluída: ")
        usuario = float(input("Para quem é esta tarefa? (apenas o número): "))
       
    
        tarefa = {
            "Tarefa": titulo_da_tarefa,
            "Descrição": descricao,
            "Nivel de Prioridade": prioridade,
            "Data Limite": data_limite,
            "Pendencia": pendencia,
            "Usuario": usuario,
        }

        lista_tarefas.append(tarefa)
        print("Tarefa criada com sucesso!!")

        continuacao = input("Quer cadastrar uma nova tarefa? (s/n): ").lower()
        if continuacao == "n":
            return 


def gerenciar_tarefas():
    if not lista_tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("----------------------- LISTA DE TAREFAS ----------------------------")
    for i, tarefa in enumerate(lista_tarefas, start=1):
        print(f"{i}. {tarefa['Tarefa']} - {tarefa['Descrição']} - {tarefa['Nivel de Prioridade']} - {tarefa['Data Limite']} - Pendencia: {tarefa['Pendencia']} - Usuario: {tarefa['Usuario']}")

    print("Digite o número da tarefa para editar ou '0' para voltar ao menu.")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "0":
        return
    else:
        try:
            indice = int(opcao) - 1
            if 0 <= indice < len(lista_tarefas):
                editar_tarefa(indice)
            else:
                print("Opção inválida.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")



def editar_tarefa(indice):
    tarefa = lista_tarefas[indice]
    print(f"Editando tarefa: {tarefa['Tarefa']}")
    
    titulo_da_tarefa = input("Novo nome da tarefa (deixe em branco para manter): ") or tarefa['Tarefa']
    descricao = input("Nova descrição (deixe em branco para manter): ") or tarefa['Descrição']
    prioridade = input("Nova prioridade (Alta, Média, Baixa) (deixe em branco para manter): ") or tarefa['Nivel de Prioridade']
    data_limite = input("Nova data limite (deixe em branco para manter): ") or tarefa['Data Limite']
    pendencia = input("Novo status (Pendente ou Concluída) (deixe em branco para manter): ") or tarefa['Pendencia']
    usuario = input("Novo usuário (deixe em branco para manter): ") or tarefa['Usuario']


    lista_tarefas[indice] = {
        "Tarefa": titulo_da_tarefa,
        "Descrição": descricao,
        "Nivel de Prioridade": prioridade,
        "Data Limite": data_limite,
        "Pendencia": pendencia,
        "Usuario": usuario,
    }
    
    print("Tarefa atualizada com sucesso!")
    


def excluir_tarefa(indice):
    if 0 <= indice < len(lista_tarefas):
        tarefa_excluida = lista_tarefas.pop(indice)
        print(f"Tarefa '{tarefa_excluida['Tarefa']}' excluída com sucesso!")
    else:
        print("Índice inválido. Nenhuma tarefa foi excluída.")
        


def filtrar_tarefas_por_status(pendencia):
    tarefas_filtradas = [tarefa for tarefa in lista_tarefas if tarefa.get('Pendencia') == pendencia]
    if not tarefas_filtradas:
        print(f"Nenhuma tarefa encontrada com o status '{pendencia}'.") 
    else:
        print(f"Tarefas com status '{pendencia}':")
        for tarefa in tarefas_filtradas:
            print(f"{tarefa['Tarefa']} - {tarefa['Descrição']} - {tarefa['Nivel de Prioridade']} - {tarefa['Data Limite']} - Pendencia: {tarefa['Pendencia']} - Usuario: {tarefa['Usuario']}")
            
            
def prioridade():
    tarefas_prioridade = [tarefa for tarefa in lista_tarefas if tarefa.get('Nivel de Prioridade')]
    if not tarefas_prioridade:
        print(f"Nenhuma tarefa encontrada com a prioridade.")
    else:
        print(f"Tarefas com prioridade:")
        for tarefa in tarefas_prioridade:
            print(f"{tarefa['Tarefa']} - {tarefa['Descrição']} - {tarefa['Nivel de Prioridade']} - {tarefa['Data Limite']} - Pendencia: {tarefa['Pendencia']} - Usuario: {tarefa['Usuario']}")