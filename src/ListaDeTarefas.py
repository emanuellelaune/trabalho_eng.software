class ListaDeTarefas:
    __instance = None

    tarefas_registradas = []

    # Garante que haja somente uma instancia da lista (Aplicação do SINGLETON)
    def __new__(cls):
        if ListaDeTarefas.__instance is None:
            ListaDeTarefas.__instance = super().__new__(cls)
        return ListaDeTarefas.__instance

    # Método para obter a lista
    def get_lista(self):
        return self.tarefas_registradas

    # Método para importar dados para a lista
    # def set_lista(self, dados):
    #     pass


    # Método para adicionar uma tarefa
    def adicionar_tarefa(self, nome, descricao):
       
        novo_id = len(self.tarefas_registradas) + 1

        self.tarefas_registradas.append({
            "id": novo_id,
            "nome": nome,
            "descricao": descricao,
            "status": "pendente"
        })

        print(f"Tarefa adicionada com sucesso!")
        print(f"ID {novo_id} - {nome} [pendente]")
        return True

    # Método para remover uma tarefa
    def remover_tarefa(self, id_tarefa):

        for tarefa in self.tarefas_registradas:
            if tarefa["id"] == id_tarefa:
                self.tarefas_registradas.remove(tarefa)
                print(" Tarefa removida com sucesso!")
                return True

        print(f" Erro: ID {id_tarefa} não encontrado.")
        return False
    
    # Método para alterar o status de uma tarefa
    def alterar_status(self, id_tarefa):
        tarefa_encontrada = None
        for tarefa in self.get_lista():
            if tarefa["id"] == id_tarefa:
                tarefa_encontrada = tarefa
                break
        
        if not tarefa_encontrada:
            print(f" Erro: ID {id_tarefa} não encontrado.")
            return
        
        print("\nNovos status disponíveis:")
        print(" 1 - Pendente")
        print(" 2 - Fazendo")
        print(" 3 - Feita")
        
        opcao_status = int(input("Opção: "))
        status_mapa = {
            1: "pendente",
            2: "fazendo",
            3: "feita"
        }
        
        if opcao_status in status_mapa:
            novo_status = status_mapa[opcao_status]
            tarefa_encontrada["status"] = novo_status
            print(f" Sucesso: Status atualizado para: {novo_status}\n")
        else:
            print(" Erro: Opção inválida!")