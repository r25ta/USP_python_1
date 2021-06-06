def is_primo(n):
    if(n==2):
        return True
    
    i = 2
    while(i<= n/2):
        
        if( n % i == 0):
            return False
        
        i = i + 1 

    return True
    
def n_primos(n):
    if(n<2):
        print("Informar número inteiro >= 2")
    
    else:
        x = 1
        i = 2
        while(i<=n):
            if(i%2!=0):
                if(is_primo(i)):
                    x = x +1
            i = i+1
        return x