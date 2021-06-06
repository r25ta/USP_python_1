def main():
    print("Digitos adjacentes")
    n = int(input("Dígite um número inteiro:"))
    
    cont=len(str(n))
    x=-99
    y=0
    while(cont>0):
        
        r = n%10
        n = n//10
        
        if(r!=x):
            x=r
        else:
            y = y+1
        cont = cont -1
        
    if(y>0):
        print("sim")
    else:
        print("não")      
main()