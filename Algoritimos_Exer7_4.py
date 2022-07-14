'''4. Utilizando variáveis acumuladoras, vamos refazer o problema abaixo:
O que você mais gosta de fazer nos finais de semana:
1) Dormir
2) Estudar algoritmos
3) Passear
4) Outros
5) Sair

Terminando a repetição você deverá mostrar as estatísticas abaixo:
Quantidade total de votos da enquete (lembre-se que o zero não pode considerar).
Quantidade de votos de cada escolha. 
Percentual de cada escolha.
Escolha com mais votos. (Considerar que não haverá empates).
'''
num=0
escolha1=0
escolha2=0
escolha3=0
escolha4=0  
    
while num !=5:
    print('O que você mais gosta de fazer nos finais de semana?:\n1) Dormir\n2) Estudar algoritmos\n3) Passear\n4) Outros\n5) Sair')
    num=int(input('Digite sua opção: '))
    print()
    if num==1:        
        escolha1+=1
    elif num==2:
        escolha2+=1
    elif num==3:
        escolha3+=1
    elif num==4:
        escolha4+=1
      
    
total=escolha1+escolha2+escolha3+escolha4                
print(f'Total de votos da enquete: {total}')  
print('---Votos por item----')         
print(f'Dormir: {escolha1} voto(s), {(escolha1/total)*100:.1f}% ')
print(f'Estudar algoritmos: {escolha2} voto(s), {(escolha2/total)*100:.1f}%')
print(f'Passear: {escolha3} voto(s), {(escolha3/total)*100:.1f}%')
print(f'Outros: {escolha4} voto(s), {(escolha4/total)*100:.1f}%')

if(escolha1 > escolha2 and escolha1 >  escolha3 and escolha1 > escolha4):
    print("Dormir foi o mais votado.")
elif(escolha2 >escolha1 and escolha2 > escolha3 and escolha2 > escolha4):
    print("Estudar foi o mais votado.")			
elif(escolha3 > escolha1 and escolha3 > escolha2 and escolha3 > escolha4):
    print("passear foi o mais votado.")
elif(escolha4 > escolha1 and escolha4 > escolha2 and escolha4 > escolha3):
    print("Outros foi o mais votado.")
