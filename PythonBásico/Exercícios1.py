#Calcule a soma dos números 10 a 14
Soma = sum([10,11,12,13,14])
print(Soma) #Resultado: 60

#Calcule a média entre os números 10,15,20
Media = sum([10,15,20])/3
print(Media) #Resultado: 15

#Peça para o Usuário digitar duas notas e calcule a média ponderada entre elas
#media(nota1*peso1+nota2*peso2);(peso1+peso2)
#A soma dos pesos deve ser 10
peso1 = 4
peso2 = 6

# Lendo as notas e convertendo para float
nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))

# Calculando a média ponderada
notaMedia = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)

# Imprimindo a média
print("Média:", notaMedia)

# Verificando se o aluno foi aprovado ou reprovado
if notaMedia >= 5:
    print("Aprovado")
else:
    print("Reprovado")
    
#Qual o menor valor dessa lista?
#preços 100.20, 34.90, 31.50, 18.95
precos = min([100.20, 34.90, 31.50, 18.95])
print(precos) #Resultado: 18.95

#Avalie se o número digitado pelo usuário é par ou ímpar
#Se for par deve dar True e se for Impar deve dar false

Usuario = int(input("Digite um número: "))
if Usuario % 2 == 0:
    print(True)
else:
    print(False)
    
#Verefique se o menor preço dessa lista é menor doque 20
#100.20,  34.90, 31.50, 18.95

Vereficar = min([100.20, 34.90, 31.50, 18.95]) < 20
print(Vereficar) #Resultado: True

#Faça um programa que converta a temperatura em graus Fareinhert fornecida pelo Usuário em graus celcius
#Fórmula: (F-32)*5/9

temperatura = float(input("Digite a temperatura em graus Fareinhert: "))
temperaturaC = (temperatura-32)*5/9
print("A temperatura em graus Celcius é:", temperaturaC)