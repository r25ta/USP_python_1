def vogal(letra):
    if(letra=="A" or letra=="a" 
       or letra=="E" or letra=="e" 
       or letra=="I" or letra=="i" 
       or letra=="O" or letra=="o" 
       or letra=="U" or letra=="u"):
        return True
    else:
        return False
    
def main():
    print("Detecção de vogal")
    letra = input("Digite um caracter:")
    print(vogal(letra))


main()