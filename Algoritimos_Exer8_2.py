'''Solicite um número entre 1 e 10 e também um idioma (I) inglês ou (E) espanhol. Mostre o número informado escrito por extenso no idioma escolhido pelo usuário.
 Caso o usuário informar algum número fora deste intervalo deve parar o programa.'''
 
num=1
while num >=1 and num <=10:    
    num=int(input('Informe um número entre 1 e 10: '))    
    idioma=str(input('Informe um idioma. (I) inglês ou (E) espanhol:  ')).upper()
    if idioma == 'I':
        if num ==1:
            print('One')
        elif num==2:
            print("Two")    
        elif num==3:
            print('Three')
        elif num==4:
            print('Four')
        elif num==5:
            print('Five')
        elif num==6:
            print('Six')
        elif num==7:
            print('Sevem')
        elif num==8:
            print('Eight')
        elif num==9:
            print('Nine')
        elif num==10:
            print('Ten') 
    if idioma == 'E':
        if num ==1:
            print('Uno')
        elif num==2:
            print("Dos")    
        elif num==3:
            print('Tres')
        elif num==4:
            print('cuatro')
        elif num==5:
            print('cinco')
        elif num==6:
            print('Seis')
        elif num==7:
            print('Siete')
        elif num==8:
            print('Ocho')
        elif num==9:
            print('Nueve')
        elif num==10:
            print('Diez')

                                                 





