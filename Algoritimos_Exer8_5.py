'''Conforme e-mail enviado para a turma o coordenador do curso de Engenharia de Computação pediu para os calouros responderem o questionário do Perfil do Ingressante. 
Como resultado a direção mandava diariamente o relatório da imagem, mas este relatório tinha que ser alimentado diariamente. 
Com isso o coordenador pensou em fazer uma competição e informou que os alunos de EngComp já tinham aprendido o suficiente para fazer um sistema para calcular as estatísticas.

Seu sistema deve solicitar:
Quantos alunos existem na turma de EngComp e SisInfo.
Após terá um menu que pede qual turma o acadêmico que respondeu faz parte:
620 – Engenharia de Computação
41 – Sistemas de Informação
0 – Sair

No momento que sair das repostas, deve informar as seguintes estatísticas:
Total de Acadêmicos que responderam.
Total de Acadêmicos que responderam de cada curso.
Mostrar o % de participação de cada curso.
Mostrar os faltantes e o % de faltantes de cada curso.
Mostrar o curso que teve mais % de participação.'''


qtde_alunosEng= int(input('Informe o número de alunos que pertemcem ao curso de Engenharia de Computação: '))
qtde_alunosSistemas= int(input('Informe o número de alunos que pertemcem ao curso de Sistemas da Informação:  '))
somaEng=0
somaSist=0
turma=1
print('620 – Engenharia de Computação\n41 – Sistemas de Informação\n0 – Sair')
while turma !=0:
    turma=int(input('Informe, através do cod, qual turma você faz parte : '))
    if turma ==620:
        somaEng+=1
    elif turma ==41:
        somaSist+=1
    elif turma==0:
        break
    else:
        print('Informe um código válido!') 
print()        
print(f'Total de respostas: {somaEng+somaSist}') 
print(f'----------Total de respostas por curso:--------------\n\nEngenharia de Computação: {somaEng} - {(somaEng/(qtde_alunosEng))*100:0.1f}%\nSistemas da Informação: {somaSist} - {(somaSist/(qtde_alunosSistemas))*100:0.1f}% ')
print() 
print(f'----------Total de faltantes:------------------------\nEngenharia de Computação: {qtde_alunosEng-somaEng} - {((qtde_alunosEng-somaEng)/qtde_alunosEng)*100:0.1f}%\nSistemas de Informação: {qtde_alunosSistemas-somaSist} - {((qtde_alunosSistemas-somaSist)/qtde_alunosSistemas)*100:0.1f}%')
print()
if somaEng>somaSist:
    print('O curso com maior índice de participação foi Engenharia de Computação! ')
elif somaSist>somaEng:
        print('O curso com maior índice de participação foi Sistemas de Informação! ')
else:
    print('Ambos os cursos tiveram o mesmo índice de participação!')        
