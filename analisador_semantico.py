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

    def verifica_declaracao_variavel_tipo(self):

        # Percorre os a lista de tokens
        for posicao, token in enumerate(self.tokens):
            # Verifica se a linha começa com 'INT'
            if self.tokens[posicao]['tipo'] == 'INT' and self.tokens[posicao + 1]['tipo'] == 'IDENTIFICADOR':
                # Verifica se a declaração é 'INT A;'
                if self.tokens[posicao + 2]['valor'] == ';':
                    # Verifica se a variavel já foi declarada
                    if self.tabela_simbolos.obter_token(self.tokens[posicao + 1]['valor'])['tipo'] == 'IDENTIFICADOR':
                        self.tabela_simbolos.obter_token(self.tokens[posicao + 1]['valor'])['tipo'] = 'INT'
                    else:
                        print(
                            f"Erro semântico: A Variável '{self.tokens[posicao + 1]['valor']}' na linha {self.tabela_simbolos.obter_token(self.tokens[posicao + 1]['valor'])['linha']} não é 'INT'")

            elif self.tokens[posicao]['tipo'] == 'BOOLEAN' and self.tokens[posicao + 1]['tipo'] == 'IDENTIFICADOR':
                # Verifica se a declaração é 'BOOLEAN A;'
                if self.tokens[posicao + 2]['valor'] == ';':
                    # Verifica se a variavel já foi declarada
                    if self.tabela_simbolos.obter_token(self.tokens[posicao + 1]['valor'])[
                            'tipo'] == 'IDENTIFICADOR':
                        self.tabela_simbolos.obter_token(self.tokens[posicao + 1]['valor'])['tipo'] = 'BOOLEAN'
                    else:
                        print(
                                f"Erro semântico: A Variável '{self.tokens[posicao + 1]['valor']}' na linha {self.tabela_simbolos.obter_token(self.tokens[posicao + 1]['valor'])['linha']} não é 'BOOLEAN'")

    def verifica_atribuicao_variavel(self):

        # Percorre os a lista de tokens
        for posicao, token in enumerate(self.tokens):
           # Se inicio não tiver 'INT' e 'BOOLEAN' e a atribuição for X = 1;
            if self.tokens[posicao - 1]['tipo'] not in ['INT', 'BOOLEAN'] and token['tipo'] == 'IDENTIFICADOR' and self.tokens[posicao + 1]['valor'] == '=' and self.tokens[posicao + 3]['valor'] == ';':
                # se for um valor numerico atribuido
                if self.tokens[posicao + 2]['tipo'] == 'NUMERO':
                    if self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['tipo'] != 'BOOLEAN':
                        # Salva o tipo INT na variavel
                        self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['tipo'] = 'INT'
                        # Salva o do NUMERO na variavel
                        self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['valor'] = self.tokens[posicao + 2]['valor']
                        print("Análise semântica concluída: Atribuição Variaveis INT corretas")
                    else:
                        print(
                            f"Erro semântico: A Variável '{self.tokens[posicao]['valor']}' na linha {self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['linha']} não é 'INT'")

                # se for um valor 'BOOLEAN' atribuido
                elif self.tokens[posicao + 2]['tipo'] == 'BOOLEAN':
                    if self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['tipo'] != 'INT':
                        # Salva o tipo BOOLEAN na variavel
                        self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['tipo'] = 'BOOLEAN'
                        # Salva o valor booleano na variavel
                        self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['valor'] = \
                        self.tokens[posicao + 2]['valor']
                        print("Análise semântica concluída: Atribuição Variaveis BOOLEAN corretas")
                    else:
                        print(
                                f"Erro semântico: A Variável '{self.tokens[posicao]['valor']}' na linha {self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['linha']} não é 'BOOLEAN'")


                # se depois da variável tiver um '=' e depois for 'IDENTIFICADOR'
                elif self.tokens[posicao + 1]['valor'] == '=' and self.tabela_simbolos.obter_token(self.tokens[posicao + 2]['valor'])['tipo'] == 'INT':
                    if self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['tipo'] == self.tabela_simbolos.obter_token(self.tokens[posicao + 2]['valor'])['tipo'] or self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['tipo'] == 'IDENTIFICADOR':
                       # Salva o tipo 'IDENTIFICADOR' na variavel
                        self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['tipo'] = self.tabela_simbolos.obter_token(self.tokens[posicao + 2]['valor'])['tipo']
                        # Salva o valor do 'IDENTIFICADOR' na tabela na variavel
                        self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['valor'] = \
                        self.tabela_simbolos.obter_token(self.tokens[posicao + 2]['valor'])['valor']
                        print("Análise semântica concluída: Atribuição Variaveis IDENTIFICADOR corretas")
                    else:
                        print(
                            f"Erro semântico: A Variável '{self.tokens[posicao + 2]['valor']}' na linha {self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['linha']} não é '{self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['tipo']}'")

                        # se depois da variável tiver um '=' e depois for 'BOOLEAN'
                elif self.tokens[posicao + 1]['valor'] == '=' and self.tabela_simbolos.obter_token(self.tokens[posicao + 2]['valor'])['tipo'] == 'BOOLEAN':

                    if self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['tipo'] == self.tabela_simbolos.obter_token(self.tokens[posicao + 2]['valor'])['tipo'] or self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['tipo'] == 'IDENTIFICADOR':
                        # Salva o tipo 'BOOLEAN' na variavel
                        self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['tipo'] = \
                        self.tabela_simbolos.obter_token(self.tokens[posicao + 2]['valor'])['tipo']
                        # Salva o valor do 'BOOLEAN' na tabela na variavel
                        self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['valor'] = \
                        self.tabela_simbolos.obter_token(self.tokens[posicao + 2]['valor'])['valor']
                        print("Análise semântica concluída: Atribuição Variaveis BOOLEAN corretas")
                    else:
                        print(
                                f"Erro semântico: A Variável '{self.tokens[posicao + 2]['valor']}' na linha {self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['linha']} não é '{self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['tipo']}'")

                elif self.tabela_simbolos.obter_token(self.tokens[posicao + 2]['valor'])['tipo'] == 'IDENTIFICADOR':
                    print(
                            f"Erro semântico: A Variável {self.tokens[posicao + 2]['valor']} na linha {self.tabela_simbolos.obter_token(self.tokens[posicao + 3]['valor'])['linha']} não foi declarada")

    def verifica_atribuicao_variavel_tipada(self):

        # Percorre os a lista de tokens
        for posicao, token in enumerate(self.tokens):
            # Verifica se a atribuição é 'INT a = valor;'
            if self.tokens[posicao]['tipo'] in ['INT', 'BOOLEAN'] and self.tokens[posicao + 1]['tipo'] == 'IDENTIFICADOR' and self.tokens[posicao + 2]['valor'] == '=':
                # Verifica se não ultrapassa o tamanho
                # da lista de tokens
                if posicao + 4 < len(self.tokens):
                    # Verifica se depois do '=' é um valor numerico e se depois vem ';'
                    if self.tokens[posicao + 3]['tipo'] == 'NUMERO' and self.tokens[posicao + 4]['tipo'] == ';':
                        #
                        if self.tabela_simbolos.obter_token(self.tokens[posicao + 1]['valor'])['tipo'] != 'BOOLEAN' and self.tokens[posicao]['tipo'] != 'BOOLEAN':
                            # Salva o do NUMERO na variavel
                            self.tabela_simbolos.obter_token(self.tokens[posicao + 1]['valor'])['valor'] = \
                            self.tokens[posicao + 3]['valor']
                            # Salva o tipo na variavel
                            self.tabela_simbolos.obter_token(self.tokens[posicao + 1]['valor'])['tipo'] = \
                                self.tokens[posicao]['tipo']
                            print("Análise semântica concluída: Atribuição Variaveis INT corretas")
                        else:
                            print(
                                f"Erro semântico: A Variável '{self.tokens[posicao + 1]['valor']}' na linha {self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['linha']} não é 'INT'")

                    # Verifica se depois do '=' é um valor 'BOOLEAN' e se depois vem ';'
                    elif self.tokens[posicao + 3]['tipo'] == 'BOOLEAN' and self.tokens[posicao + 4]['tipo'] == ';':
                        # Verifica se a variavel declarada é INT ou 'IDENTIDADE' e se seu tipo é direfente de 'INT'
                        if self.tabela_simbolos.obter_token(self.tokens[posicao + 1]['valor'])['tipo'] != 'INT' and self.tokens[posicao]['tipo'] != 'INT':
                            # Salva o valor  na variavel
                            self.tabela_simbolos.obter_token(self.tokens[posicao + 1]['valor'])['valor'] = \
                            self.tokens[posicao + 3]['valor']
                            # Salva o Tipo na variavel
                            self.tabela_simbolos.obter_token(self.tokens[posicao + 1]['valor'])['tipo'] = \
                                self.tokens[posicao]['tipo']
                            print("Análise semântica concluída: Atribuição Variaveis BOOLEANAS corretas")
                        else:
                            print(
                                        f"Erro semântico: A Variável '{self.tokens[posicao + 1]['valor']}' na linha {self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['linha']} não é 'BOOLEAN'")
                            # Verifica se depois do '=' é um valor 'BOOLEAN' e se depois vem ';'

                    elif self.tabela_simbolos.obter_token(self.tokens[posicao + 3]['valor'])['tipo'] in ['INT', 'BOOLEAN'] and self.tokens[posicao + 4][
                                'tipo'] == ';':
                            # Verifica se a variavel declarada é INT ou 'IDENTIFICADOR' e se seu tipo é direfente de 'INT'
                            if self.tabela_simbolos.obter_token(self.tokens[posicao + 3]['valor'])['tipo'] == 'INT' and \
                                    self.tokens[posicao]['tipo'] == 'INT':
                                # Salva o valor  na variavel
                                self.tabela_simbolos.obter_token(self.tokens[posicao + 1]['valor'])['valor'] = \
                                    self.tokens[posicao + 3]['valor']
                                # Salva o Tipo na variavel
                                self.tabela_simbolos.obter_token(self.tokens[posicao + 1]['valor'])['tipo'] = \
                                    self.tokens[posicao]['tipo']
                                print("Análise semântica concluída: Atribuição Variaveis corretas")

                                # Verifica se a variavel declarada é INT ou 'IDENTIFICADOR' e se seu tipo é direfente de 'INT'
                            elif self.tabela_simbolos.obter_token(self.tokens[posicao + 1]['valor'])[
                                    'tipo'] != 'INT' and \
                                self.tabela_simbolos.obter_token(self.tokens[posicao + 3]['valor'])[
                                            'tipo'] != 'INT' and \
                                self.tokens[posicao]['tipo'] != 'INT':
                                # Salva o valor  na variavel
                                self.tabela_simbolos.obter_token(self.tokens[posicao + 1]['valor'])['valor'] = \
                                        self.tokens[posicao + 3]['valor']
                                # Salva o Tipo na variavel
                                self.tabela_simbolos.obter_token(self.tokens[posicao + 1]['valor'])['tipo'] = \
                                        self.tokens[posicao]['tipo']
                                print("Análise semântica concluída: Atribuição Variaveis corretas")

                            else:
                                print(
                                    f"Erro semântico: A Variável '{self.tokens[posicao + 3]['valor']}' na linha {self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['linha']} não é 'BOOLEAN'")

                    elif self.tabela_simbolos.obter_token(self.tokens[posicao + 3]['valor'])['tipo'] == 'IDENTIFICADOR':
                        print(
                            f"Erro semântico: A Variável {self.tokens[posicao + 3]['valor']} na linha {self.tabela_simbolos.obter_token(self.tokens[posicao + 3]['valor'])['linha']} não foi declarada")

    def verifica_declararacao_funcao(self):

        # Percorre os a lista de tokens
        for posicao, token in enumerate(self.tokens):
            # Verifica se a atribuição é 'int func funcao(;'
            if self.tokens[posicao]['tipo'] in ['INT', 'BOOLEAN']:
                if self.tokens[posicao + 1]['tipo'] == 'FUNC':
                    if self.tabela_simbolos.obter_token(self.tokens[posicao + 2]['valor'])['tipo'] == 'IDENTIFICADOR':
                        self.tabela_simbolos.obter_token(self.tokens[posicao + 2]['valor'])['tipo'] = self.tokens[posicao]['tipo']

                        self.verifica_return_funcao()
                        self.verifica_tipo_return_funcao(self.tokens[posicao]['valor'])

    def verifica_return_funcao(self):

        # Percorre os a lista de tokens
        for posicao, token in enumerate(self.tokens):
            # Verifica se a atribuição é 'int func funcao(;'
            if self.tokens[posicao]['tipo'] == 'INT':
                # Encontra a Funcao
                if self.tokens[posicao + 1]['tipo'] == 'FUNC':
                    # Percorre a até achar o valor de return
                    for posicao, token in enumerate(self.tokens[posicao:], start=posicao):
                        if self.tokens[posicao]['tipo'] == 'RETURN':
                            # Salva o tipo no RETURN
                            self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['tipo'] = \
                            self.tabela_simbolos.obter_token(self.tokens[posicao + 1]['valor'])['tipo']
                            # Salva o valor da variavel no RETURN
                            self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['valor'] = \
                                self.tokens[posicao + 1]['valor']
                        elif self.tokens[posicao]['tipo'] == 'END':
                            break
            elif self.tokens[posicao]['tipo'] == 'BOOLEAN':
                # Encontra a Funcao
                if self.tokens[posicao + 1]['tipo'] == 'FUNC':
                    # Percorre a até achar o valor de return
                    for posicao, token in enumerate(self.tokens[posicao:], start=posicao):
                        if self.tokens[posicao]['tipo'] == 'RETURN':
                            # Salva o tipo no RETURN
                            self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['tipo'] = \
                            self.tabela_simbolos.obter_token(self.tokens[posicao + 1]['valor'])['tipo']
                            # Salva o valor da variavel no RETURN
                            self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['valor'] = \
                                self.tokens[posicao + 1]['valor']
                        elif self.tokens[posicao]['tipo'] == 'END':
                            break

    def verifica_parametro_declarado_funcao(self):

        # Percorre os a lista de tokens
        for posicao, token in enumerate(self.tokens):
            # Verifica se a atribuição é 'int func funcao(;'
            if self.tokens[posicao]['tipo'] == 'INT':
                # Encontra a Funcao
                if self.tokens[posicao + 1]['tipo'] == 'FUNC':
                    # Encontra o nome da funcao
                    if self.tokens[posicao + 2]['tipo'] == 'IDENTIFICADOR':
                        # Percorre a até achar o valor de return
                        for posicao, token in enumerate(self.tokens[posicao:], start=posicao):

                            if self.tabela_simbolos.obter_token(self.tokens[posicao]['valor'])['tipo'] == 'IDENTIFICADOR':
                                print(
                                    f"Erro semântico: A Variável '{self.tokens[posicao]['valor']}' na linha {self.tokens[posicao]['linha']} não foi declarada")
                            elif self.tokens[posicao]['tipo'] == ')':
                                print("Análise semântica concluída: Variaveis de Funcão declaradas")
                                break


    def verifica_tipo_return_funcao(self, tipo_funcao):
        for identificador, token_info in self.tabela_simbolos.tabela.items():
            valor = token_info['valor']

            if identificador == 'return':
                if self.tabela_simbolos.obter_token(identificador)['tipo'] == 'IDENTIFICADOR':
                    print(
                        f"Erro semântico: Return tem variavel não inicializada na linha {token_info['linha']}")
                elif self.tabela_simbolos.obter_token(identificador)['tipo'] == tipo_funcao.upper():
                    print("Análise semântica concluída: Return com tipos corretos")
                else:
                    print(
                    f"Erro semântico: Return na linha {token_info['linha']} tem tipo incorreto")

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
                f"Erro semântico: Variável não inicializada")




    def verificar_declaracoes(self):
        # Verifica se todas as variáveis foram declaradas
        for identificador, info in self.tabela_simbolos.tabela.items():
            if info['tipo'] == 'IDENTIFICADOR':
                print(f"Aviso: Variável '{identificador}' na linha {info['linha']} foi usada sem ser declarada.")

    def realizar_analise_semantica(self, tokens):
        self.verifica_chamada_programa()
        self.verifica_declaracao_variavel_tipo()
        self.verifica_atribuicao_variavel()
        self.verifica_atribuicao_variavel_tipada()
        self.verifica_declararacao_funcao()

        # self.verifica_chamada_funcao()
        self.verifica_quantidade_parametro_funcao()
        # self.verifica_tipo_parametro_funcao()
        self.verifica_variavel_chamada_condicional()
        self.verifica_variavel_chamada_enquanto()
        self.verifica_declaracao_variavel_operacao()
        print(self.tabela_simbolos)









# Carrega arquivo
codigo = "exemplo_codigo/atribuicao.txt"

# Carrega o código de um arquivo TXT
programa_exemplo = AnalisadorLexico(codigo)

# Obtém os tokens do programa
tokens_encontrados, tabela_simbolos = programa_exemplo.carregar_tokens()

# print(tabela_simbolos)
for token in tokens_encontrados:
    print(token)

#print(tabela_simbolos)


# Crie uma instância do analisador sintático e realize a análise
analisador = AnalisadorSintatico(tokens_encontrados, codigo)
analisador.analise_sintatica()

# Crie uma instância do analisador semântico e realize a análise
analisador_semantico = AnalisadorSemantico(tabela_simbolos, tokens_encontrados)
analisador_semantico.realizar_analise_semantica(tokens_encontrados)