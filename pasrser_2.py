from analisador_lexico import *

class AnalisadorSintatico:
    def __init__(self, tokens):
        self.tokens = tokens
        self.posicao = 0

    def analise_sintatica(self):
        try:
            self.programa()
        except Exception as e:
            print(f"{e}")

    def programa(self):
        self.match('PROGRAMA')
        self.identificador()
        self.match(';')
        # self.bloco()

    def identificador(self):
        if self.tokens[self.posicao]['tipo'] == 'IDENTIFICADOR':
            self.avancar()
        else:
            raise SyntaxError("Erro de sintaxe: Identificador inválido")

    def match(self, terminal):
        if self.tokens[self.posicao]['tipo'] == terminal:
            self.avancar()
        else:
            raise SyntaxError(f"Erro de sintaxe: Esperado {terminal}, mas encontrado {self.tokens[self.posicao]['tipo']}")

    def avancar(self):
        if self.posicao < len(self.tokens) - 1:
            self.posicao += 1
        else:
            raise SyntaxError("Compilado")


# Obtém os tokens do programa
tokens_encontrados = carregar_tokens(programa_exemplo)

# Crie uma instância do analisador sintático e realize a análise
analisador = AnalisadorSintatico(tokens_encontrados)
analisador.analise_sintatica()