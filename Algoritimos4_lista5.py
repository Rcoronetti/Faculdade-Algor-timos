ddd= int(input('Informe o DDD: '))
numero = int(input('Informe o número do celular: '))
nome = input('Informe seu nome: ')
if ddd == 49:
    print('Olá, %s\n%s VOCÊ LIGOU PARA %d PARA O VELHO OESTE'%(nome,nome,numero))
if ddd == 48:
    print('Olá, %s\n%s VOCÊ LIGOU PARA %d A REGIÃO DO LITORAL'%(nome,nome,numero))    
if ddd == 47:
    print('Olá, %s\n%s VOCÊ LIGOU PARA %d A REGIÃO DE JOINVILLE'%(nome,nome,numero)) 
if ddd!=49 and ddd!=48 and ddd!=47:    
    print('Olá, %s\n%s VOCÊ LIGOU PARA %d UM TELEFONE PARA FORA DE SC'%(nome,nome,numero))



