from analisador_lexico import AnalisadorLexico
from analisador_semantico import AnalisadorSemantico
from analisador_sintatico import *
from tabela_simbolos import *





variaveis_declaradas = []
variaveis_operacoes = []

linha_declaracao = 0;
linha_operacao = 0;

encontrar_igual = False





vetor = ['atribuicao',
         'chamada_funcao',
         'chamada_procedimento',
         'declaracao_funcao',
         'declaracao_procedimento',
         'condicional',
         'declaracao_funcao',
         'declaracao_variavel',
         'enquanto',
         'escrita',
         'operacoes'
         ]

# Carrega arquivo
codigo = "exemplo_codigo/" + vetor[10] + ".txt"

# Carrega o código de um arquivo TXT
programa_exemplo = AnalisadorLexico(codigo)

# Obtém os tokens do programa
tokens_encontrados, tabela_simbolos = programa_exemplo.carregar_tokens()

# print(tabela_simbolos)
for token in tokens_encontrados:
    print(token)

# Crie uma instância do analisador sintático e realize a análise
analisador = AnalisadorSintatico(tokens_encontrados, codigo)
analisador.analise_sintatica()

# Crie uma instância do analisador semântico e realize a análise
analisador_semantico = AnalisadorSemantico(tabela_simbolos, tokens_encontrados)
analisador_semantico.realizar_analise_semantica(tokens_encontrados)


codigo_tres_enderecos = [
    "T1 = 1 + b",
    "T2 = T1 + c",
    "a = T2"
]


for atual, proximo, proximo_do_proximo in zip(tokens_encontrados, tokens_encontrados[1:], tokens_encontrados[2:]):
    print('Atual', atual)
    print('prox', proximo)
    print('prox_prox', proximo_do_proximo)

    if atual['tipo'] == 'IDENTIFICADOR' and proximo['tipo'] == 'OP_RELACIONAL':
        print('entrouuu.....................')
        if proximo_do_proximo['tipo'] == 'NUMERO':
            print('Funcionando ............')





