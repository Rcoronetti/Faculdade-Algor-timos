#1. Faça um algoritmo que leia um vetor de inteiro de tamanho 10 e após a leitura exiba os valores lidos de trás para frente.
vet=[]
for c in range(10,-1,-1):
    vet.append(int(input(f"Entre com o valor de vet[{c}]:")))
print(vet)    