class DadosTXT:
    def salvar_dados_TXT(self, dados):
        print("Salvando em TXT")
        
        with open("Dados_Lista_de_Tarefas.txt", "w") as arquivoTXT:
            arquivoTXT.write(dados)

class DadosJson:
    def salvar_dados_JSON(dados):
        print("Salvando em JSON")

# Classe que adapta os dados para saída
## Recebe objeto do método de salvamento desejado
class AdapterDados:
    
    def __init__(self, metodo):
        self.metodo = metodo

    def salvar_dados(self, dados):
        if isinstance(self.metodo, DadosTXT):
            self.metodo.salvar_dados_TXT(dados)
        else:
            return self.metodo.salvar_dados_JSON()
        

# txtadapter = AdapterDados(DadosTXT())
# txtadapter.salvar_dados("a")