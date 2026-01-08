#método para add tarefa
    def add_tarefa(self, tarefa):
        if not tarefa or tarefa.strip() == "":
            return False

        self.tarefas_registradas.append({
            "nome": tarefa.strip(),
            "status": "pendente"
        })
        return True
 
    # método para remover a tarefa 
    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas_registradas):
            self.tarefas_registradas.pop(indice)
            return True
        return False
