def maximo(x,y):
    if(x>=y):
        return x
    
    else:
        return y

    def test_maximo_x():
        assert maximo(4,2) == 4
    
    def test_maximo_y():
        assert maximo(3,6) == 6

def main():
    x = int(input("Digite o primerio numero:"))
    y = int(input("Digite o segundo numero:"))
    
    print(maximo(x,y))

main()