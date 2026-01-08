# método para adicionar uma tarefa
def adicionar_tarefa(self, tarefa):
    if not tarefa or tarefa.strip() == "":
        return False

    novo_id = len(self.tarefas_registradas) + 1

    self.tarefas_registradas.append({
        "id": novo_id,
        "nome": tarefa.strip(),
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
