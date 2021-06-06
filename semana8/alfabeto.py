def main():
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    print(alfabeto[:13])
    print(alfabeto[13:27])
    print(alfabeto[13:])
    print(len(alfabeto))
    print(alfabeto[1:10])
    print(alfabeto[2:2])
    
    
    carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
    
    carnes2 = []
    
    for i in carnes:
        carnes2.append(i)
    carnes2.append("Ponta de Agulha")
    
    
    carnes1 = ["picanha", "alcatra"]
    carnes2 = ["filé mignon", "cupim", "ponta de alcatra"]
    carnes3 = carnes2 + carnes1
    
    print("carnes1 ",carnes1)
    print("carnes2 ",carnes2)
    print("carnes3 ",carnes3)
    
    
main()