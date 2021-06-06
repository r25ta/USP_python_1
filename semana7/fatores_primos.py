def calcular(n):
    fator = 2
    multiplicidade = 0
    
    while n > 1:
        while n % fator == 0:
            n = n / fator
            multiplicidade = multiplicidade + 1
        if(multiplicidade!=0):
            print("Fator",fator,"multiplicidade =",multiplicidade)
        
        multiplicidade = 0
        fator = fator + 1    
        
def main():
    n = 2
    while( n > 1 ):
        n = int(input("Digite número positivo > 1: "))
        calcular(n)
        
main()