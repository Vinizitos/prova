def contar_palavras(frase):

    frase = frase.lower()

    palavras = frase.split()

    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
           contagem[palavra]+=1

        elif contagem[palavra]==1:
            return contagem