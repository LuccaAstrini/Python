#fazer um programa que rode um fatorial da escolha do usuário
num = int(input("Digite um número: "))
fatorial = num

while num >= 2:
    fatorial = fatorial * (num-1)
    num = num-1

print("Valor total: ", fatorial)

#Simule um cofre com senha prefefinida e use o while para tentar até acertar a senha
# e a cada erro o programa mostra a quantidade de tentativas e falha ao errar mais de 3 vezes

senha = 1256
tentativas = 3;

while tentativas != 0:
    senhaDigitada = int(input("Digite a senha: "))
    if senhaDigitada == senha:
        print("Senha correta")
        break
    else:
        tentativas = tentativas - 1
        print("Senha incorreta, tentativas restantes: ", tentativas)
    