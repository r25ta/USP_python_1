def draw_retangulo_cheio(l,a):
    i = 0
    while(a > 0):
        i = l
        while(i > 0):
            print("#",end="")
            i = i -1
        print(end="\n")
        a = a - 1

def main():
    l = int(input("digite a largura: "))
    a = int(input("digite a altura: "))
    draw_retangulo_cheio(l,a)
    
main()