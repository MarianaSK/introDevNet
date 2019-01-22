#entrada
nome=input("Qual o seu nome: ") #Mariana
#saida
print("Oi, "+nome) #Olá, Mariana
#teste de condicionais
numSecreto=5
numeroUser=int(input("Advinhe qual o numero escolhido. Dica: o numero esta entre 0 e 10"))

while(numSecreto!=numeroUser):
    print("Voce errou... Tente outra vez")
    numeroUser=int(input("Advinhe qual o numero escolhido. Dica: o numero esta entre 0 e 10"))
else:
    print("Voce acertou!")

