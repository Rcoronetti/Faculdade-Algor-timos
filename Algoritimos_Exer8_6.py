'''. Utilizando um comando de repetição dentro do outro, vamos resolver o problema abaixo:
Imagine-se num quartel. Logo pela manhã foi dado o seguinte exercício. Você deverá dar 10 voltas no quarteirão e a cada 2 voltas você deverá fazer 50 abdominais e 10 flexões.
 Toda volta deverá ser informada uma mensagem, e cada abdominal e flexão também, as mensagens devem seguir o modelo abaixo:
Volta numero ......
....... abdominal 
Flexão .......
a)	Faça este algoritmo utilizando o comando para.
b)	Faça este algoritmo utilizando o comando enquanto.

Exemplo:
Volta numero 1
Volta número 2
1 abdominal 
2 abdominal 
.
50 abdominal 
Flexão 1
Flexão 2
.
Flexão 10
Volta numero 3
Volta numero 4'''

for c in range(1,11,1):
    print(f'Volta numero {c}')
    if c%2==0:                 
        for abdominal in range(1,51,1):               
            print(f'{abdominal} abdominal')                 
            for flexao in range(1,11,1):                                            
                print(f'Flexão {flexao}')
	

