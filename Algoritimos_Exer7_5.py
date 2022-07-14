'''Utilizando flag ou variável de identificação de passagem, vamos resolver o problema abaixo:
Faça um programa que deve ser informado um número inteiro para ser realizada uma busca. 
Após informar o número a ser pesquisado, deve-se informar mais 10 números inteiros. Após informar os 10 números você deve utilizar somente uma mensagem para dizer se aquele
 número foi encontrado NUMERO ENCONTRADO, caso contrário deve informar que NUMERO NÃO ENCONTRADO'''

num = int(input("Entre com um numero a ser encontrado: "))

achou = 0

for i in range(10):
    numero = int(input("Entre com um numero: "))
    if numero == num:
        achou = achou + 1
if achou > 0:
    print("%d foi encontrado."%num)
else:
    print("%d nao foi encontrado."%num)
