# App "Lista de Tarefas"

## Gerenciamento de Tarefas com Implementação de Design Patterns em Python

![Python](https://img.shields.io/badge/python-3.8+-306998?style=flat&labelColor=FFD43B)


## Sobre o projeto
Tem como objetivo implementação eficaz dos estudos aprendidos em sala de aula, é uma atividade focada em gerenciar tarefas, permitindo que o usuário de crie, visualize, remova e atualize suas atividades ao longo do progresso.
 Funcionalidades:

Adicionar Tarefa: Cadastro com nome, descrição e status.
Listar Tarefas: Exibição completa das tarefas e seus estados atuais.
Remover Tarefa: Exclusão de itens selecionados.
Alterar Status: Transição entre os estados: Disponível, Fazendo e Feita.

### Padrões de Projeto Utilizados
 1. Singleton: Para garantir 1 só instância da Lista de Tarefas
 2. Adapter: Para adaptaçaõ do metodo de armazenamento (TXT ou JSON)
 3. Strategy:Usado para modelar como a tarefa se comporta ou como ela valida a transição (mudança de status) dependendo do estado em que ela está no momento.

## Funcionamento
Optamos por manter uma main, que é a cabeça do projeto e local em que ocorre a lógica do aplicativo
    
