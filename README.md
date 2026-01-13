# App "Lista de Tarefas"

## Gerenciamento de Tarefas com Implementação de Design Patterns em Python

![Python](https://img.shields.io/badge/python-3.8+-306998?style=flat&labelColor=FFD43B)


## Sobre o projeto
Tem como objetivo implementação eficaz dos estudos aprendidos em sala de aula, é uma atividade focada em gerenciar tarefas, permitindo que o usuário de crie, visualize, remova e atualize suas atividades ao longo do progresso.
### Funcionalidades

#### Adicionar Tarefa:
Permite o cadastro de uma nova tarefa informando nome, descrição e status inicial.

#### Listar Tarefas:
Exibe todas as tarefas cadastradas, mostrando seus identificadores e estados atuais.

#### Remover Tarefa:
Possibilita a exclusão de uma tarefa específica a partir do seu ID.

#### Alterar Status:
Permite a transição entre os estados:

1.Disponível

2.Fazendo

3.Feita

### Padrões de Projeto Utilizados: 
 1. Singleton: Para garantir 1 só instância da Lista de Tarefas.
 2. Adapter: Para adaptaçaõ do metodo de armazenamento (TXT ou JSON).
 3. Strategy:Usado para modelar como a tarefa se comporta ou como ela valida a transição (mudança de status) dependendo do estado em que ela está no momento.

## Funcionamento
A função main() é o ponto central da aplicação. Ela é responsável por executar a classe GerenciadorTarefas e iniciar a execução do sistema por meio do método executar(), que controla o fluxo principal do programa e a interação com o usuário pelo terminal.

#### 👥 Equipe 

1.Bárbara Ellen

2.Emanuelle da Silva 

3.Letícia Assunção
