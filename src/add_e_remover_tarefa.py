class ListaDeTarefas:
    def __init__(self):
        self.tarefas_registradas = []
        self.proximo_id = 1  
    # método para adicionar tarefa
    def add_tarefa(self, nome, descricao):
        if not nome or nome.strip() == "":
            return False

        self.tarefas_registradas.append({
            "id": self.proximo_id,
            "nome": nome.strip(),
            "descricao": descricao.strip(),
            "status": "pendente"
        })

        self.proximo_id += 1
        return True

    # método para remover a tarefa pelo ID
    def remover_tarefa(self, id_tarefa):
        for tarefa in self.tarefas_registradas:
            if tarefa["id"] == id_tarefa:
                self.tarefas_registradas.remove(tarefa)
                return True
        return False


