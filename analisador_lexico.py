from carregar_codigo import carregar_codigo

def carregar_tokens(programa):
    tokens = []
    i = 0  # índice para percorrer o programa

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
            while i < len(programa) and (programa[i].isalnum() or programa[i] == '_'):
                identificador += programa[i]
                i += 1

            if identificador == 'int':
                tokens.append({'tipo': 'INT', 'valor': identificador})
            elif identificador == 'boolean':
                tokens.append({'tipo': 'BOOLEAN', 'valor': identificador})
            elif identificador == 'func':
                tokens.append({'tipo': 'FUNC', 'valor': identificador})
            elif identificador == 'begin':
                tokens.append({'tipo': 'BEGIN', 'valor': identificador})
            elif identificador == 'end':
                tokens.append({'tipo': 'END', 'valor': identificador})
            elif identificador == 'if':
                tokens.append({'tipo': 'IF', 'valor': identificador})
            elif identificador == 'else':
                tokens.append({'tipo': 'ELSE', 'valor': identificador})
            elif identificador == 'while':
                tokens.append({'tipo': 'WHILE', 'valor': identificador})
            elif identificador == 'return':
                tokens.append({'tipo': 'RETURN', 'valor': identificador})
            elif identificador == 'break':
                tokens.append({'tipo': 'BREAK', 'valor': identificador})
            elif identificador == 'continue':
                tokens.append({'tipo': 'CONTINUE', 'valor': identificador})
            elif identificador == 'print':
                tokens.append({'tipo': 'PRINT', 'valor': identificador})
            elif identificador == 'true' or identificador == 'false':
                tokens.append({'tipo': 'BOOLEAN_LITERAL', 'valor': identificador})
            else:
                tokens.append({'tipo': 'IDENTIFICADOR', 'valor': identificador})

        # Números
        elif char.isdigit():
            numero = char
            i += 1
            while i < len(programa) and programa[i].isdigit():
                numero += programa[i]
                i += 1
            tokens.append({'tipo': 'NUMERO', 'valor': numero})

        # Operadores relacionais
        elif char in "=!><":
            operador_relacional = char
            i += 1
            if i < len(programa) and programa[i] == '=':
                operador_relacional += '='
                i += 1
            tokens.append({'tipo': 'OP_RELACIONAL', 'valor': operador_relacional})

        # Operadores aritméticos
        elif char in "+-*/":
            tokens.append({'tipo': 'OP_ARITMETICO', 'valor': char})
            i += 1

        # Outros caracteres especiais
        else:
            tokens.append({'tipo': char, 'valor': char})
            i += 1

    return tokens


