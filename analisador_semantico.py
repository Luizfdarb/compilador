from analisador_lexico import AnalisadorLexico
from analisador_sintatico import *
from tabela_simbolos import *

class AnalisadorSemantico:
    def __init__(self, tabela_simbolos, tokens):
        self.tabela_simbolos = tabela_simbolos
        self.tokens = tokens

    def verifica_chamada_programa(self):
        for token in self.tokens:
            if self.tokens[0]['valor'] == 'programa':
                if self.tokens[1]['tipo'] == 'IDENTIFICADOR':
                    # Atualiza o valor da tabela de Símbolos
                    for identificador, info in tabela_simbolos.tabela.items():
                        if identificador == 'programa':
                            # Atribuímos ao programa
                            # O que foi passado pelo usuário
                            info['valor'] = self.tokens[1]['valor']
                    print("Análise semântica concluída: Estrutura básica do programa está correta.")
                    break
                else:
                    print(f"Erro semântico: Esperado um identificador na linha {self.tokens[0]['linha']}.")
                    break
            else:
                print(
                    f"Erro semântico: O programa deve começar com a palavra-chave  seguida por um identificador linha {self.tokens[0]['linha']}.")
                break

    def verifica_declaracao_variavel(self):

        # Função de Python que intera com o vetor
        # para captura valores proximo do vetor
        iterador = iter(self.tokens)

        # Inicializando a variável do elemento anterior
        anterior = next(iterador)

        # Loop para acessar cada elemento e seu próximo elemento consecutivo
        for atual, proximo, proximo_do_proximo in zip(self.tokens, self.tokens[1:], self.tokens[2:]):
            if atual['tipo'] == 'IDENTIFICADOR' and proximo['tipo'] == 'OP_RELACIONAL':
                if proximo_do_proximo['tipo'] == 'NUMERO':
                    # Atualiza o valor da tabela de Símbolos
                    for identificador, info in tabela_simbolos.tabela.items():
                        if identificador == atual['valor']:
                            # Atribui o valor INTEIRO a variável
                            info['valor'] = proximo_do_proximo['valor']

                elif proximo_do_proximo['tipo'] == 'IDENTIFICADOR':
                    # Atualiza o valor da tabela de Símbolos
                    for identificador, info in tabela_simbolos.tabela.items():
                        if identificador == atual['valor']:
                            # Atribui o valor INTEIRO a variável
                            info['valor'] = proximo_do_proximo['valor']

                elif proximo_do_proximo['tipo'] == 'BOOLEAN':
                    # Atualiza o valor da tabela de Símbolos
                    for identificador, info in tabela_simbolos.tabela.items():
                        if identificador == atual['valor']:
                            # Atribui o valor INTEIRO a variável
                            info['valor'] = proximo_do_proximo['valor']
                    print("Análise semântica concluída: Variaveis corretas")

                else:
                    print(
                        f"Erro semântico: É esperado uma Variável, INT ou BOOLEAN, foi passado '{proximo_do_proximo['valor']}' na linha  {atual['linha']}")
                    break
        print(tabela_simbolos)

    def verifica_tipagem_variavel(self):

        # Função de Python que intera com o vetor
        # para captura valores proximo do vetor
        iterador = iter(self.tokens)

        # Inicializando a variável do elemento anterior
        anterior = next(iterador)

        # Loop para acessar cada elemento e seu próximo elemento consecutivo
        for atual, proximo, proximo_do_proximo in zip(self.tokens, self.tokens[1:], self.tokens[2:]):
            if atual['tipo'] == 'INT':
                if proximo['tipo'] == 'IDENTIFICADOR':
                        print("Análise semântica concluída: Variaveis corretas")
                        break
                elif proximo['tipo'] == 'FUNC':
                        print("Análise semântica concluída: Variaveis corretas")
                        break
                else:
                    print(
                        f"Erro semântico: É esperado uma Variável e foi passado '{proximo['valor']}' na linha  {atual['linha']}")
                    break

    def verifica_chamada_funcao(self):
        # Função de Python que intera com o vetor
        # para captura valores proximo do vetor
        iterador = iter(self.tokens)

        # Pega cada elemento e seu próximo elemento consecutivo
        for atual, proximo, proximo_do_proximo in zip(self.tokens, self.tokens[1:], self.tokens[2:]):
            if atual['tipo'] == 'FUNC':
                if proximo['tipo'] == 'IDENTIFICADOR':
                    contador = 0
                    for token in self.tokens:
                        if token.get('valor') == proximo['valor']:
                            contador += 1
                    if contador > 1:
                        print("Análise semântica concluída: Funçoes corretas")

                    else:
                        print(
                        f"Erro semântico: Erro chamada de Função, ela não foi declarada")
                        break

    def verifica_quantidade_parametro_funcao(self):

        quantidade_virgula_declaracao = 0;
        quantidade_virgula_chamada= 0;
        linha_declaracao = 0;
        linha_chamada = 0;

        # Loop para acessar cada elemento e seu próximo elemento consecutivo
        for atual, proximo, proximo_do_proximo in zip(self.tokens, self.tokens[1:], self.tokens[2:]):
            if atual['tipo'] == 'FUNC':
                if proximo['tipo'] == 'IDENTIFICADOR':
                    for token in self.tokens:
                        if token.get('valor') == proximo['valor']:
                            # Encontro as linhas que das funções
                            if linha_declaracao == linha_chamada:
                                linha_declaracao = token.get('linha')
                            else:
                                linha_chamada = token.get('linha')
        # Faço um for para contar quantas vírgulas tem
        # em cada linha, da declaração e da chamada
        for token in self.tokens:
            if token['linha'] == linha_declaracao:
                if token['valor'] == ',':
                    quantidade_virgula_declaracao += 1
            elif token['linha'] == linha_chamada:
                if token['valor'] == ',':
                    quantidade_virgula_chamada += 1

        # Se os valores forem iguais, a mesma quantidade de parametro
        if quantidade_virgula_declaracao == quantidade_virgula_chamada:
            print("Análise semântica concluída: Funçoes corretas")
        else:
            print(
                f"Erro semântico: Erro chamada de Função, quantidade de parâmentro errada")

    def verifica_tipo_parametro_funcao(self):

        # Vou usar para salvar todos os tipos
        # em dois vetores
        tipos_declaracao = []
        tipos_chamada = []

        linha_declaracao = 0;
        linha_chamada = 0;

        # Loop para acessar cada elemento e seu próximo elemento consecutivo
        for atual, proximo, proximo_do_proximo in zip(self.tokens, self.tokens[1:], self.tokens[2:]):
            if atual['tipo'] == 'FUNC':
                if proximo['tipo'] == 'IDENTIFICADOR':
                    for token in self.tokens:
                        if token.get('valor') == proximo['valor']:
                            # Encontro as linhas que das funções
                            if linha_declaracao == linha_chamada:
                                linha_declaracao = token.get('linha')
                            else:
                                linha_chamada = token.get('linha')
        # Faço um for para contar quantas vírgulas tem
        # em cada linha, da declaração e da chamada
        for token in self.tokens:
            if token['linha'] == linha_declaracao:
                if token['tipo'] in ['INT', 'BOOLEAN']:
                    tipos_declaracao.append(token['tipo'])
            elif token['linha'] == linha_chamada:
                if token['tipo'] in ['INT', 'BOOLEAN']:
                    tipos_chamada.append(token['tipo'])

        # Removo o primeiro iten do vetor
        # ja que a função sempre recebe um
        # tipo
        if len(tipos_declaracao) > 0:
            tipos_declaracao.pop(0)

            # Se os valores forem iguais, a mesma quantidade de parametro
        if tipos_declaracao == tipos_chamada:
            print("Análise semântica concluída: Funçoes corretas")
        else:
            print(
                f"Erro semântico: Erro chamada de Função, tipos de parâmentro errada")


    def verifica_variavel_chamada_condicional(self):

        # Vou usar para salvar  as variaveis declarada
        variaveis_declaradas = []
        variaveis_if = []

        linha_declaracao = 0;
        linha_if = 0;

        for token in self.tokens:
            # Procuro o IF no código
            if token.get('tipo') == 'IF':

                # Salvo a linha que o IF está
                linha_if = token['linha']
                for linha in self.tokens:
                    # Procuro na linha do IF
                    if linha.get('linha') == linha_if:
                        # Variaveis presentes nessa linha
                        if linha.get('tipo') == 'IDENTIFICADOR':
                            # Se achou encontro o retorno
                            variaveis_if.append(linha['valor'])

                            while linha_declaracao < linha_if:
                                for token in self.tokens:
                                    if token.get('linha') == linha_declaracao:
                                        # Variaveis presentes nessa linha
                                        if token.get('tipo') == 'IDENTIFICADOR':
                                            # Se achou encontro o retorno
                                            variaveis_declaradas.append(token['valor'])
                                linha_declaracao += 1

        # Removo o primeiro iten do vetor
        # já que o nome do programa sempre
        # entrará na conta
        if len(variaveis_declaradas) > 0:
            variaveis_declaradas.pop(0)

           # Se os valores forem iguais, a mesma quantidade de parametro
        if variaveis_declaradas == variaveis_if:
            print("Análise semântica concluída: Condicional correto")
        else:
            print(
                f"Erro semântico: Erro no Condicional, variável não inicializada")


    def verifica_variavel_chamada_enquanto(self):

        # Vou usar para salvar  as variaveis declarada
        variaveis_declaradas = []
        variaveis_while = []

        linha_declaracao = 0;
        linha_while = 0;

        for token in self.tokens:
            # Procuro o WHILE no código
            if token.get('tipo') == 'WHILE':

                # Salvo a linha que o WHILE está
                linha_while = token['linha']
                for linha in self.tokens:
                    # Procuro na linha do WHILE
                    if linha.get('linha') == linha_while:
                        # Variaveis presentes nessa linha
                        if linha.get('tipo') == 'IDENTIFICADOR':
                            # Se achou encontro o retorno
                            variaveis_while.append(linha['valor'])

                            while linha_declaracao < linha_while:
                                for token in self.tokens:
                                    if token.get('linha') == linha_declaracao:
                                        # Variaveis presentes nessa linha
                                        if token.get('tipo') == 'IDENTIFICADOR':
                                            # Se achou encontro o retorno
                                            variaveis_declaradas.append(token['valor'])
                                linha_declaracao += 1

        # Removo o primeiro iten do vetor
        # já que o nome do programa sempre
        # entrará na conta
        if len(variaveis_declaradas) > 0:
            variaveis_declaradas.pop(0)

           # Se os valores forem iguais, a mesma quantidade de parametro
        if variaveis_declaradas == variaveis_while:
            print("Análise semântica concluída: Enquanto correto")
        else:
            print(
                f"Erro semântico: Erro no Enquanto, variável não inicializada")

    def verifica_declaracao_variavel_operacao(self):

        # Vou usar para salvar  as variaveis declarada
        variaveis_declaradas = []
        variaveis_operacoes = []

        linha_declaracao = 0;
        linha_operacao = 0;

        encontrar_igual = False

        # Pega cada elemento e seu próximo elemento consecutivo
        for atual, proximo, proximo_do_proximo in zip(self.tokens, self.tokens[1:], self.tokens[2:]):
            if atual['tipo'] == 'IDENTIFICADOR':
                if proximo['valor'] == '=':
                    # Encontro a linha do '='
                    linha_operacao = proximo['linha']

        for linha in self.tokens:
            # Procuro na linha do '='
            if linha.get('linha') == linha_operacao:

                # Estratégia para pegar os valores depois do '='
                if linha.get('valor') == '=':
                    encontrar_igual = True
                # Variaveis presentes nessa linha
                elif linha.get('tipo') == 'IDENTIFICADOR' and encontrar_igual:
                    # Se achou encontro o retorno
                    variaveis_operacoes.append(linha['valor'])

                    # Captura todas as variaveis declaradas antes do '='
                    while linha_declaracao < linha_operacao:
                        for token in self.tokens:
                            if token.get('linha') == linha_declaracao:
                                if token.get('tipo') == 'IDENTIFICADOR':
                                    # Se achou encontro o retorno
                                    variaveis_declaradas.append(token['valor'])
                                    variaveis_declaradas = list(set(variaveis_declaradas))
                        linha_declaracao += 1


        # Vejo se as variaveis as operações estão no vetor da declaradas
        todas_declaradas = set(variaveis_operacoes) & set(variaveis_declaradas)

        if len(todas_declaradas) == len(variaveis_operacoes):
            print("Análise semântica concluída: Operacões estão corretas")
        else:
            print(
                f"Erro semântico: Erro na Operacao, variável não inicializada")




    def verificar_declaracoes(self):
        # Verifica se todas as variáveis foram declaradas
        for identificador, info in self.tabela_simbolos.tabela.items():
            if info['tipo'] == 'IDENTIFICADOR':
                print(f"Aviso: Variável '{identificador}' na linha {info['linha']} foi usada sem ser declarada.")

    def realizar_analise_semantica(self, tokens):
        self.verifica_chamada_programa()
        self.verifica_declaracao_variavel()
        self.verifica_tipagem_variavel()
        self.verifica_chamada_funcao()
        self.verifica_quantidade_parametro_funcao()
        self.verifica_tipo_parametro_funcao()
        self.verifica_variavel_chamada_condicional()
        self.verifica_variavel_chamada_enquanto()
        self.verifica_declaracao_variavel_operacao()








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
codigo = "exemplo_codigo/" + vetor[0]+ ".txt"

# Carrega o código de um arquivo TXT
programa_exemplo = AnalisadorLexico(codigo)

# Obtém os tokens do programa
tokens_encontrados, tabela_simbolos = programa_exemplo.carregar_tokens()

# print(tabela_simbolos)
for token in tokens_encontrados:
    print(token)

print(tabela_simbolos)


# Crie uma instância do analisador sintático e realize a análise
analisador = AnalisadorSintatico(tokens_encontrados, codigo)
analisador.analise_sintatica()

# Crie uma instância do analisador semântico e realize a análise
analisador_semantico = AnalisadorSemantico(tabela_simbolos, tokens_encontrados)
analisador_semantico.realizar_analise_semantica(tokens_encontrados)