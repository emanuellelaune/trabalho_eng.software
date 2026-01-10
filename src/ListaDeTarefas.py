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

    # Método para definir os dados da lista
    ## Aplicar o ADAPTER por aqui
    def set_lista(self, dados):
        pass


    # método para adicionar uma tarefa
    def adicionar_tarefa(self, tarefa):
        if not tarefa or tarefa.nome == "":
            return False

        novo_id = len(self.tarefas_registradas) + 1

        self.tarefas_registradas.append({
            "id": novo_id,
            "nome": tarefa.nome,
            "status": "pendente"
        })
        return True


    # método para remover uma tarefa pelo ID
    def remover_tarefa(self, id_tarefa):
        for tarefa in self.tarefas_registradas:
            if tarefa["id"] == id_tarefa:
                self.tarefas_registradas.remove(tarefa)
                return True
        return False