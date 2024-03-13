from analisador_lexico import AnalisadorLexico

def gerar_codigo_tres_enderecos(tokens):
    codigo_tres_enderecos = []
    temporarios = []
    prox_temporario = 0

    # Função auxiliar para obter um nome de temporário único
    def novo_temporario():
        nonlocal prox_temporario
        temporario = f"t{prox_temporario}"
        prox_temporario += 1
        return temporario

    i = 0
    while i < len(tokens):
        token = tokens[i]

        # Atribuição
        if token['tipo'] == 'IDENTIFICADOR' and tokens[i + 1]['valor'] == '=':
            resultado = token['valor']
            operando = tokens[i + 2]['valor']
            if tokens[i + 2]['tipo'] == 'IDENTIFICADOR' or tokens[i + 2]['tipo'] == 'NUMERO' or tokens[i + 2]['tipo'] == 'BOOLEAN':
                operando = tokens[i + 2]['valor']

            # Operações aritméticas
            if i + 3 < len(tokens) and tokens[i + 3]['tipo'] == 'OP_ARITMETICO':
                operando1 = operando
                operando2 = tokens[i + 4]['valor']
                temporario = novo_temporario()
                codigo_tres_enderecos.append(f"{temporario} = {operando1} {tokens[i + 3]['valor']} {operando2}")
                operando = temporario
                i += 2

            codigo_tres_enderecos.append(f"{resultado} = {operando}")
            i += 3

        # Condicional
        elif token['valor'] == 'if':
            condicao = f"{tokens[i + 1]['valor']} {tokens[i + 2]['valor']} {tokens[i + 3]['valor']}"
            codigo_tres_enderecos.append(f"if {condicao} goto L1")
            i += 4  # Pula para o próximo token após a condição
            codigo_tres_enderecos.append(f"goto L2")
            codigo_tres_enderecos.append(f"L1:")
            while tokens[i]['valor'] != 'begin':
                i += 1
            i += 1

        elif token['valor'] == 'begin':
            while tokens[i]['valor'] != 'end':
                i += 1
            i += 1

        # While
        elif token['valor'] == 'while':
            codigo_tres_enderecos.append(f"L3:")
            condicao = f"{tokens[i + 1]['valor']} {tokens[i + 2]['valor']} {tokens[i + 3]['valor']}"
            codigo_tres_enderecos.append(f"if {condicao} goto L4")
            i += 4  # Pula para o próximo token após a condição
            codigo_tres_enderecos.append(f"goto L5")
            codigo_tres_enderecos.append(f"L4:")
            while tokens[i]['valor'] != 'begin':
                i += 1
            i += 1

        # funcao
        elif token['tipo'] == 'FUNC':
            print('funcooooooo')
            i += 1

        else:
            print(token['tipo'])
            i += 1



    return codigo_tres_enderecos

codigo = "exemplo_codigo.txt"

# Carrega o código de um arquivo TXT
programa_exemplo = AnalisadorLexico(codigo)

# Obtém os tokens do programa
tokens_encontrados, tabela_simbolos = programa_exemplo.carregar_tokens()

# Gera o código de três endereços a partir dos tokens encontrados
codigo = gerar_codigo_tres_enderecos(tokens_encontrados)

# Imprime o código de três endereços gerado
for instrucao in codigo:
    print(instrucao)
    print()  # Adiciona uma linha em branco após cada instrução