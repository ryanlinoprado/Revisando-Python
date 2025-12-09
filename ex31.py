# Função para ler apenas letras
def ler_nome():
    while True:
        nome = input("Qual seu nome? ").strip()
        if nome.replace(" ", "").isalpha():  # permite nomes compostos
            return nome
        else:
            print("Entrada inválida! Digite apenas letras.\n")

# Função para ler idade (inteiro)
def ler_idade():
    while True:
        try:
            idade = int(input("Qual sua idade? "))
            if idade >= 0:
                return idade
            else:
                print("Idade não pode ser negativa.\n")
        except ValueError:
            print("Entrada inválida! Digite apenas números.\n")

# Função para ler distância (float)
def ler_distancia():
    while True:
        try:
            dist = float(input("Qual a distância a ser percorrida? "))
            if dist >= 0:
                return dist
            else:
                print("A distância não pode ser negativa!\n")
        except ValueError:
            print("Entrada inválida! Digite apenas números.\n")

nome = ler_nome()
idade = ler_idade()

# Verifica habilitação
if idade >= 18:
    print(f"{nome}, você está habilitado para dirigir.")
else:
    print(f"Você não está habilitado. Você tem {idade} anos de idade.")

dist = ler_distancia()

# Calcula valor
if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45

print(f"{nome}, o valor final a ser pago será de R$ {preco:.2f}")
