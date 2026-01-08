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
    def __init__(self, nome, status=Status.DISPONIVEL):
        self.nome = nome
        self.status = status
        
        self._estrategias = {
            Status.DISPONIVEL: regra_disponivel,
            Status.FAZENDO: regra_fazendo,
            Status.FEITA: regra_feita
        }

    def mudar_para(self, novo_status):
        validar_transicao = self._estrategias.get(novo_status)
        
        if validar_transicao and validar_transicao(self.status):
            print(f"[{self.nome}] Status atualizado: {self.status.value} -> {novo_status.value}")
            self.status = novo_status
        else:
            print(f"[{self.nome}] Erro: Não é permitido mudar de {self.status.value} para {novo_status.value}")

if __name__ == "__main__":
    t = Tarefa("Refatorar código")
    
    t.mudar_para(Status.FEITA)   # Falha (Strategy bloqueia)
    t.mudar_para(Status.FAZENDO) # Sucesso
    t.mudar_para(Status.FEITA)   # Sucesso
