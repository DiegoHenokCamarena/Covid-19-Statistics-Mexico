import os

lineas = []
estados = {}
sexo ={}
edadAcum = 0
casos = []

with open('C:/Users/52552/Documents/2020-2/EDA II/P10EDA2/covid-19-15052020.csv','r') as file: #Change this path
    lineas = file.readlines()

    for i in range(1, len(lineas)):
        l = lineas[i]
        registro = l.split(',')  
        edadAcum = edadAcum + int( registro[3] ) #registro[3] is the age

        if registro[1] in estados: #registro[1] es el estado
            estados[ registro[1]] += 1
        else:
            estados[ registro[1]] = 1

        if registro[2] in sexo:
            sexo[ registro[2] ] += 1 #registro[2] is the genre/sex
        else:
            sexo[ registro[2] ] = 1

print("\n     Resumen. Casos Covid en México   \n")
print("     Casos por estado\n")
for estado,numero in estados.items():
    casos.append("         - "+ estado + " cuenta con " + str(numero) + " casos\n")
    print("         - "+ estado + " cuenta con " + str(numero) + " casos\n")
edadProm = edadAcum/(len(lineas)-1)
print("     Casos por sexo: \n")
casosH ="          Total de hombres con Covid: " + str(sexo['"M"']) + "\n"
print("          Total de hombres con Covid: " + str(sexo['"M"']) + "\n")
casosM = "          Total de mujeres con Covid: " + str(sexo['"F"']) + "\n"
print("          Total de mujeres con Covid: " + str(sexo['"F"']) + "\n")
prom = "     Edad promedio de los contagiados: " + str(edadProm) + "\n" 
print("     Edad promedio de los contagiados: " + str(edadProm) + "\n" )

lista = estados.values() 
minimo=min(lista)
maximo=max(lista)

for est, num in estados.items():
    if num == minimo: 
        casmin = "     El estado con menos casos es "+ est+ " con "+ str(num)+ " casos\n"
        print("     El estado con menos casos es "+ est+ " con "+ str(num)+ " casos\n")
for est, num in estados.items():
    if num == maximo:
        casmax = "     El estado con mas casos es "+ est+ " con "+ str(num)+ " casos\n"
        print("     El estado con mas casos es "+ est+ " con "+ str(num)+ " casos\n")

print("     El numero total de casos confirmados de Covid en Mexico es de "+ str(len(lineas)-1) +"\n")

try:
    os.makedirs("Covid19Summary")
except:
    print("No se pudo crear el directorio o ya existe")

with open('Covid19Summary/resumenCovid.eda2','w') as resumen: #Choose your own path and name file, etc
    resumen.write("\n     Casos de Covid en México   \n")
    resumen.write("     Casos por estado\n")
    resumen.writelines(casos)
    resumen.write("     Casos por sexo: \n")
    resumen.write(casosH)
    resumen.write(casosM)
    resumen.write(prom)
    resumen.write(casmin)
    resumen.write(casmax)
    resumen.write("     El numero total de casos confirmados de Covid en Mexico es de "+ str(len(lineas)-1) +"\n")


