import csv

def run(data):

  with open(data,"r") as datos:
    reader=csv.reader(datos, delimiter=",")
    cabecera=next(reader)

    print(cabecera)