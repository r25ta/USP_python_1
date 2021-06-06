import math

#Função para calcular distancia, retorna distancia entre as coordenadas do ponto A e B
def calcDistancia(x1,y1,x2,y2):
    return math.sqrt((((x1 - x2)**2) + ((y1-y2)**2)))


def main():
    print("Calular a distância entre dois pontos")
    x1 = float(input("Digite coordenada X ponto 1:"))
    y1 = float(input("Digite coordenada Y ponto 1:"))
    x2 = float(input("Digite coordenada X ponto 2:"))
    y2 = float(input("Digite coordenada y ponto 2:"))
   
    if(calcDistancia(x1,y1,x2,y2) >= 10):
        print("longe!")
        
    else:
        print("perto!")    
main()

