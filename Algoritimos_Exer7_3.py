'''Faça um programa que leia dois valores inteiros positivos para base, expoente e faça o cálculo da potência utilizando comandos de repetição, ou seja,
 não pode ser utilizado pow do C ou ** Python.
Exemplo: 2^4 = 2 x 2 x 2 x 2'''

base=int(input('Informe um valor para base: '))
exp=int(input('Informe um valor para expoente: '))
potencia=base
controle=1
while controle < exp:
    controle+=1
    potencia*=base
print(potencia)    


