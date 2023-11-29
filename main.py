from analisador_lexico import carregar_tokens
from carregar_codigo import carregar_codigo

codigo = 'codigo.txt'

# Carrega o código de um TXT
programa_exemplo = carregar_codigo(codigo)

tokens_encontrados = carregar_tokens(programa_exemplo)

for token in tokens_encontrados:
    print(token)