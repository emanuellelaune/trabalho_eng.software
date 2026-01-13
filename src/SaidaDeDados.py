import json
from datetime import datetime
from abc import ABC, abstractmethod


class SalvarStrategy(ABC):
    def salvar(self, dados):
        pass


class SalvarTXT(SalvarStrategy):
    def salvar(self, dados):
        print("Salvando em TXT")

        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        with open("Dados_Lista_de_Tarefas.txt", "w", encoding='utf-8') as arquivoTXT:

            arquivoTXT.write("=" * 60 + "\n")
            arquivoTXT.write(f"LISTA DE TAREFAS\nData: {data_atual}\n")
            arquivoTXT.write("=" * 60 + "\n")

            for i, item in enumerate(dados, 1):
                arquivoTXT.write(f"TAREFA #{i}\n")
                arquivoTXT.write("-" * 60 + "\n")
                arquivoTXT.write(f"ID:          {item['id']}\n")
                arquivoTXT.write(f"Nome:        {item['nome']}\n")
                arquivoTXT.write(f"Descrição:   {item['descricao']}\n")
                arquivoTXT.write(f"Status:      {item['status']}\n")
                arquivoTXT.write("=" * 60 + "\n")

            arquivoTXT.write(f"Total de tarefas: {len(dados)}\n")
            arquivoTXT.write("=" * 60 + "\n")


class SalvarJson(SalvarStrategy):
    def salvar(self, dados):
        print("Salvando em JSON")
        dadosFormatados = {str(item['id']): item for item in dados}
        with open("Dados_Lista_de_Tarefas.json", 'w', encoding='utf-8') as arquivoJson:
            json.dump(dadosFormatados, arquivoJson, ensure_ascii=False, indent=4)


class SalvamentoContext:
    def __init__(self, estrategia: SalvarStrategy):
        self.estrategia = estrategia

    def salvar_dados(self, dados):
        self.estrategia.salvar(dados)


if __name__ == "__main__":
    lista_exemplo = [
        {'id': 1, 'nome': 'Estudo', 'descricao': 'Estudar para prova', 'status': 'feita'},
        {'id': 2, 'nome': 'Almoço', 'descricao': 'Preparar almoço', 'status': 'fazendo'}
    ]

    contexto_txt = SalvamentoContext(SalvarTXT())
    contexto_txt.salvar_dados(lista_exemplo)
