totalf = int(input("Quantidade de fotos: "))
pacotes =  int(totalf/100)
avulsas = totalf- (pacotes*100)
custot = pacotes* 44.0+ avulsas* 0.70 
print ("O numero de pacotes é", pacotes, "e de fotos avulsas é", avulsas, "totalizando R$", custot)
