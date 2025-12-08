from time import sleep
for Iniciando in range (3,0,-1):
    print (Iniciando)
    sleep(1)

nome = str(input('Qual o seu nome?' ))
casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual o seu salário? '))
ano = int(input('Em quantos anos você pretende pagar? '))

prestação = casa / (ano * 12)
mínimo = sal * 30 / 100

print ('Para pagar uma casa de R${:.2f} em {} anos '.format(casa, ano))
print ('você precisa pagar prestações de R${:.2f}'.format(prestação))
print ('e o mínimo que você deve pagar é de R${:.2f}!'.format(mínimo))

if prestação <= mínimo:
    print ('Você foi aprovado(a), {}! :D'.format(nome))

else:
    print ('Infelizmente você foi reprovado(a), {}. :('.format(nome))

