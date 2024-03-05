#1: Listar las últimas N ofertas de trabajo según su país y nivel deexperticia

import csv
from tabulate import tabulate


headers = ["Fecha de publicación", 
           "Título de la oferta", 
           "Nombre de la empresa", 
           "Nivel de experticia", 
           "País", "Ciudad", 
           "Tamaño de la empresa",
             "Tipo de ubicación", 
             "Disponible a contratar ucranianos"]
ofertas = []

##Leemos el archivo  csv
with open('large-jobs.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for oferta in reader:
        ofertas.append(oferta)


# N = 20
# countryCode = 'ES'
# developerLevel = 'senior'
        
def getNumberOfer(numbeQueries, countryCode, levelDeveloper):
    
    selectedOffers = []
    for offer in ofertas:
        #agrega elementos a la lista si cumple con la condición
        if offer['country_code'] == countryCode and offer['experience_level'] == levelDeveloper:
            selectedOffers.append(offer)

   
    selectedOffers = sorted(selectedOffers, key=lambda x: x['published_at'], reverse=True)
    
    data = []
    for value in selectedOffers[:numbeQueries]:
        
        valueinfo = [
            value['published_at'],
            value['title'],
            value['company_name'],
            value['experience_level'],
            value['country_code'],
            value['city'],
            value['company_size'],
            value['workplace_type'],
            value['open_to_hire_ukrainians']
        ]
        data.append(valueinfo)
    
    return data

N = 20
countryCode = 'ES'
developerLevel = 'senior'


print(tabulate(getNumberOfer(N, countryCode, developerLevel), headers=headers))
print("Total de ofertas seleccionadas:", len(getNumberOfer(N, countryCode, developerLevel)))

