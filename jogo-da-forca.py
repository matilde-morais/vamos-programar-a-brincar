import os # módulo para limpar o ecrã
 
def limparEcra(): # função para limpar o ecrã
    os.system('cls' if os.name == 'nt' else 'clear') # muda consoante o sistema operativo

def desenhoForca(tentativas): # função para desenhar o boneco da forca
    estados = [
        # 6 erros
        '''
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |   / \\
           --
        ''',
        # 5 erros
        '''
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |   / 
           --
        ''',
        # 4 erros
        '''
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |    
           --
        ''',
        # 3 erros
        '''
           ------
           |    |
           |    O
           |   \\|
           |    |
           |    
           --
        ''',
        # 2 erros
        '''
           ------
           |    |
           |    O
           |    |
           |    |
           |    
           --
        ''',
        # 1 erro
        '''
           ------
           |    |
           |    O
           |    
           |    
           |    
           --
        ''',
        # 0 erros
        '''
           ------
           |    |
           |    
           |    
           |    
           |    
           --
        '''
    ]
    return estados[tentativas] # devolve o estado da forca

def mensagemFinal(ganhar): # função para mostrar a mensagem final
    if ganhar: # se o jogador ganhar
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
    else: # se o jogador perder
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

def jogarForca(): # função principal

    limparEcra()  # corre a função limparEcra
    print("BEM-VINDO AO 'JOGO DA FORCA'!")
    print(" ")
    
    # jogador 1 insere a palavra a adivinhar
    while True:
        palavra = input("Jogador 1, insira a palavra a adivinhar: ").strip().upper() # recebe a palavra a adivinhar
        if palavra.isalpha() and palavra != "": # checkar se a palavra é válida
            break # se a palavra for válida, sair do loop
        print("Palavra inválida! Por favor, insira uma palavra válida.")
        print(" ")
    
    limparEcra() # corre a função limparEcra
    
    palavraAdivinhar = ['_'] * len(palavra) # torna a palavra a adivinhar numa string de '_'
    letrasAdivinhar = [] # lista para guardar as letras adivinhadas
    tentativas = 6 # número de tentativas erradas possíveis
    ganhar = False # a variavél começa falsa

    while tentativas > 0 and not ganhar: # enquanto houver tentativas e o jogador não ganhar
        limparEcra()  # corre a função limparEcra
        print(desenhoForca(tentativas))  # corre a função desenhoForca
        print(" ")
        print(' '.join(palavraAdivinhar))  # mostra a palavra a adivinhar em '_' e letras já acertadas
        print(f"Letras adivinhadas: {' '.join(letrasAdivinhar)}")  # mostra as letras adivinhadas
        print(" ")
        
        while True:
            adivinha = input("Jogador 2, adivinhe uma letra: ").strip().upper() # recebe a letra a adivinhar
            print(" ")
            if len(adivinha) == 1 and adivinha.isalpha(): # checkar se a adivinha é uma letra
                if adivinha not in letrasAdivinhar: # checkar se a letra já foi adivinhada
                    break # se a letra não foi adivinhada antes, sair do loop
                else:
                    print("Já adivinhaste esta letra!")
            else: # se a adivinha não for uma letra
                print("Letra inválida! Por favor, insira uma letra válida.")
        
        letrasAdivinhar.append(adivinha) # adicionar a letra a adivinhar à lista de letras adivinhadas
        
        if adivinha in palavra: # se a letra a adivinhar estiver na palavra
            for i, letter in enumerate(palavra): # corre a palavra
                if letter == adivinha: # se for a letra certa
                    palavraAdivinhar[i] = adivinha # substutui o '_' pela letra a adivinhar
        else: # se a letra a adivinhar não estiver na palavra
            tentativas -= 1  # menos 1 tentativa possivel
        
        if '_' not in palavraAdivinhar: # se o jogador adivinhar todas as letras
            ganhar = True # o jogador ganha
    
    limparEcra() # corre a função limparEcra
    print(desenhoForca(tentativas)) # corre a função desenhoForca
    print('A palavra era: ', ' '.join(palavra)) # mostra a palavra a adivinhar
    print(" ")
    mensagemFinal(ganhar) # corre a função mensagemFinal

if __name__ == "__main__":
    jogarForca() # corre a função jogarForca
