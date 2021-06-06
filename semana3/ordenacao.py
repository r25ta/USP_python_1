def main():
    print("Programa para ordenar os número")
    numero1 = int(input("Digite o primeiro número:"))
    numero2 = int(input("Digite o segundo número:"))
    numero3 = int(input("Digite o terceiro número:"))
    
    if(numero1 < numero2 < numero3):
    #if((n2>n1) and (n2<n3)):
        print("crescente")
    else:
        print("não está em ordem crescente")
main()