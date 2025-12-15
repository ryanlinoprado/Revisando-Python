from random import randint
import os

nome = input('Qual o seu nome? ')

while not nome.replace(' ', '').isalpha():
    print('Erro: digite apenas letras.')
    nome = input('Qual o seu nome? ')


continuar = 's'

def limpar_tela():
    # Verifica o sistema operacional e executa o comando de limpeza apropriado
    if os.name == 'nt': # Para Windows
        os.system('cls')


while continuar.lower() == 's':
    computador = randint(0, 5)

    while True:
        try:
            num = int(input('Em qual número você acha que estou pensando de 0 a 5? '))
            break
        except ValueError:
            print('Erro: digite apenas números inteiros.')



    if num == computador:
        print(f'{nome}, você acertou o número! Era {computador}.')
        continuar = input('Quer tentar novamente? [s/n] ')
        limpar_tela()

    else:
        print(f'{nome}, você falhou. O número em que eu estava pensando era {computador}.')
        continuar = input('Quer tentar novamente? [s/n] ')
        limpar_tela()

        if continuar == 'n':
            print('O jogo será fechado')
            break  # sai do jogo ao acertar


