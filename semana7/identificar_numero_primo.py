def is_primo(n):
    if(n==2):
        return True
    
    i = 2
    while(i<= n/2):
        
        if( n % i == 0):
            return False
        
        i = i + 1 
    return True

def main():
    n = 2
    while(n>1):
        n = int(input("Digite número positivo > 1: "))
        if(n > 1):
            if(is_primo(n)):
                print(n," é primo.")
            else:
                print(n," não é primo.")
        else:
            print("Você saiu do programa.")
main()