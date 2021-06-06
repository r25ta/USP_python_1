def main():
    print("Sequencia de números impares")
    n = int(input("Digite o valor de n:"))
    cont=0
    impar=0
    while( n > cont ):
        impar = impar + 1
        if(impar%2==0):
            impar += 1
        print(impar)
        cont = cont + 1
        
main()