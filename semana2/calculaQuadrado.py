#1.  Dada uma seqüência de números inteiros não-nulos, seguida por 0, imprimir seus quadrados.
def main():
    cont = 0
    print("Programa imprime o ouadrado da sequencia")
    print("A sequencia termina com Zero(0)")
    n = int(input("Digite número inteiro:"))
    while n != 0:
        quadrado = n ** 2
        print("Valor do quadrado no número", n,"é",quadrado)
        n = int(input("Digite número inteiro:"))
main()