def éPrimo(n):
    j = 2
    primo = True
    i = 2
    p = 2
    #Valida se o número é primo
    if(n==2 or n==3 or n==5 or n==7 or n==7 or n==11):
        return n
    else:
        if(n<=12):
                if(n==4):
                    return 2
                elif(n==6):
                    return 3
                elif n==8 or n==9 or n==10:
                    return 7
                else:
                    return 11    
    
            
    while(j<=n):
        if(n!=j):
            if(n%j==0):
                primo = False
        
        j=j+1
        
    if(primo):
        return n
    
    while(i <= n):
        if(i%2!=0) and (i%3!=0) and (i%5!=0) and (i%7!=0) and(i%11!=0):
            if(n!=i):
                p = i
        i=i+1
    
    return p

def maior_primo(n):
    if(n< 2):
        return print("Parametro inválido! Digite um número maior que 2:")
    else:
        return éPrimo(n)
