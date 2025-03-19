#Tabuada
tabuada = int(input("Digite um número para ver a tabuada: "))
limite = int(input("Até qual número deseja calcular?: "))
for numero in range(0, limite+1):
    print(f'{tabuada} x {numero} = {tabuada*numero}')


#faça um programa que calcule o enésimo elemento da série de Fibonnaci: ex 1,1,2,3,5,8...
n = int(input("Digite o enésimo elemento da série de Fibonacci: "))
a = 0
b = 1
for i in range(0, n):
    pos = a + b
    b = a
    a = pos
    print(pos)

#Faça um programa que calcule a média de uma lista de números
lista = [1,2,3,4,5,6,7,8,9,10]
soma = 0
for numero in lista:
    soma += numero
print(f'A média da lista é: {soma/len(lista)}')
