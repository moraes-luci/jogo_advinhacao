from random import randrange
print("""
#################################################
####          Jogo da Advinhação             ####    
#################################################
      """)


def iniciar_jogo():
    numero_sorteado = randrange(1, 8)
    try:
        numero_escolhido = int(input("\nEscolha um número entre 1 e 8.\n"))
        numeros = (1, 2, 3, 4, 5, 6, 7, 8)
        if numero_escolhido not in numeros:
            print("\nNúmero não está no intevalo de 1 à 8, tente novamente!\n")
        elif numero_escolhido == numero_sorteado:
            print(f"\nParabéns, você acertou, o número sorteado foi {numero_sorteado} !!!\n")
        else:
            print(f"\nQue pena, você errou, o número sorteado foi {numero_sorteado}!!!!\n")
    except ValueError:
        print("\nDigitação inválida! Tente novamente.\n")


instrucoes = ("""\n<<------Instruções ------>>>
Escolha um número de 1 à 8 e então aguarde para saber se advinhou o número sorteado!\n""")

# Menu
while True:
    try:
        opcao = int(input("""Escolha uma das opções abaixo:
    1- Iniciar Jogo.
    2- Instruções sobre o jogo.
    0- Sair\n"""))
        if opcao == 1:
            iniciar_jogo()
        elif opcao == 2:
            print(instrucoes)
        elif opcao == 0:
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")
    except ValueError:
        print("\nDigitação inválida! Tente novamente.\n")
