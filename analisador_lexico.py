def carregar_tokens(programa):
    # Lista para armazenar os tokens encontrados
    tokens = []
    # Índice para percorrer o programa
    i = 0

    # Loop para percorrer o programa
    while i < len(programa):
        char = programa[i]

        # Ignorar espaços em branco e quebras de linha
        if char.isspace():
            i += 1
            continue

        # Identificadores e palavras-chave
        if char.isalpha() or char == '_':
            identificador = char
            i += 1
            # Continua lendo enquanto o caractere atual é alfanumérico ou '_'
            while i < len(programa) and (programa[i].isalnum() or programa[i] == '_'):
                identificador += programa[i]
                i += 1

            # Verifica se é uma palavra-chave ou identificador e adiciona ao token
            palavras_chave = ['programa', 'int', 'boolean', 'begin', 'end',
                              'return', 'if', 'else', 'while', 'break', 'continue', 'print']
            if identificador in palavras_chave:
                tokens.append(
                    {'tipo': identificador.upper(), 'valor': identificador})
            else:
                tokens.append(
                    {'tipo': 'IDENTIFICADOR', 'valor': identificador})

        # Números
        elif char.isdigit():
            numero = char
            i += 1
            # Continua lendo enquanto o caractere atual é um dígito
            while i < len(programa) and programa[i].isdigit():
                numero += programa[i]
                i += 1
            # Adiciona o número ao token
            tokens.append({'tipo': 'NUMERO', 'valor': numero})

        # Operadores relacionais
        elif char in "=!><":
            operador_relacional = char
            i += 1
            # Se o próximo caractere for '=', adiciona ao operador
            if i < len(programa) and programa[i] == '=':
                operador_relacional += '='
                i += 1
            # Adiciona o operador ao token
            tokens.append({'tipo': 'OP_RELACIONAL',
                          'valor': operador_relacional})

        # Operadores aritméticos
        elif char in "+-*/":
            # Adiciona o operador aritmético ao token
            tokens.append({'tipo': 'OP_ARITMETICO', 'valor': char})
            i += 1

        # Outros caracteres especiais
        else:
            # Adiciona o caractere especial ao token
            tokens.append({'tipo': char, 'valor': char})
            i += 1

    # Retorna a lista de tokens encontrados
    return tokens


def carregar_codigo(codigo):
    # Lê o conteúdo do arquivo TXT que contém o código
    with open(codigo, 'r') as arquivo:
        linha = arquivo.read()
        return linha


# Nome do arquivo contendo o código
codigo = 'codigo.txt'

# Carrega o código de um arquivo TXT
programa_exemplo = carregar_codigo(codigo)

# Obtém os tokens do programa
tokens_encontrados = carregar_tokens(programa_exemplo)

# Exibe os tokens encontrados
for token in tokens_encontrados:
    print(token)