def mensagem(jogador, jogada, n):
    if(jogada == 1):
        print(jogador, "tirou uma peça.")
                    
    else:
        print(jogador, "tirou", jogada, "peças.")

    if(n==1):
        print("Agora resta apenas uma peça no tabuleiro.")
        print("")
        
    elif(n>1):
        print("Agora restam", n, "peças no tabuleiro.")
        print("")
        
def computador_escolhe_jogada(n,m):
    i = 1
    jogada = m
    while(i <= m):
        if((n - i) % (m + 1) == 0):
            jogada = i
            
        i = i + 1    
    return jogada
       
def usuario_escolhe_jogada(n,m):
    n = int(input("Quantas peças você vai tirar? " ))
    while(n>m or n<=0):
        print("")
        print("Oops! Jogada inválida! Tente de novo.")
        n = int(input("Quantas peças você vai tirar? " )) 
    
    return n   

def partida():
    vencedor=""
    jogadaComputador=0
    jogadaUsuario=0
    m=0
    n = int(input("Quantas peças? "))
         
    while(n<1):
        print("")
        print("Oops! Jogada inválida! Tente de novo.")
        n = int(input("Quantas peças? "))
    
    while(m<=0):
        m = int(input("Limite de peças por jogada? "))
        while(m > n):
            print("")
            print("Oops! Jogada inválida! Tente de novo.")
            m = int(input("Limite de peças por jogada? "))
    
    jogaComputador = True
    
    if(n % (m+1) == 0):
        jogaComputador = False
        print("")
        print("Você começa!")
        print("")
        
    else:
        print("")
        print("Computador começa!")
        print("")
                        
    while(n>0):
        if(jogaComputador):
            jogaComputador = False
            jogadaComputador = computador_escolhe_jogada(n,m)
            n = n - jogadaComputador
                           
        else:
            jogaComputador = True
            jogadaUsuario = usuario_escolhe_jogada(n,m)
            n = n - jogadaUsuario

        if(jogaComputador):
            mensagem("Você",jogadaUsuario,n)
            if(n==0):
                return "Você"
                
        else:
            mensagem("O computador",jogadaComputador,n)
            if(n==0):
                return "Computador"
            
    return vencedor

def campeonato():
    pontosComputador = 0
    pontosUsuario = 0
    print("")
    print("*** Partida 1 ***")
    vencedor = partida()
    if(vencedor=="Computador"):
        print("")
        print("Fim do jogo! O",vencedor, "ganhou!")
        pontosComputador = pontosComputador + 1
    else:
        print("")
        print("Fim do jogo!",vencedor, "ganhou!")
        pontosUsuario = pontosUsuario + 1    
    
    print("")
    print("*** Partida 2 ***")
    vencedor = partida()
    if(vencedor=="Computador"):
        print("")
        print("Fim do jogo! O",vencedor, "ganhou!")
        pontosComputador = pontosComputador + 1
    else:
        print("")
        print("Fim do jogo!",vencedor, "ganhou!")
        pontosUsuario = pontosUsuario + 1    
      
    print("")
    print("*** Partida 3 ***")
    print("")
    vencedor = partida()
    if(vencedor=="Computador"):
        print("")
        print("Fim do jogo! O",vencedor, "ganhou!")
        pontosComputador = pontosComputador + 1
    else:
        print("")
        print("Fim do jogo!",vencedor, "ganhou!")
        pontosUsuario = pontosUsuario + 1    
    
    print("")  
    print("*** Final do Campeonato! ***")
    print("Placa: Você", pontosUsuario,"X",pontosComputador,"Computador")
                      
def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    
    n = 0
    while(n!=1 and n!=2):
        n = int(input(" 1 - para jogar uma partida isolada " + 
                      " 2 - para jogar um campeonato "))
        if(n!=1 and n!=2):
            print("")
            print("Opção inválida, tente novamente!")    

    if(n==1):
        print("")
        print("Você escolheu uma partida isolada")
        print("")
        print("*** Partida Isolada ***")
        print("")
        vencedor = partida()
        if(vencedor=="Computador"):
            print("")
            print("Fim do jogo! O",vencedor, "ganhou!")
        else:
            print("")
            print("Fim do jogo!",vencedor, "ganhou!")
    elif(n==2):
        print("")
        print("Você escolheu um campeonato")
        print("")
        campeonato()
    else:
        print("")
        print("Opção inválida, tente novamente!")
        

main()
