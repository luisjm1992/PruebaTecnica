import csv
from tabulate import tabulate

offer = []
countryCode = 'ES'
startDate = '2022-04-14'
endDate = '2022-05-20'

headers = ["Fecha de publicación", 
               "Título de la oferta", 
               "Nivel de experticia", 
               "Nombre de la empresa", 
               "Ciudad", 
               "Tipo de trabajo", 
               "Disponible a contratar ucranianos"]


with open('large-jobs.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for oferta in reader:
        offer.append(oferta)

totalCompany = []
empresas = set()
ciudades = {} 

def listar(cod, startDate, endDate):
    
    for jobOffer in offer:
        
        if jobOffer['country_code'] == cod and startDate <= jobOffer['published_at'] <= endDate:
            totalCompany.append(jobOffer)
            empresas.add(jobOffer['company_name'])
            
            ciudad = jobOffer['city']

            if ciudad in ciudades:
                ciudades[ciudad] += 1
            else: 
                ciudades[ciudad] = 1

    data = []
    for value in totalCompany:
        valueinfo = [
            value['published_at'],
            value['title'],
            value['experience_level'],
            value['company_name'],
            value['city'],
            value['workplace_type'],
            value['open_to_hire_ukrainians']
        ]
        
        data.append(valueinfo)


    print(tabulate(data, headers=headers))
    return totalCompany, data, empresas

resultado = listar(countryCode, startDate, endDate)


totalCompanies = len(totalCompany)
totalEmpresasC = len(empresas)
totalCiudadesC = len(ciudades)
#Obtenemos el maximo y minimo de ofertas
ciudad_max_ofertas = max(ciudades, key=ciudades.get)
ciudad_min_ofertas = min(ciudades, key=ciudades.get)

print("--------------------------------------------------------------------------------------------")
print('El total de ofertas en el país en el periodo de consulta. : ', totalCompanies)
print('El total de empresas que publicaron al menos una oferta en el país de consulta : ', totalEmpresasC)
print('El numero de ciudades que publicaron al menos una oferta en el país de consulta : ', totalCiudadesC)
print('ciudad maxima ofertas: ', ciudad_max_ofertas)
print('ciudad minima ofertas: ', ciudad_min_ofertas)

