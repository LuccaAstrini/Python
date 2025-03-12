#Regra Universal de começar com um Hello World para dar sorte
print("Hello World")
#Definindo variáveis
a = 10
b = 5

#Operações Simples
c = a+b
print("Soma: ", c)

c = a-b
print("Subtração: ", c)

c = a/b
print("Divisão: ", c)

c = a*b
print("Multiplicação: ", c)

#Condicionais
c = a>b
print(c)

c = a<b
print(c)

#Funções Built-in

NumAbsol = abs(-10) #Retorna o valor absoluto
print(NumAbsol)

ValorMin = min(1,2,3,4,5) #Retorna o menor valor
print(ValorMin)

ValorMax = max(1,2,3,4,5) #Retorna o maior valor
print(ValorMax)

Soma = sum([1,2,3,4,5]) #Retorna a soma dos valores
print(Soma)

Potencia = pow(2,3) #Retorna a potência
print(Potencia)

#nome = input("Digite seu nome: ")
#print("O nome é: ", nome)

help(bool)#help ajuda a entender uma determinada função

#Teste de Input
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
garan = input(f"Certeza que sua idade e seu nome são: {nome}, {idade}? (sim/não) ")
#O uso de f é para incluir variáveis dentro da string que é exibida ao usuário
#Isso permite que você insira o valor das variáveis diretamente na string

while garan != "sim":
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    garan = input(f"Certeza que sua idade e seu nome são: {nome}, {idade}? (sim/não) ")