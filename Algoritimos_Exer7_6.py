'''Utilizando flag ou variável identificação de passagem, vamos resolver o problema abaixo:
(Problema 1165 da Uri) Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser dividido
 apenas pelo número 1 e pelo número 7.
Entrada: A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100), indicando o número de casos de teste da entrada.
 Cada uma das N linhas seguintes contém um valor inteiro X (1 < X ≤ 107), que pode ser ou não, um número primo.
Saída: Para cada caso de teste de entrada, imprima a mensagem “X eh primo” ou “X nao eh primo”, de acordo com a especificação fornecida.'''




n=int(input('Informe o número de testes: '))
for i in range(0,n):
    total=True
    x=int(input('Informe o número: '))
    for c in range(2,x):                   
        if x%c==0:  
            total=False
            break
    if total:
        print('eh primo')   
    else:
        print('nao eh primo')         

'''ou
       repeticoes=int(input())
for a in range(1,repeticoes+1):
    numeros_teste=int(input())
    for c in range(2,numeros_teste):
        if numeros_teste%c==0:
            print(f'{numeros_teste} nao eh primo')                       
            break
    else:   
        print(f'{numeros_teste} eh primo')  
'''
         
        
            
            
                    



        