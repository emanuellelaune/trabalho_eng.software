# App "Lista de Tarefas"

## Gerenciamento de Tarefas com Implementação de Design Patterns em Python

![Python](https://img.shields.io/badge/python-3.8+-306998?style=flat&labelColor=FFD43B)

## Início:

### 1. Instalar dependências
Instale as bibliotecas necessárias para o projeto:

```bash
pip install -r requirements.txt
```


## Sobre o projeto
Tem como objetivo implementação eficaz dos estudos aprendidos em sala de aula, é uma atividade focada gerenciar tarefas, permitindo que o usuário de crie, visualize, remova e atualize suas atividades ao longo do progresso.
 Funcionalidades:

Adicionar Tarefa: Cadastro com nome, descrição e status.
Listar Tarefas: Exibição completa das tarefas e seus estados atuais.
Remover Tarefa: Exclusão de itens selecionados.
Alterar Status: Transição entre os estados: Disponível, Fazendo e Feita.

### Padrões de Projeto Utilizados
 1. Singleton: Para garantir 1 só instância da Lista de Tarefas
 2. Adapter: Para adaptaçaõ do metodo de armazenamento (TXT ou JSON)
 3. Strategy:
