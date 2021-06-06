def draw_retangulo_vazado(l,a):
    x = 0
    y = a
    while(y > 0):
        x = l
        while(x > 0):
            if(a/y==1):
                print("#",end="")
                
            elif(a*y==a):
                print("#",end="")
            else:
                if(x==l):
                    print("#",end="")
                    
                elif(x==1):
                    print("#",end="")
                    
                else:
                    print(" ",end="")  
            x = x -1
        print(end="\n")
        y = y - 1

def main():
    l = int(input("digite a largura: "))
    a = int(input("digite a altura: "))
    draw_retangulo_vazado(l,a)
    
main()