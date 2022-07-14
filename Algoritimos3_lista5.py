dia,mes,ano=input("Informe o dia,mês e ano no formato dd m aaaa: ").split()
dia=int(dia)
mes=int(mes)
ano=int(ano)
if mes ==1:
    print("Chapecó, %d/janeiro/%d"%(dia,ano))
elif mes ==2:
     print("Chapecó, %d/fevereiro/%d"%(dia,ano))
elif mes ==3:
     print("Chapecó, %d/março/%d"%(dia,ano))
elif mes ==4:
     print("Chapecó, %d/abril/%d"%(dia,ano))
elif mes ==5:
     print("Chapecó, %d/maio/%d"%(dia,ano))
elif mes ==6:
     print("Chapecó, %d/junho/%d"%(dia,ano))
elif mes ==7:
     print("Chapecó, %d/julho/%d"%(dia,ano))
elif mes ==8:
     print("Chapecó, %d/agosto/%d"%(dia,ano))      
elif mes ==9:
     print("Chapecó, %d/setembro/%d"%(dia,ano))
elif mes ==10:
     print("Chapecó, %d/outubro/%d"%(dia,ano))
elif mes ==11:
     print("Chapecó, %d/novembro/%d"%(dia,ano))
elif mes ==12:
     print("Chapecó, %d/dezembro/%d"%(dia,ano)) 
else:
    print('Digite um mês valido')         



