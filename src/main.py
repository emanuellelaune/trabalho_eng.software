import estrategias as t
import ListaDeTarefas as lt
import SaidaDeDados as sdd

## FUNÇÕES EXTRAS
def Salvamento(lista, metodo):
    if metodo == 1:
        ### Txt
        saidaDeDados = sdd.AdapterDados(sdd.DadosTXT())
        saidaDeDados.salvar_dados(lista.tarefas_registradas)
    elif metodo == 2:    
        ### Json
        saidaDeDados = sdd.AdapterDados(sdd.DadosJson())
        saidaDeDados.salvar_dados(lista.tarefas_registradas)
    elif metodo == 3:
        ### Txt
        saidaDeDados = sdd.AdapterDados(sdd.DadosTXT())
        saidaDeDados.salvar_dados(lista.tarefas_registradas)
        ### Json
        saidaDeDados = sdd.AdapterDados(sdd.DadosJson())
        saidaDeDados.salvar_dados(lista.tarefas_registradas)
    else:
                print("Opção Inválida -- Tente Novamente")

def MainProg():
    print("AVALIAÇÃO 3 - LISTA DE TAREFAS")
    while True:
        # Criação da Lista de Tarefas
        listaDeTarefas = lt.ListaDeTarefas()

        textoMenu = "Escolha uma opção:" \
        "\n 1 - LISTAR TAREFAS " \
        "\n 2 - ADICIONAR TAREFA" \
        "\n 3 - REMOVER TAREFA" \
        "\n 4 - ALTERAR STATUS" \
        "\n 5 - SALVAR DADOS" \
        "\n 6 - SAIR"

        print(textoMenu)
        opcao = int(input("Opcão: "))

        if opcao == 6:
            print("Finalizando Programa")
            break
        if opcao == 1:
            # Função de Listar tarefas
            print("Listar Tarefas")
        elif opcao == 2:
            # Função de Adicionar Tarefas
            print(20*"-")
            print("ADIÇÃO DE TAREFA")

            # Input de Info
            tarefaNome = input("Escolha um nome para a Tarefa: ")
            tarefaDescricao = input("Descreva a tarefa: ")

            # Criação e Adição de Tarefa
            tarefa = t.Tarefa(nome=tarefaNome, descricao=tarefaDescricao)
            listaDeTarefas.adicionar_tarefa(tarefa)

            # ID {id} {nome} [{status}] - {descrição}
            print(f"ID {tarefa.id} - {tarefa.nome}[{tarefa.status}]: {tarefa.descricao}")
        elif opcao == 3:
            # Função de Remover Tarefa
            print("REMOÇÃO DE TAREFA")
        elif opcao == 4:
            print("ALTERAÇÃO DE STATUS")
        elif opcao == 5:
            print("SALVAMENTO DE DADOS")

            metodo = int(input("Escolha uma opção de Salvamento: \n" \
            "1 - TXT \n" \
            "2 - JSON \n" \
            "3 - Ambos \n" \
            "Opção: "))

            Salvamento(lista=listaDeTarefas, metodo=metodo)
            
                
    # MENSAGEM DE SAÍDA
    print("Obrigada por Utilizar a Lista de Tarefas!")
    print("FIM")

MainProg()

