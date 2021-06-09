import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

#Calcular Tamanho Médio de Palvras
def format_palavras(texto):
    sentencas = separa_sentencas(texto)
    for sentenca in sentencas:
        frases = separa_frases(sentenca)

    for frase in frases:
        palavras = separa_palavras(frase)

    return palavras

def somar_tamanho_palavras(lstPalavras):
    tamanhoPalavra = 0
    for palavra in lstPalavras:
        tamanhoPalavra = tamanhoPalavra + len(palavra)

    return tamanhoPalavra

    
def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    lst_palavras = format_palavras(texto)
    tamanho_palavra = somar_tamanho_palavras(lst_palavras)
    total_palavras_diferente = n_palavras_diferentes(lst_palavras)
    total_palavras_unicas = n_palavras_unicas(lst_palavras)
    
    #TAMANHO MEDIO DE PALAVRAS
    wal_calculado = tamanho_palavra / len(lst_palavras)
    print("wal_calculado: ",wal_calculado)
    
    #TYPE TOKEN
    ttr_calculado = total_palavras_diferente / len(lst_palavras)
    print("ttr_calculado: ",ttr_calculado)
    
    #HAPAX LEGOMANA
    hlr_calculado = total_palavras_unicas / len(lst_palavras)
    print("hlr_calculado: ",hlr_calculado)
    
    #TAMANHO MÉDIO SENTENÇA
    sal_calculado = 0
    #COMPLEXIDADE MÉDIA SENTENÇA
    sac_calculado = 0
    #TAMANHO MÉDIO FRASE
    pal_calculado = 0
    
    return [wal_calculado, ttr_calculado, hlr_calculado, sal_calculado, sac_calculado, pal_calculado]
    
def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass


def main():
    texto="O rato roeu a roupa do rei de roma!"
    
    
    calcula_assinatura(texto)

main()