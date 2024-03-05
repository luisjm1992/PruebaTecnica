import csv
from tabulate import tabulate


#Requerimiento No. 2: Consultar las ofertas que publicó una empresa durante un
#periodo especifico de tiempo


companyName = 'Citi'
startDate = '2022-04-14'
endDate = '2022-06-29'

jobsJunior = 0
jobsMid = 0
jobsSenior = 0

totalCompany = []
offer = []

headers = ["Fecha de publicación", 
           "Título de la oferta", 
           "Nombre de la empresa", 
           "Nivel de experticia", 
           "País", "Ciudad", 
           "Tamaño de la empresa",
           "Tipo de ubicación", 
           "Disponible a contratar ucranianos"]

with open('large-jobs.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for oferta in reader:
        offer.append(oferta)

def GetCompany(company, stardDate, endDate):
    global jobsJunior, jobsMid, jobsSenior, totalCompany

#1 Número total de ofertas.
    totalOfertasEmpresa = 0
    
    for jobOffer in offer: 
        if jobOffer['company_name'] == company and stardDate <= jobOffer['published_at'] <= endDate:
            totalOfertasEmpresa += 1 
            #agregamos a la lista
            totalCompany.append(jobOffer)

#2 Número total de ofertas con experticia
    for nJobs in totalCompany:
        if nJobs['experience_level'] == 'junior':
            jobsJunior += 1
        elif nJobs['experience_level'] == 'mid':
            jobsMid += 1
        elif nJobs['experience_level'] == 'senior':
            jobsSenior += 1
#3
    data = []
    for value in totalCompany:
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
    print(tabulate(data, headers=headers))

    return totalOfertasEmpresa, nJobs, company, value, data

result = GetCompany(companyName, startDate, endDate)
total = len(totalCompany)
print('total Empresas : ', total)
print('total mid : ', jobsMid)
print('total junior : ', jobsJunior)
print('total senior : ', jobsSenior)
