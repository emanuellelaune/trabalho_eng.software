import Tarefa as t
import ListaDeTarefas as lt
import SaidaDeDados as sdd


# Teste saída de dados
## Criação da lista de Tarefas
listaDeTarefas = lt.ListaDeTarefas()

## Criação de Tarefas
tarefa = t.Tarefa("tarefa1", "descricao")
tarefa2 = t.Tarefa("tarefa2", "descricao")

## Colocando as tarefas na lista de tarefas registradas
listaDeTarefas.tarefas_registradas.append([tarefa.nome, tarefa.descricao, tarefa.status])
listaDeTarefas.tarefas_registradas.append([tarefa2.nome, tarefa2.descricao, tarefa2.status])

## Testando a Saída de Dados
### Txt
saidaDeDados = sdd.AdapterDados(sdd.DadosTXT())
saidaDeDados.salvar_dados(listaDeTarefas.tarefas_registradas)
### Json
saidaDeDados = sdd.AdapterDados(sdd.DadosJson())
saidaDeDados.salvar_dados(listaDeTarefas.tarefas_registradas)