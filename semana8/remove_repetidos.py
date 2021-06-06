def remove_repetidos(numeros):
    lst = []
    repetido=-99;
    for i in sorted(numeros):
        if(repetido!=i):
            repetido = i
            lst.append(i)
    
    return lst
#FUNÇÃO DE TESTE, RETIRAR QUANDO SUBMETER PARA CORREÇÃO
def main():
    numeros = remove_repetidos([2, 4, 2, 2, 3, 3, 1,0,-1,4,3,9,-3,0,1,3,4,5,6])
    print(numeros)
main()