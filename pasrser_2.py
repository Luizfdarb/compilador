from analisador_lexico import *

class AnalisadorSintatico:
    def __init__(self, tokens):
        self.posicao = 0
        self.codigo = codigo
        self.tokens = tokens

    def analise_sintatica(self):
        try:
            self.programa()
        except Exception as e:
            print(f"{e}")

    def programa(self):
        self.match('PROGRAMA')
        self.identificador()
        self.match(';')
        self.bloco()

    def identificador(self):
        if self.tokens[self.posicao]['tipo'] == 'IDENTIFICADOR':
            self.avancar()
        else:
            raise SyntaxError(f"Erro de sintaxe: Identificador inválido \"{self.tokens[self.posicao]['tipo']}\" na linha {self.tokens[self.posicao]['linha']}")

    def match(self, terminal):
        if self.tokens[self.posicao]['tipo'] == terminal:
            self.avancar()
        else:
            raise SyntaxError(f"Erro de sintaxe: Esperado {terminal} na linha {self.tokens[self.posicao]['linha']}, mas encontrado {self.tokens[self.posicao]['tipo']}")

    def bloco(self):
        while self.tokens[self.posicao]['tipo'] in ['INT', 'BOOLEAN']:
            self.declaracao_variaveis()
        # while self.tokens[self.index]['tipo'] in ['IDENTIFICADOR', 'IF', 'WHILE', 'RETURN', 'BREAK', 'CONTINUE', 'PRINT']:
        #     self.comando()

    def declaracao_variaveis(self):
        self.tipo()
        self.identificador()
        self.match(';')

    def tipo(self):
        if self.tokens[self.posicao]['tipo'] in ['INT', 'BOOLEAN']:
            self.avancar()
        else:
            raise SyntaxError(f"Erro de sintaxe: Tipo inválido na linha {self.tokens[self.posicao]['linha']}")

    def declaracao_funcao(self):
        self.match('FUNC')
        self.tipo()
        self.identificador()
        self.match('(')
        if self.tokens[self.index]['tipo'] in ['INT', 'BOOLEAN']:
            self.parametro()
        self.match(')')
        self.bloco_funcao()

    def avancar(self):
        if self.posicao < len(self.tokens) - 1:
            self.posicao += 1
        else:
            raise SyntaxError("Compilado")




# Nome do arquivo contendo o código
codigo = "codigo_2.txt"

# Carrega o código de um arquivo TXT
programa_exemplo = AnalisadorLexico(codigo)

# Obtém os tokens do programa
tokens_encontrados = programa_exemplo.carregar_tokens()


# Crie uma instância do analisador sintático e realize a análise
analisador = AnalisadorSintatico(tokens_encontrados)
analisador.analise_sintatica()