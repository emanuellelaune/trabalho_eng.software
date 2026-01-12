from enum import Enum

class Status(Enum):
    DISPONIVEL = "Disponível"
    FAZENDO = "Fazendo"
    FEITA = "Feita"

def regra_disponivel(atual):
    return atual == Status.FAZENDO

def regra_fazendo(atual):
    return atual in [Status.DISPONIVEL, Status.FEITA]

def regra_feita(atual):
    return atual == Status.FAZENDO

class Tarefa:
    def __init__(self, nome, descricao, status=Status.DISPONIVEL):
        self.nome = nome
        self.status = status
        self.descricao = descricao
        
        self._estrategias = {
            Status.DISPONIVEL: regra_disponivel,
            Status.FAZENDO: regra_fazendo,
            Status.FEITA: regra_feita
        }

    def mudar_para(self, novo_status):
        if novo_status == self.status:
            print(f"[{self.nome}] Info: A tarefa já está no status {novo_status.value}")
            return

        validar_transicao = self._estrategias.get(novo_status)
        
        if validar_transicao and validar_transicao(self.status):
            print(f"[{self.nome}] Sucesso: {self.status.value} -> {novo_status.value}")
            self.status = novo_status
        else:
            print(f"[{self.nome}] Erro: Movimentação de {self.status.value} para {novo_status.value} não permitida.")

if __name__ == "__main__":
    t = Tarefa("Refatorar código", "Limpar o Gerenciador")
    
    t.mudar_para(Status.FEITA)    
    t.mudar_para(Status.FAZENDO)  
    t.mudar_para(Status.FEITA)    
