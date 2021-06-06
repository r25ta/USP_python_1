def inverter(numeros):
    x = 1
    for i in range(len(numeros)):
        if(i!=0):
            print(numeros[-x])
        
        x = x + 1
        
        
def main():
    n=1
    i=0
    
    lst=[]
    while(n>0):
        n = int(input("Digite um número: "))
        lst.insert(i,n)
        i=i+1

    inverter(lst)

main()        