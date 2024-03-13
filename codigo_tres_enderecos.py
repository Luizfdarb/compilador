from analisador_lexico import AnalisadorLexico
from analisador_sintatico import *
from analisador_semantico import *
from tabela_simbolos import *

class CodigoTresEnderecos:
    def __init__(self, tokens_encontrados, tabela_simbolos):
        self.codigo = []
        self.tokens = tokens_encontrados
        self.tabela_simbolos = tabela_simbolos
        self.nome_arquivo = "codigo_enderecos.txt"
        self.posicao = 0

    def salvar_codigo_tres_enderecos(self, nome_arquivo):


        with open(nome_arquivo, 'w') as arquivo:
            for posicao, token in enumerate(self.tokens):
                print(posicao)

                # Verifica inicialização de variável
                if self.tokens[posicao]['tipo'] in ['INT', 'BOOLEAN']:
                    if self.tokens[posicao + 1]['tipo'] == 'IDENTIFICADOR':
                        arquivo.write(str(self.tokens[posicao + 1]['valor']) + '\n')



                # Verifica atribuição de variável
                elif self.tokens[posicao]['tipo'] == 'IDENTIFICADOR':
                    if self.tokens[posicao + 1]['valor'] == '=':
                        if self.tokens[posicao + 2]['tipo'] in  ['NUMERO', 'IDENTIFICADOR']:
                            if self.tokens[posicao + 3]['tipo'] == ';':
                                arquivo.write(str(self.tokens[posicao]['valor']) + ' = ' + str(self.tokens[posicao + 2]['valor']) + '\n')
                            # Verifica atribuição de variável
                            elif self.tokens[posicao + 3]['tipo'] == 'OP_ARITMETICO':
                                arquivo.write(str(self.tokens[posicao]['valor']) + ' = ' + str(
                                                self.tokens[posicao + 2]['valor']) + ' ' + str(self.tokens[posicao + 3]['valor']))
                                for posicao, token in enumerate(self.tokens[posicao + 4:], start=posicao + 4):
                                    print(self.tokens[posicao]['valor'])
                                    if self.tokens[posicao]['tipo'] != ';':
                                        arquivo.write(' ' + str(self.tokens[posicao]['valor']))
                                    else:
                                        break

    def carrega_codigo(self):
        self.salvar_codigo_tres_enderecos(self.nome_arquivo)


    def cria_codigo_3_endereco(self):
        self.carrega_codigo()
        for token in self.tokens:
            print(token)




codigo = "exemplo_codigo/escrita.txt"

# Carrega o código de um arquivo TXT
programa_exemplo = AnalisadorLexico(codigo)

# Obtém os tokens do programa
tokens_encontrados, tabela_simbolos = programa_exemplo.carregar_tokens()


# Crie uma instância do analisador sintático e realize a análise
analisador = AnalisadorSintatico(tokens_encontrados, codigo)
analisador.analise_sintatica()

# Crie uma instância do analisador semântico e realize a análise
analisador_semantico = AnalisadorSemantico(tabela_simbolos, tokens_encontrados)
analisador_semantico.realizar_analise_semantica(tokens_encontrados)

codigo_3_enderecos = CodigoTresEnderecos(tokens_encontrados, tabela_simbolos)
codigo_3_enderecos.cria_codigo_3_endereco()