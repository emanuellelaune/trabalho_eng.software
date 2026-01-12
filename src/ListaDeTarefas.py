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
  
    def adicionar_tarefa(self):
        nome = input("Digite o nome da tarefa: ").strip()
        descricao = input("Digite a descrição da tarefa: ").strip()

        if not nome:
            print(" Nome inválido!")
            return False

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

#metodo para remover tarefa
        def remover_tarefa(self):
        if not self.tarefas_registradas:
            print(" Não há tarefas para remover.")
            return False

        try:
            id_tarefa = int(input("Digite o ID da tarefa que deseja remover: "))

            for tarefa in self.tarefas_registradas:
                if tarefa["id"] == id_tarefa:
                    self.tarefas_registradas.remove(tarefa)
                    print(" Tarefa removida com sucesso!")
                    return True

            print(" ID não encontrado.")
            return False

        except ValueError:
            print(" Digite um número válido.")
            return False
