import math
#FUNÇÃO BOOLEANA RESPONSAVEL POR CONSISTIR SE O VALOR CORRESPONDE A UMA HIPOTENUSA.
def é_hipotenusa(n):    
    #CHEGA SE A SOMA DO QUADRADO DOS CATETOS FORMA UMA HIPOTENUSA
    h = math.sqrt(n)    
    if(h//1 == h):
        return True
    
    else:
        return False    

#FUNÇÃO RETORNA LISTA DE HIPOTENUSAS ENCONTRADAS NO RANGE INFORMADO        
def calcular_triangulo(n):
    a=1
    b=1
    i=n
    j=n
    lstHipotenusas=[]
    
    while(i>=1):        
        b=1
        j=n
        while(j>=1):
            #SOMA DO QUADRADOS DOS CATETOS
            h = (a**2 + b**2)
            if(é_hipotenusa(h)):
                #RECUPERA VALOR DA HIPOTENUSA
                h = math.sqrt(h)
                if(h<=n):
                    #ARMAZENA HIPOTENUSA NA LISTA
                    lstHipotenusas.append(h)
                        
            b=b+1
            j=j-1
            
        a=a+1
        i=i-1
        
    return lstHipotenusas

#FUNÇÃO RESPONSÁVEL POR ELIMINAR AS DUPLICIDADES E SOMAR AS HIPOTENUSAS A QTDE DE HIPOTENUSAS DIFERENTES.
def soma_hipotenusas(n):
    lstHipotenusas = []
    #ORDENAR CONTEÚDO DA LISTA RETORNADA PELA FUNÇÃO CALCULAR_TRIANGULO
    lstHipotenusas = sorted(calcular_triangulo(n))
    a = 0
    n=0
    for h in lstHipotenusas:
        #CONSISTÊNCIA PARA EXCLUIR AS DUPLICIDADES E SOMAR APENAS UMA VEZ
        if(a != h):
            a = h
            n = n + h
                
    return int(n)