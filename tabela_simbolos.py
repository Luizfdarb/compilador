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
        table_str = "Tabela de Símbolos:\n"
        table_str += "{:<15} {:<15} {:<15} {:<15}\n".format("Identificador", "Tipo", "Linha", "Valor")
        for identificador, token_info in self.tabela.items():
            valor = token_info['valor'] if token_info['valor'] is not None else "N/A"
            table_str += "{:<15} {:<15} {:<15} {:<15}\n".format(identificador, token_info['tipo'], token_info['linha'], valor)
        return table_str