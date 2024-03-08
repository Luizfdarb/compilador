class TabelaSimbolos:
    def __init__(self):
        self.tabela = {}

    def adicionar_token(self, identificador, tipo, linha, valor=None):
        self.tabela[identificador] = {
            'tipo': tipo,
            'linha': linha,
            'valor': valor
        }

    def obter_token(self, identificador):
        return self.tabela.get(identificador)

    def __str__(self):
        return str(self.tabela)

