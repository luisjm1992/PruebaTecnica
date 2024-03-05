#Parte 1: Carga de Datos

#La información de las tres primeras y tres últimas ofertas de trabajo publicadas
#Numero total de ofertas 

import csv
from tabulate import tabulate

ofertas = []

with open('large-jobs.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for oferta in reader:
        ofertas.append(oferta)

def getInfoOffer(oferta):
    #devuelve un nuevo d con informacion especifica
    return {
        'Fecha de publicación': oferta['published_at'],
        'Título de la oferta': oferta['title'],
        'Nombre de la empresa que publica': oferta['company_name'],
        'Nivel de experticia de la oferta': oferta['experience_level'],
        'País de la oferta': oferta['country_code'],
        'Ciudad de la oferta': oferta['city']
    }

#total ofertas
totalOfertas = len(ofertas)

# tres ultimas y tres primeras ofertas 
lastOffers = [getInfoOffer(oferta) for oferta in ofertas[:3]]
firstOffers = [getInfoOffer(oferta) for oferta in ofertas[-3:]]



print("-------Tres primeras-------")
print(tabulate(firstOffers, headers="keys"))
print("-------Tres ultimas-------")
print(tabulate(lastOffers, headers="keys"))
print("---------------------------")
print("Total de ofertas: ", totalOfertas)
