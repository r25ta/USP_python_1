#Exercicio Bhaskara
import math

def calcularDelta(a, b, c):
    return (b ** 2) - (4*a*c)
    
def calcularRaiz(x, a, b, delta):
    if(x == 1):
        raiz = (-(b) - math.sqrt(delta)) / (2*a)
            
    elif(x == 2):
        raiz = (-(b) + math.sqrt(delta)) / (2*a)
    else:
        print("Parametro X incorreto")    

    return raiz

def main():
    print("Equação de 2° grau quadratica")
    a = float(input("Digite o valor de A:"))
    b = float(input("Digite o valor de B:"))
    c = float(input("Digite o valor de C:"))
    
    delta = calcularDelta(a,b,c)
    
    if(delta < 0):
        print("esta equação não possui raízes reais")
    
    elif(delta == 0):
        x = calcularRaiz(1,a,b,delta)
        print("a raiz dupla desta equação é %s" %(x))
        
    else:
        x1= calcularRaiz(1,a,b,delta)
        x2= calcularRaiz(2,a,b,delta)
        if(x1 < x2):
            print("as raízes da equação são %s e %s" %(x1,x2))
        else:
            print("as raízes da equação são %s e %s" %(x2,x1))
main()