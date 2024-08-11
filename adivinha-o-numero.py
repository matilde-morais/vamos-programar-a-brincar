import random  # módulo para números aleatórios

def main(): # função principal
    
    print(" ")
    print("BEM-VINDO AO 'ADIVINHA O NÚMERO'!")
    print(" ")
    print("Estou a pensar num número entre 1 e 20. Tens 5 tentativas para adivinhar!")
    
    numeroAdivinhar = random.randint(1, 20) # gera um número aleatório entre 1 e 20
    
    tentativas = 0 # começa com 0 tentativas
    tentativasMaximo = 5 # tem 5 tentativas no total
    
    while tentativas < tentativasMaximo: # enquanto não fizer 5 tentativas
        try:
            print(" ")
            adivinha = int(input("Número: ")) # recebe o número que o jogador acha que é
            if adivinha < 1 or adivinha > 20: # se o número não estiver entre 1 e 20
                print(" ")
                print("Por favor, adivinhe um número entre 1 e 20.")
                continue
        except ValueError: # se o jogador não inserir um número válido
            print(" ")
            print("Por favor, insira um número válido.")
            continue
        
        tentativas += 1 # aumenta 1 tentativa de cada vez
        
        if adivinha == numeroAdivinhar: # se o jogador adivinhar o número
            print(" ")
            print(f"Parabéns! Adivinhaste em {tentativas} tentativas!")
            funcaoPremio() # corre a função funcaoPremio
            break # termina o jogo
        elif adivinha < numeroAdivinhar: # a adivinha é menor que o número
            print(" ")
            print("Muito baixo! Tenta de novo.")
        else: # a adivinha é maior que o número
            print(" ")
            print("Muito alto! Tenta de novo.")
        
        restoTentativas = tentativasMaximo - tentativas # quantas tentativas restam
        print(f"Restam {restoTentativas} tentativas!")
    
    if tentativas == tentativasMaximo: # se o jogador usou todas as tentativas
        if adivinha != numeroAdivinhar: # se o jogador não adivinhou o número até á última tentativa
            print(" ")
            print("Acabaram as tentativas! O número era " + str(numeroAdivinhar) + ".")
            print(" ")
            funcaoPerder() # corre a função funcaoPerder

def funcaoPremio(): # função para mostrar o prémio
    print("Yay! Aqui está o teu prémio!")
    print(" ")
    print(" ------------")
    print(" |          |")
    print(" |          |")
    print(" |          |")
    print("  \        /")
    print("   \      /")
    print("    |    |")
    print("    |    |")
    print("  __|____|__")
    print(" |__________|")
    print(" ")

def funcaoPerder(): # função para mostrar que o jogador perdeu
    print("Oh não! Perdeste!")
    print(" ")
    print("   ----------")
    print("  /          \\")
    print(" /   o    o   \\")
    print("|     ____     |")
    print(" \   |    |    /")
    print("  \           /")
    print("   -----------")
    print(" ")

if __name__ == "__main__":
    main()  # corre a função main