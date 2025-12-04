import statistics
import platform
import os

 # Tentei fazer um comando p limpar a tela e não rolou :P
 # def limpar_tela():
 #    sistema = platform.system()
 #    if sistema == "Windows":
 #        os.system("cls")
 #    else:
 #        os.system("clear")
 #
 #        input("\nPressione ENTER para continuar...")
 #        limpar_tela()

print("### Calculadora Python ###")
nome = input("Digite o seu nome (evite números): ")

while True:
    print(f"\nOlá, {nome}! Escolha uma das opções abaixo:\n")
    print('''[ 1 ] Soma
[ 2 ] Subtração
[ 3 ] Tabuada
[ 4 ] Divisão
[ 5 ] Porcentagem
[ 6 ] Desconto
[ 7 ] Sair''')

    try:
        num = int(input("Qual tipo de conta você deseja executar? "))

    except ValueError:
        print("Entrada inválida! Digite apenas números.")
        continue

    if num == 7:
        print("O programa será encerrado. Até logo!")
        break

    if num == 1:
        try:
            num2 = float(input("Digite o primeiro número da soma: "))
            num3 = float(input("Digite o segundo número da soma (ou 0 caso não seja necessário): "))

        except ValueError:
            print("Entrada inválida! Tente novamente.")
            continue


        soma = num2 + num3
        print(f"A soma de {num2} + {num3} é {soma}")




    elif num == 2:
        try:
            num2 = float(input("Digite o primeiro número da subtração: "))
            num3 = float(input("Digite o segundo número a subtração(ou 0 caso não seja necessário): "))

        except ValueError:
            print("Entrada inválida! Tente novamente.")
            continue


        sub = num2 - num3
        print(f"A subtração de {num2} - {num3} é {sub}")

    elif num == 3:
        try:
            num2 = float(input("Digite o número que deseja para a tabuada: "))

        except ValueError:
            print("Entrada inválida! Tente novamente.")
            continue


        print(f"Tabuada de {num2}:")
        for i in range(1, 11):
            print(f"{num2} x {i} = {num2 * i}")

    elif num == 4:
        try:
            num2 = float(input("Digite o primeiro número da divisão: "))
            num3 = float(input("Digite o segundo número a divisão: "))

        except ValueError:
            print("Entrada inválida! Tente novamente.")
            continue


        if num3 == 0:
            print("Erro: Não é possível dividir por zero!")
        else:
            div = num2 / num3
            print(f"A divisão de {num2} por {num3} é {div}")

    elif num == 5:
        try:
            num2 = float(input("Digite o primeiro número a ser divido: "))
            num3 = float(input("Digite o segundo número: "))

        except ValueError:
            print("Entrada inválida! Tente novamente.")
            continue


        porc = (num2 / num3) * 100
        print (f"O resultado da sua porcentagem é: {porc}")


    elif num == 6:
        try:
            num2 = float(input("Digite o preço inicial: "))
            num3 = float(input("Digite o valor de desconto: "))

        except ValueError:
            print("Entrada inválida! Tente novamente.")
            continue


        desc = num2 - (num2 * num3 / 100)
        print(f"O novo preço é: {desc}")

    else:
        print("Opção inválida! Escolha um número de 1 a 7.")


    print("\n" + "-"*40)




