'''Usando das explicações de string e caractere, faça um algoritmo para encontrar um doador de sangue do tipo (B-). Seu programa deve solicitar o nome e o tipo sanguíneo
 de cada doador, pare de solicitar assim que encontrar o doador compatível.'''
tipo=''
while tipo!='B-':
    nome=str(input('Informe seu nome: '))
    tipo=str(input('Informe seu tipo sanguíneo: ')).upper()
    if tipo=='B-':
        print(f'Doador encontrado! {nome}\nTipo sanguíneo: {tipo}')
        break
