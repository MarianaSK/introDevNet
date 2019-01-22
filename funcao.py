ladoA=int(input("Lado A do retangulo: "))
ladoB=int(input("Lado B do retangulo: "))

#definindo a função
def areaRetangulo(ladoA, ladoB):
    area=ladoA*ladoB
    print("A area do retangulo e: " + str(area))

#chamando a função
areaRetangulo(ladoA, ladoB)