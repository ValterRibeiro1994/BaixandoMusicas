from fuzzywuzzy import fuzz

def checar_nome(escrito, encontrado):
    
    # quebre as strings em listas de palavras
    texto_encontrado = encontrado.split()
    texto_escrito = escrito.split()
    
    # armazena o resultado das palavras que batem com o que esta sendo pesquisado
    resultado = []

    tamanho_texto_escrito = len(set(texto_escrito))

    # para cada palavra dentro do texto texto_escritoo
    for palavra_usuario in texto_escrito:
        # verifico a semelhança  entra a primeira palavra que escrevi, com o texto encontrado...
        for palavra in texto_encontrado:
            semelhanca = fuzz.ratio(palavra_usuario, palavra)
            # se for maior que 70%
            if semelhanca >= 70:
                # adiciona na lista de resultado - garanta que não esteja repetida
                if palavra_usuario not in resultado:
                    resultado.append(palavra_usuario)

            # se o tamanho da lista de resultado for do mesmo tamanho que a do texto escrito
            # afirma que todas as palavras correspondem
            if len(resultado) == tamanho_texto_escrito:
                return True
    return False

if __name__ == "__main__":
    texto_encontrado = 'alter wlter water waler waltr walte  valte walte'
    texto_escrito = 'valter, valti, valtr'
    print(checar_nome(texto_escrito, texto_encontrado))
    print(checar_nome(texto_encontrado, texto_escrito))