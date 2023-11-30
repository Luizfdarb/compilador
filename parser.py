from analisador_lexico import *

class AnalisadorSintatico:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def analise_sintatica(self):
        try:
            self.programa()
            print("Análise sintática concluída com sucesso!")
        except SyntaxError as e:
            print(e)

    def programa(self):
        self.match('PROGRAMA')
        self.identificador()
        self.match(';')
        self.bloco()
        self.match('.')

    def bloco(self):
        while self.tokens[self.index]['tipo'] in ['INT', 'BOOLEAN', 'FUNC']:
            self.declaracao_variaveis()
        while self.tokens[self.index]['tipo'] == 'FUNC':
            self.declaracao_funcao()
        while self.tokens[self.index]['tipo'] in ['IDENTIFICADOR', 'IF', 'WHILE', 'RETURN', 'BREAK', 'CONTINUE', 'PRINT']:
            self.comando()

    def comando(self):
        if self.tokens[self.index]['tipo'] == 'IDENTIFICADOR':
            self.atribuicao()
        elif self.tokens[self.index]['tipo'] == 'IF':
            self.condicional()
        elif self.tokens[self.index]['tipo'] == 'WHILE':
            self.enquanto()
        elif self.tokens[self.index]['tipo'] == 'RETURN':
            self.comando_retorno()
        elif self.tokens[self.index]['tipo'] in ['BREAK', 'CONTINUE']:
            self.comando_desvio_incondicional()
        elif self.tokens[self.index]['tipo'] == 'PRINT':
            self.escrita()
        else:
            raise SyntaxError("Erro de sintaxe: Comando inválido")

    def declaracao_variaveis(self):
        self.tipo()
        self.identificador()
        while self.tokens[self.index]['tipo'] == ',':
            self.index += 1
            self.identificador()
        self.match(';')

    def declaracao_funcao(self):
        self.match('FUNC')
        self.tipo()
        self.identificador()
        self.match('(')
        if self.tokens[self.index]['tipo'] in ['INT', 'BOOLEAN']:
            self.parametro()
        self.match(')')
        self.bloco_funcao()

    def tipo(self):
        if self.tokens[self.index]['tipo'] in ['INT', 'BOOLEAN']:
            self.index += 1
        else:
            raise SyntaxError("Erro de sintaxe: Tipo inválido")

    def identificador(self):
        if self.tokens[self.index]['tipo'] == 'IDENTIFICADOR':
            self.index += 1
        else:
            raise SyntaxError("Erro de sintaxe: Identificador inválido")

    def parametro(self):
        self.tipo()
        self.identificador()
        while self.tokens[self.index]['tipo'] == ',':
            self.index += 1
            self.tipo()
            self.identificador()

    def bloco_funcao(self):
        if self.tokens[self.index]['tipo'] == 'BEGIN':
            self.index += 1
            self.bloco()
            if self.tokens[self.index]['tipo'] == 'RETURN':
                self.index += 1
                self.expressao()
            self.match('END')
        else:
            raise SyntaxError("Erro de sintaxe: Bloco de função mal formado")

    def expressao(self):
        self.expressao_simples()
        if self.tokens[self.index]['tipo'] in ['==', '!=', '>', '>=', '<', '<=']:
            self.op_relacional()
            self.expressao_simples()

    def expressao_simples(self):
        if self.tokens[self.index]['tipo'] in ['+', '-']:
            self.op_aditivo()
        self.termo()
        while self.tokens[self.index]['tipo'] in ['+', '-']:
            self.op_aditivo()
            self.termo()

    def op_aditivo(self):
        if self.tokens[self.index]['tipo'] in ['+', '-']:
            self.index += 1
        else:
            raise SyntaxError("Erro de sintaxe: Operador aditivo inválido")

    def termo(self):
        self.fator()
        while self.tokens[self.index]['tipo'] in ['*', '/']:
            self.op_multiplicativo()
            self.fator()

    def op_multiplicativo(self):
        if self.tokens[self.index]['tipo'] in ['*', '/']:
            self.index += 1
        else:
            raise SyntaxError("Erro de sintaxe: Operador multiplicativo inválido")

    def fator(self):
        if self.tokens[self.index]['tipo'] == 'IDENTIFICADOR':
            self.identificador()
        elif self.tokens[self.index]['tipo'] == 'NUMERO':
            self.index += 1
        elif self.tokens[self.index]['tipo'] == '(':
            self.index += 1
            self.expressao()
            self.match(')')
        elif self.tokens[self.index]['tipo'] in ['TRUE', 'FALSE']:
            self.index += 1
        elif self.tokens[self.index]['tipo'] == 'NAO':
            self.index += 1
            self.fator()
        else:
            raise SyntaxError("Erro de sintaxe: Fator inválido")

    def op_relacional(self):
        if self.tokens[self.index]['tipo'] in ['==', '!=', '>', '>=', '<', '<=']:
            self.index += 1
        else:
            raise SyntaxError("Erro de sintaxe: Operador relacional inválido")

    def match(self, expected_type):
        if self.tokens[self.index]['tipo'] == expected_type:
            self.index += 1
        else:
            raise SyntaxError(f"Erro de sintaxe: Esperado {expected_type}, mas encontrado {self.tokens[self.index]['tipo']}")

    def condicional(self):
        self.match('IF')
        self.expressao()
        self.match('THEN')
        self.bloco_condicional()
        self.match('ELSE')
        self.bloco_condicional()

    def bloco_condicional(self):
        self.match('BEGIN')
        self.bloco()
        self.match('END')

    def enquanto(self):
        self.match('WHILE')
        self.expressao()
        self.match('DO')
        self.bloco_enquanto()
        self.match('END')

    def bloco_enquanto(self):
        self.match('BEGIN')
        self.bloco()
        self.match('END')

    def comando_retorno(self):
        self.match('RETURN')
        self.expressao()
        self.match(';')

    def comando_desvio_incondicional(self):
        if self.tokens[self.index]['tipo'] in ['BREAK', 'CONTINUE']:
            self.index += 1
        else:
            raise SyntaxError("Erro de sintaxe: Comando de desvio incondicional inválido")

    def escrita(self):
        self.match('PRINT')
        self.match('(')
        self.expressao()
        self.match(')')


# Nome do arquivo contendo o código
codigo = 'codigo.txt'

# Carrega o código de um arquivo TXT
programa_exemplo = carregar_codigo(codigo)

# Obtém os tokens do programa
tokens_encontrados = carregar_tokens(programa_exemplo)

# Crie uma instância do analisador sintático e realize a análise
analisador = AnalisadorSintatico(tokens_encontrados)
analisador.analise_sintatica()
