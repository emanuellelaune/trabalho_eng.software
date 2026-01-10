import json

class DadosTXT:
    def salvar_dados_TXT(self, dados):
        print("Salvando em TXT")
        
        with open("Dados_Lista_de_Tarefas.txt", "w", encoding='utf-8') as arquivoTXT:
            arquivoTXT.write(str(dados))

class DadosJson:
    def salvar_dados_JSON(self,dados):
        print("Salvando em JSON")
        # dados: [[nome, descricao, status],[nome, descricao, status], ...]
        # Formatação dos dados para salvar em Json:
        dadosFormatados = {}
        for item in dados:
            dadosFormatados.update({str(item['id']): item})
            

        with open("Dados_Lista_de_Tarefas.json", 'w', encoding='utf-8') as arquivoJson:
            json.dump(dadosFormatados, arquivoJson, ensure_ascii=False, indent=4)

# Classe que adapta os dados para saída
## Recebe objeto do método de salvamento desejado
class AdapterDados:
    
    def __init__(self, metodo):
        self.metodo = metodo

    def salvar_dados(self, dados):
        if isinstance(self.metodo, DadosTXT):
            self.metodo.salvar_dados_TXT(dados)
        else:
            self.metodo.salvar_dados_JSON(dados)
        

# txtadapter = AdapterDados(DadosTXT())
# txtadapter.salvar_dados("a")