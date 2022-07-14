'''Solicite quantos alunos tem na turma de algoritmos, depois solicite a nota da prova de cada aluno. Ao final mostre a média da turma.'''
alunos=int(input('Informe número de alunos: '))
controle=0
media=0
while controle<alunos:
    controle+=1
    nota=float(input('Informe sua nota: '))
    media+=nota
print(f'A média da turma é: {(media/alunos):0.1f}')    

