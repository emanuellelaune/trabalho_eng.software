import ListaDeTarefas as lt
import SaidaDeDados as sdd
import estrategias as est


class GerenciadorTarefas:
    
    
    def __init__(self):
        self.lista = lt.ListaDeTarefas()  # Singleton
        self.opcoes = {
            1: self.listar_tarefas,
            2: self.adicionar_tarefa,
            3: self.remover_tarefa,
            4: self.alterar_status,
            5: self.salvar_dados,
            6: self.sair
        }
    
    def exibir_menu(self):
        
        print("\n" + "="*50)
        print("App - LISTA DE TAREFAS")
        print("="*50)
        print(" 1 - LISTAR TAREFAS")
        print(" 2 - ADICIONAR TAREFA")
        print(" 3 - REMOVER TAREFA")
        print(" 4 - ALTERAR STATUS")
        print(" 5 - SALVAR DADOS")
        print(" 6 - SAIR")
        print("="*50)
        
        try:
            return int(input("Opção: "))
        except ValueError:
            print(" Erro: Digite um número válido!")
            return None
    
    def listar_tarefas(self):
        
        print("\n" + "-"*50)
        print("LISTAGEM DE TAREFAS")
        print("-"*50)
        
        if not self.lista.tarefas_registradas:
            print(" Info: Nenhuma tarefa registrada ainda.")
        else:
            for tarefa in self.lista.tarefas_registradas:
                status_label = "Feito" if tarefa["status"] == "feita" else "Em espera"
                print(f"\n[{status_label}] ID {tarefa['id']} - {tarefa['nome']}")
                print(f"   Status: {tarefa['status']}")
                print(f"   Descrição: {tarefa['descricao']}")
        
        print("-"*50)
    
    def adicionar_tarefa(self):
        
        print("\n" + "-"*50)
        print("ADIÇÃO DE TAREFA")
        print("-"*50)
        
        nome = input("Nome da tarefa: ").strip()
        if not nome:
            print(" Erro: Nome não pode estar vazio!")
            return
        
        descricao = input("Descrição da tarefa: ").strip()
        if not descricao:
            print(" Erro: Descrição não pode estar vazia!")
            return
        
        novo_id = len(self.lista.tarefas_registradas) + 1
        self.lista.tarefas_registradas.append({
            "id": novo_id,
            "nome": nome,
            "descricao": descricao,
            "status": "pendente"
        })
        
        print(f"\n Sucesso: Tarefa adicionada!")
        print(f"   ID {novo_id} - {nome} [pendente]")
    
    def remover_tarefa(self):
        
        print("\n" + "-"*50)
        print("REMOÇÃO DE TAREFA")
        print("-"*50)
        
        if not self.lista.tarefas_registradas:
            print(" Erro: Não há tarefas para remover.")
            return
        
        self.listar_tarefas()
        
        try:
            id_tarefa = int(input("\nDigite o ID da tarefa a remover: "))
            
            for tarefa in self.lista.tarefas_registradas:
                if tarefa["id"] == id_tarefa:
                    self.lista.tarefas_registradas.remove(tarefa)
                    print(f" Sucesso: Tarefa {id_tarefa} removida!\n")
                    return
            
            print(f" Erro: ID {id_tarefa} não encontrado.")
        
        except ValueError:
            print(" Erro: Digite um número válido!")
    
    def alterar_status(self):
        
        print("\n" + "-"*50)
        print("ALTERAÇÃO DE STATUS")
        print("-"*50)
        
        if not self.lista.tarefas_registradas:
            print(" Erro: Nenhuma tarefa disponível.")
            return
        
        self.listar_tarefas()
        
        try:
            id_tarefa = int(input("\nDigite o ID da tarefa: "))
            
            tarefa_encontrada = None
            for tarefa in self.lista.tarefas_registradas:
                if tarefa["id"] == id_tarefa:
                    tarefa_encontrada = tarefa
                    break
            
            if not tarefa_encontrada:
                print(f" Erro: ID {id_tarefa} não encontrado.")
                return
            
            print("\nNovos status disponíveis:")
            print(" 1 - Pendente")
            print(" 2 - Fazendo")
            print(" 3 - Feita")
            
            opcao_status = int(input("Opção: "))
            status_mapa = {
                1: "pendente",
                2: "fazendo",
                3: "feita"
            }
            
            if opcao_status in status_mapa:
                novo_status = status_mapa[opcao_status]
                tarefa_encontrada["status"] = novo_status
                print(f" Sucesso: Status atualizado para: {novo_status}\n")
            else:
                print(" Erro: Opção inválida!")
        
        except ValueError:
            print(" Erro: Digite valores válidos!")
    
    def salvar_dados(self):
        """Salva os dados das tarefas nos formatos escolhidos."""
        print("\n" + "-"*50)
        print("SALVAMENTO DE DADOS")
        print("-"*50)
        
        print("\nFormatos disponíveis:")
        print(" 1 - TXT")
        print(" 2 - JSON")
        print(" 3 - Ambos (TXT e JSON)")
        
        try:
            metodo = int(input("Opção: "))
            
            if metodo == 1:
                self._salvar_txt()
            elif metodo == 2:
                self._salvar_json()
            elif metodo == 3:
                self._salvar_txt()
                self._salvar_json()
            else:
                print(" Erro: Opção inválida!")
        
        except ValueError:
            print(" Erro: Digite um número válido!")
    
    def _salvar_txt(self):
        """Salva dados em TXT."""
        try:
            adaptador = sdd.AdapterDados(sdd.DadosTXT())
            adaptador.salvar_dados(self.lista.tarefas_registradas)
            print(" Sucesso: Dados salvos em TXT!")
        except Exception as e:
            print(f" Erro ao salvar TXT: {e}")
    
    def _salvar_json(self):
        """Salva dados em JSON."""
        try:
            adaptador = sdd.AdapterDados(sdd.DadosJson())
            adaptador.salvar_dados(self.lista.tarefas_registradas)
            print(" Sucesso: Dados salvos em JSON!")
        except Exception as e:
            print(f" Erro ao salvar JSON: {e}")
    
    def sair(self):
        """Encerra o programa."""
        print("\n" + "="*50)
        print("Obrigada por utilizar a Lista de Tarefas!")
        print("="*50)
        return True
    
    def executar(self):
        """Loop principal da aplicação."""
        while True:
            opcao = self.exibir_menu()
            
            if opcao in self.opcoes:
                resultado = self.opcoes[opcao]()
                if resultado: 
                    break
            elif opcao is not None:
                print(" Erro: Opção inválida! Tente novamente.")


def main():
    """Função principal que inicia o programa."""
    gerenciador = GerenciadorTarefas()
    gerenciador.executar()


if __name__ == "__main__":
    main()
