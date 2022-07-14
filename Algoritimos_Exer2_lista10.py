#2. Faça um algoritmo que leia um vetor de inteiro de tamanho 10 e após a leitura o usuário deverá informar um valor que ele queira encontrar dentro do vetor.
#  Exiba então quantas vezes o número foi encontrado dentro do vetor digitado.

vet=[]
for c in range(10):
    vet.append(int(input(f"Entre com o valor de vet[{c}]:")))

valor= int(input('Digite o valor a ser encontrado: '))
print(f'O valor {valor} aparece  {vet.count(valor)} vezes na lista.')
     
  
