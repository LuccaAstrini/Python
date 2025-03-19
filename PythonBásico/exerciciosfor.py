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
