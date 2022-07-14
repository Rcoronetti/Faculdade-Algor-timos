'''(Problema by professor Rafaeli) A prefeitura de Rio Seco teve que tomar uma medida urgente, pois os efeitos da estiagem estão castigando os moradores do bairro Poeira na
 periferia do município. A prefeitura conseguiu alugar dois caminhões pipa para trazer água para a população local todos os dias. Faça um programa utilizando uma estrutura de 
 repetição para calcular quantas viagens os caminhões terão que fazer para trazer 120.000 litros de água que a população consome todos os dias. 
Mas preste atenção, existem uns detalhes importantes que você precisa saber: as viagens iniciam com o caminhão que tem maior reservatório conforme imagem, mas este caminhão
 perde pelo caminho pelo menos 10% da água transportada, pois ele está com o tanque do reservatório com vários vazamentos, quando este caminhão está retornando vai o outro 
 caminhão com a metade da capacidade porque a estrada para o reservatório tem uma ponte que só passa um caminhão por vez.'''

caminhao1=9000
caminhao2=5000
total1=0
total2=0
viagens_caminhao1=0
viagens_caminhao2=0
while total1+total2<=120000:
    if caminhao1:
        viagens_caminhao1+=1
        total1+=caminhao1
    if caminhao2:    
        viagens_caminhao2+=1
        total2+=caminhao2
print(total1,total2,viagens_caminhao1,viagens_caminhao2)    

    





