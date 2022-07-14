'''1.	Solicite o nome e o salário de 10 pessoas, ao final mostre a soma de todos os salários digitados.'''
nome=''
salario=0
soma=0
for c in range(1,11):
    nome =str(input('Digite um nome: '))
    salario = float(input('Digite um salário: '))
    soma+=salario
print(soma)    

