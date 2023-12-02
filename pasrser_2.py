from analisador_lexico import *

class AnalisadorSintatico:
    def __init__(self, tokens, codigo):
        self.tokens = tokens
        self.posicao = 0
        self.codigo = codigo

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
            linha = self.carregar_linhas_codigo()
            raise SyntaxError(f"Erro de sintaxe: Identificador inválido \"{self.tokens[self.posicao]['tipo']}\" na linha {linha}")

    def match(self, terminal):
        if self.tokens[self.posicao]['tipo'] == terminal:
            self.avancar()
        else:
            linha = 1
            raise SyntaxError(f"Erro de sintaxe: Esperado {terminal} na linha {linha}, mas encontrado {self.tokens[self.posicao]['tipo']}")

    def bloco(self):
        while self.tokens[self.posicao]['tipo'] in ['INT', 'BOOLEAN', 'FUNC']:
            self.declaracao_variaveis()
        # while self.tokens[self.index]['tipo'] == 'FUNC':
        #     self.declaracao_funcao()
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
            raise SyntaxError("Erro de sintaxe: Tipo inválido")

    def avancar(self):
        if self.posicao < len(self.tokens) - 1:
            self.posicao += 1
        else:
            raise SyntaxError("Compilado")

    def carregar_linhas_codigo(self):
        linhas_codigo = []
        # Ler o txt com o código
        with open(self.codigo, 'r') as arquivo:
            linha = arquivo.read()
            # Remove os espaços do código
            linhas_codigo = linha.replace(' ', '')

            # Salva as linhas de código
            linhas_codigo = linhas_codigo.split()

            linha = 0
            for i in linhas_codigo:
                if i.find(self.tokens[self.posicao]['tipo']) >= 0:
                    break
                linha = linha + 1

        return linha

# Nome do arquivo contendo o código
codigo = "codigo_2.txt"

# Obtém os tokens do programa
tokens_encontrados = carregar_tokens(programa_exemplo)

# Crie uma instância do analisador sintático e realize a análise
analisador = AnalisadorSintatico(tokens_encontrados, codigo)
analisador.analise_sintatica()