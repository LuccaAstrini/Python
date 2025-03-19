#Escreva uma função que calcule o quadrado do numero como parâmetro, 
# se não for passado o padrão é 5

def quadrado (num = 5):
    num *= num;
    print(num)

quadrado()

#Faça uma função que receba como parâmetro uma temperatura em Ferenheit e 
# retorne a temperatura em Celsius

def temperatura(f):
    c = (f-32)*5/9
    print(f"A temperatura em Celsius é: {c:.2f}")

temperatura(52)

#Escreva uma função que receba dois parâmetros, O primeiro será uma palavra, 
# se ela for quadrado deverá calcular o quadrado do número passado como segundo parâmetro
#Se a palavra for cubo deverá calcular o cubo do número passado como segundo parâmetro

def calculo(palavra, num):
    if palavra == "quadrado":
        num *= num
        print(num)
    elif palavra == "cubo":
        num = num**3
        print(num)
    else:
        print("Palavra inválida")

calculo("quadrado", 5)
calculo("cubo", 3)
calculo("teste", 3)