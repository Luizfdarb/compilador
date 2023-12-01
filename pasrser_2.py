from analisador_lexico import carregar_codigo, carregar_tokens


def programa(tokens):
    global posicao
    try:
        match(tokens, 'PROGRAMA')
        identificador(tokens)
        match(tokens, ';')
        #bloco()
    except Exception as e:
        print(f"{e}")


def identificador(tokens):
    global posicao
    if tokens[posicao]['tipo'] == 'IDENTIFICADOR':
        # Verifica se é uma posição válida do vetor tokens
        if(posicao < len(tokens) - 1):
            posicao = posicao + 1
        else:
            raise SyntaxError("Compilado")
    else:
        raise SyntaxError("Erro de sintaxe: Identificador inválido")

def match(tokens, terminal):
    global posicao
    if tokens[posicao]['tipo'] == terminal:
        # Verifica se é uma posição válida do vetor tokens
        if (posicao < len(tokens) - 1):
            posicao = posicao + 1
        else:
            raise SyntaxError("Compilado")
    else:
        raise SyntaxError(f"Erro de sintaxe: Esperado {terminal}, mas encontrado {tokens[posicao]['tipo']}")


# Variável global para navegar na lista de tokens
posicao: int = 0

# Nome do arquivo contendo o código
codigo = 'codigo_2.txt'

# Carrega o código de um arquivo TXT
programa_exemplo = carregar_codigo(codigo)

# Obtém os tokens do programa
tokens_encontrados = carregar_tokens(programa_exemplo)

# Crie uma instância do analisador sintático e realize a análise
programa(tokens_encontrados)