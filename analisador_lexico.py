from tabela_simbolos import *

class AnalisadorLexico:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.codigo = self.carregar_codigo()
        self.linhas = self.carregar_linhas()
        self.indice = 0
        self.tokens = []
        self.tabela_simbolos = TabelaSimbolos()

    def carregar_codigo(self):
        # Lê o conteúdo do arquivo TXT que contém o código
        with open(self.arquivo, 'r') as arquivo:
            linha = arquivo.read()
            return linha

    def carregar_linhas(self):
        linhas_codigo = []
        # Ler o txt com o código
        with open(self.arquivo, 'r') as arquivo:
            linha = arquivo.read()
            # Remove os espaços do código
            linhas_codigo = linha.replace(' ', '')

            # Salva as linhas de código
            linhas_codigo = linhas_codigo.split()

        return linhas_codigo

    def carregar_tokens(self):

        # Loop para percorrer o programa
        while self.indice < len(self.codigo):
            char = self.codigo[self.indice]

            # Ignorar espaços em branco e quebras de linha
            if char.isspace():
                self.indice += 1
                continue

            # Comentários
            if char == '#':
                self.indice += 1
                while self.indice < len(self.codigo) and self.codigo[self.indice] != '\n':
                    self.indice += 1
                continue

            # Identificadores e palavras-chave
            if char.isalpha() or char == '_':
                identificador = char
                self.indice += 1
                # Continua lendo enquanto o caractere atual é alfanumérico ou '_'
                while self.indice < len(self.codigo) and (self.codigo[self.indice].isalnum() or self.codigo[self.indice] == '_'):
                    identificador += self.codigo[self.indice]
                    self.indice += 1

                # Verifica se é uma palavra-chave ou identificador e adiciona ao token
                palavras_chave = ['programa', 'int', 'boolean', 'func', 'begin', 'end', 'true', 'false',
                                  'return', 'if', 'else', 'while', 'break', 'continue', 'print']
                if identificador in palavras_chave:
                    for i, string in enumerate(self.linhas):
                        if identificador in string:
                            linha = i + 1
                            self.linhas[i] = string.replace(identificador, '', 1)
                            break

                    if identificador == 'true' or identificador == 'false':
                        self.tokens.append(
                            {'tipo': 'BOOLEAN', 'valor': identificador, 'linha': linha})
                    else:
                        self.tokens.append(
                        {'tipo': identificador.upper(), 'valor': identificador, 'linha': linha})
                else:
                    for i, string in enumerate(self.linhas):
                        if identificador in string:
                            linha = i + 1
                            self.linhas[i] = string.replace(identificador, '', 1)
                            break
                    self.tokens.append(
                        {'tipo': 'IDENTIFICADOR', 'valor': identificador, 'linha': linha})

            # Números
            elif char.isdigit():
                numero = char
                self.indice += 1
                # Continua lendo enquanto o caractere atual é um dígito
                while self.indice < len(self.codigo) and self.codigo[self.indice].isdigit():
                    numero += self.codigo[self.indice]
                    self.indice += 1
                # Percorre o vetor de linhas
                for i, string in enumerate(self.linhas):
                    if char in string:
                        linha = i + 1
                        self.linhas[i] = string.replace(char, '', 1)
                        break
                # Adiciona o número ao token
                self.tokens.append({'tipo': 'NUMERO', 'valor': numero, 'linha': linha})

            # Operadores relacionais
            elif char in "=!><":
                operador_relacional = char
                self.indice += 1
                # Se o próximo caractere for '=', adiciona ao operador
                if self.indice < len(self.codigo) and self.codigo[self.indice] == '=':
                    operador_relacional += '='
                    self.indice += 1

                # Percorre o vetor de linhas
                for i, string in enumerate(self.linhas):
                    if operador_relacional in string:
                        linha = i + 1
                        self.linhas[i] = string.replace(char, '', 1)
                        break
                # Adiciona o operador ao token
                self.tokens.append({'tipo': 'OP_RELACIONAL',
                              'valor': operador_relacional, 'linha': linha})

            # Operadores aritméticos
            elif char in "+-*/":
                # Percorre o vetor de linhas
                for i, string in enumerate(self.linhas):
                    if char in string:
                        linha = i + 1
                        self.linhas[i] = string.replace(char, '', 1)
                        break
                # Adiciona o operador aritmético ao token
                self.tokens.append({'tipo': 'OP_ARITMETICO', 'valor': char, 'linha': linha})
                self.indice += 1

            # Literal de String
            elif char == '"':
                self.indice += 1
                vazio = ''
                while self.indice < len(self.codigo) and self.codigo[self.indice] != '"':
                    string += self.codigo[self.indice]
                    self.indice += 1
                if self.indice < len(self.codigo) and self.codigo[self.indice] == '"':
                    self.indice += 1
                    # Percorre o vetor de linhas
                    for i, string in enumerate(self.linhas):
                        if vazio in string:
                            linha = i + 1
                            self.linhas[i] = string.replace(char, '', 1)
                            break
                    self.tokens.append({'tipo': 'STRING', 'valor': string, 'linha': linha})
                else:
                    # Erro: String não fechada
                    print("Erro: String não fechada")

            # Outros caracteres especiais
            else:
                for i, string in enumerate(self.linhas):
                    if char in string:
                        linha = i + 1
                        self.linhas[i] = string.replace(char, '', 1)
                        break
                # Adiciona o caractere especial ao token
                self.tokens.append({'tipo': char, 'valor': char, 'linha': linha})
                self.indice += 1


        # Imprimindo os valores do dicionário
        for token in self.tokens:

            # Verifica se é uma palavra-chave ou identificador e adiciona ao token
            palavras_reservadas = ['programa', 'int', 'func', 'begin', 'end',
                              'return', 'if', 'else', 'while', 'break', 'continue', 'print']

            # Verifica se é um booleano
            tipos_boolean = ['true', 'false']

            # Adicionando a tabela de Símbolos
            if token['tipo'].lower() in palavras_reservadas:
                self.tabela_simbolos.adicionar_token(token['valor'], 'PALAVRA_CHAVE', token['linha'])
            # Adicionando tokens à tabela
            elif token['tipo'] == 'IDENTIFICADOR':
                self.tabela_simbolos.adicionar_token(token['valor'], token['tipo'], token['linha'])
            elif token['tipo'] == 'NUMERO':
                self.tabela_simbolos.adicionar_token(token['valor'], 'INTEIRO', token['linha'])
            elif token['tipo'] == 'OP_RELACIONAL':
                self.tabela_simbolos.adicionar_token(token['valor'], 'OP_RELACIONAL', token['linha'])
            elif token['tipo'] == 'OP_ARITMETICO':
                self.tabela_simbolos.adicionar_token(token['valor'], 'OP_ARITMETICO', token['linha'])
            elif token['tipo'] == 'STRING':
                self.tabela_simbolos.adicionar_token(token['valor'], 'STRING', token['linha'])
            elif token['tipo'] in ';()':
                self.tabela_simbolos.adicionar_token(token['valor'], 'DELIMITADOR', token['linha'])
            elif token['tipo'] == 'BOOLEAN':
                self.tabela_simbolos.adicionar_token(token['valor'], 'BOOLEAN', token['linha'])

        # Retorna a lista de tokens encontrados
        return self.tokens, self.tabela_simbolos
