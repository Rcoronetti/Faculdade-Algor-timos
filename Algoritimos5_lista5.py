cod,qtd=input('Informe o código do produto: '),input('Informe a quantidade de produtos adquiridos: ')
cod=int(cod)
qtd=int(qtd)
if cod == 1:
    print('Total: R$ %0.2f'%(qtd*4.00))
elif cod == 2:
    print('Total: R$ %0.2f'%(qtd*4.50))
elif cod == 3:
    print('Total: R$ %0.2f'%(qtd*5.00))  
elif cod == 4:
    print('Total: R$ %0.2f'%(qtd*2.00))
elif cod == 5:
    print('Total: R$ %0.2f'%(qtd*1.50))     
else:
    print('Informe um código válido')             