nome = input("Nome do funcionario: ")
horas = int(input("Horas trabalhadas: "))
valorh = int(input("Valor por Horas: "))
filhos  = int(input("Quantidade de Filhos: "))
salario = horas* valorh
adicional = salario* 0.03* filhos
salariot = salario+ adicional
print ("O valor total de", nome, "com adicional é R$", salariot)
