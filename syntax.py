print(2+2)
print(type(2))
print("Isso eh uma string")
print("na verdade eh um teste")
print("junto"+"separado")
print("abc"*3)
print("Oi, meu nome eh {}!".format("Chris")) #.format é um metodo que permite preencher chaves vazias ou nao nomeadas
print("Na verdade, meu nome eh {nome}".format(nome="Mariana")) #quando as chaves sao nomeadas, eh preciso referenciar 
print("a b c".split(" "))#uma string vira varias strings dado o delimitador para fazer varias strings, neste caso, o delimitador e um espaço
print("a, b, c".split(",")) #neste outro caso é uma virgula
print(",".join(['a', 'b', 'c'])) #pega varias strings e faz delas uma unica string dado o delimitador, que e uma virgula
#entao, 'a,b,c'
#DEFININDO VARIAVEIS
a=3
print(a)
#variaveis=atributos
#funçoes=metodos
print(a.bit_length()) #11 em binario, logo 2 bits
nome="ErA PrA Ser TUDO minusculo"
print(nome.lower())
