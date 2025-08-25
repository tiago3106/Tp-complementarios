#Empiezo
dia_semana, dia, mes = input("ingrese el dia de la semana/dia/mes: ").split("/")
dia_semana = dia_semana.lower()
dia = int(dia.lower())
mes = int(mes.lower())
if (dia_semana != "lunes") and (dia_semana != "martes") and (dia_semana != "miercoles") and (dia_semana != "jueves" ) and (dia_semana != "viernes"):
    print("Error")

if (mes > 12):
    print("Error")

if (mes == "01") and (mes == "03") and (mes == "05") and (mes == "07") and (mes == "08") and (mes == "10") and  (mes == "12"):
    if (dia > "31"):
        print("Error")

if (mes == "4") and (mes == "06") and (mes == "9") and (mes == "11"):
    if (dia > "31"):
        print("Error")

