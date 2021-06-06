def fatorial(n):
    fatorial = 1
    while(n>=1):
        fatorial = fatorial * n
        n = n - 1
    print(fatorial)    
    
    
def main():
    is_fatorial = True
    while(is_fatorial):
        n = int(input("Digite um número inteiro positivo, para calcular o fatorial: "))

        fatorial(n)

        str = input("Deseja continuar calculando fatorial (S)im ou (N)ão? ")
    
        while(str!="S" and str!="N"):
            str = input("Opção inválida, digite novamente S ou N " )

        if(str=="S"):
            is_fatorial=True
        else:
            is_fatorial=False
        
main()