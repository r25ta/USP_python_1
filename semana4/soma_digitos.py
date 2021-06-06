def main():
    print("Calcular a soma dos digitos")
    n = int(input("Digite um número inteiro:"))
    cont=0
    d = n
    soma = 0
    while(cont<len(str(n))):
        r = d % 10    
        d = d // 10
        soma = soma + r
        cont = cont + 1
    
    print(soma)
    
main()