from analisador_lexico import AnalisadorLexico


def gerar_codigo_tres_enderecos(tokens):
    codigo_tres_enderecos = []
    temporarios = []
    prox_temporario = 0
    prox_rotulo = 1  # Variável para controlar os rótulos

    # Função auxiliar para obter um nome de temporário único
    def novo_temporario():
        nonlocal prox_temporario
        temporario = f"t{prox_temporario}"
        prox_temporario += 1
        return temporario

    # Função auxiliar para obter um rótulo único
    def novo_rotulo():
        nonlocal prox_rotulo
        rotulo = f"L{prox_rotulo}"
        prox_rotulo += 1
        return rotulo

    i = 0
    linha_atual = 1  # Variável para rastrear a linha atual
    while i < len(tokens):
        token = tokens[i]

        # Atribuição
        if token['tipo'] == 'IDENTIFICADOR' and tokens[i + 1]['valor'] == '=':
            resultado = token['valor']
            operando = tokens[i + 2]['valor']
            if tokens[i + 2]['tipo'] == 'IDENTIFICADOR' or tokens[i + 2]['tipo'] == 'NUMERO' or tokens[i + 2]['tipo'] == 'BOOLEAN':
                operando = tokens[i + 2]['valor']
            else:
                # Trate outros tipos de operando aqui (por exemplo, strings)
                pass

            # Operações aritméticas
            if i + 3 < len(tokens) and tokens[i + 3]['tipo'] == 'OP_ARITMETICO':
                operando1 = operando
                operando2 = tokens[i + 4]['valor']
                temporario = novo_temporario()
                codigo_tres_enderecos.append(
                    f"{linha_atual}: {temporario} = {operando1} {tokens[i + 3]['valor']} {operando2}")
                linha_atual += 1
                operando = temporario
                i += 2

            codigo_tres_enderecos.append(
                f"{linha_atual}: {resultado} = {operando}")
            linha_atual += 1
            i += 3

        # Condicional
        elif token['valor'] == 'if':
            condicao = f"{tokens[i + 1]['valor']} {tokens[i + 2]['valor']} {tokens[i + 3]['valor']}"
            rotulo_else = novo_rotulo()
            rotulo_fim = novo_rotulo()
            codigo_tres_enderecos.append(
                f"{linha_atual}: if {condicao} goto {rotulo_else}")
            codigo_tres_enderecos.append(f"goto {rotulo_fim}")
            codigo_tres_enderecos.append(f"{rotulo_else}:")
            i += 4  # Pula para o próximo token após a condição
            while tokens[i]['valor'] != 'else' and tokens[i]['valor'] != 'end':
                i += 1
            if tokens[i]['valor'] == 'else':
                i += 1
                while tokens[i]['valor'] != 'end':
                    i += 1
            codigo_tres_enderecos.append(f"{rotulo_fim}:")
            linha_atual += 3

        # While
        elif token['valor'] == 'while':
            rotulo_inicio = novo_rotulo()
            rotulo_fim = novo_rotulo()
            condicao = f"{tokens[i + 1]['valor']} {tokens[i + 2]['valor']} {tokens[i + 3]['valor']}"
            codigo_tres_enderecos.append(f"{linha_atual}:")
            codigo_tres_enderecos.append(f"if {condicao} goto {rotulo_fim}")
            codigo_tres_enderecos.append(f"goto {rotulo_inicio}")
            codigo_tres_enderecos.append(f"{rotulo_fim}:")
            i += 4  # Pula para o próximo token após a condição
            while tokens[i]['valor'] != 'begin':
                i += 1
            i += 1
            linha_atual += 4

        # Print
        elif token['valor'] == 'print':
            codigo_tres_enderecos.append(f"print({tokens[i + 2]['valor']})")
            i += 3

        # Declaração de procedimento
        elif token['valor'] == 'declaracao_procedimento':
            codigo_tres_enderecos.append(f"{tokens[i + 1]['valor']}:")
            while tokens[i]['valor'] != 'end':
                i += 1
            i += 1

        # Chamada de procedimento
        elif token['valor'] == 'chamada_procedimento':
            codigo_tres_enderecos.append(f"call {tokens[i + 1]['valor']}")
            i += 2

        # Declaração de função
        elif token['valor'] == 'declaracao_funcao':
            codigo_tres_enderecos.append(f"{tokens[i + 1]['valor']}:")
            while tokens[i]['valor'] != 'end':
                i += 1
            i += 1

        # Chamada de função
        elif token['valor'] == 'chamada_funcao':
            codigo_tres_enderecos.append(f"call {tokens[i + 1]['valor']}")
            i += 2

        else:
            i += 1

    return codigo_tres_enderecos


codigo = "exemplo_codigo/atribuicao.txt"

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
