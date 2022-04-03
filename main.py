import numpy as np
import json
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib import lines as lns
import keys
from imageToTrello import fileToCard

key = keys.key
token = keys.token
image = keys.imagePATH
cardid = keys.cardID

###################################################################
#Pegando os dados dos cartões do trello    
###################################################################
def webScraping(tabelaID):    
    divs = driver.find_elements_by_xpath(
            f"//div[@id='board']//div[{tabelaID}]//div//div[2]//a//..//span[@class='list-card-title js-card-name']"
        )
    Resultado = []
    for div in divs:
        Texto = div.get_attribute('outerHTML')
        Resultado.append(Texto[Texto.find("(")+1:Texto.find(")")])
    
    return Resultado

###################################################################
#Instanciando o Firefox    
###################################################################
#url = str(input("URL: "))
url = False

if not url:
    url = "https://trello.com/b/0w2jL4Yc/404-trello-not-found"

option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)

driver.get(url)
driver.implicitly_wait(3)

###################################################################
#Obtendo os valores até o momento em ToDo/Doing/Done    
###################################################################
etapas = [[],[],[]]

etapas[0] = webScraping(3)
etapas[1] = webScraping(4) 
etapas[2] = webScraping(5)

driver.quit()

novasEtapas = []
for etapa in etapas:
    novosNumeros = []
    for numero in etapa:
        if str(numero) != "x":
            novosNumeros.append(numero)
    novasEtapas.append(novosNumeros)
etapas = novasEtapas

somas = []
for etapa in etapas:
    soma = 0
    for valor in etapa:
        soma = float(soma) + float(valor)
    somas.append(int(soma))

###################################################################
#Salvando Data colhida no dia da revisão
###################################################################    
with open('./historico.json', 'r') as f:
    data = json.load(f)

dia = mes = ano = 0
if not dia:
    dia = str(input("dia: "))
if not mes:
    mes = str(input("mes: "))
if not ano:
    ano = str(input("ano: "))
    
diaAtual = datetime(int(ano), int(mes), int(dia)).strftime('%d/%m/%Y') 

data["To-Do"].append(f"{somas[0]}")
data["Doing"].append(f"{somas[1]}")
data["Done"].append(f"{somas[2]}")
data["Dates"].append(f"{diaAtual}")

with open('./historico.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

###################################################################
#Gerando o Gráfico  
###################################################################    
plt.style.use('seaborn')

xAxis = np.arange(len(data['Dates']))
w = 0.25

toDoValues = []
for value in data['To-Do']:
    toDoValues.append(float(value))
doingValues = []
for value in data['Doing']:
    doingValues.append(float(value))
doneValues = []
for value in data['Done']:
    doneValues.append(float(value))

plt.bar(xAxis, toDoValues, w, label="To-Do")
plt.bar(xAxis+w, doingValues, w, label="Doing")
plt.bar(xAxis+w*2, doneValues, w, label="Done")
lns.Line2D(xAxis+w*2, doneValues, linewidth=0.75, label="Done")


plt.xlabel("Data")
plt.ylabel("Pontos")
plt.title("Pontos por tempo")

plt.xticks(xAxis+w, data['Dates'], rotation=45)
plt.tight_layout()
plt.legend()
plt.savefig('./images/graph.jpg')

###################################################################
#Enviando a imagem pro trello  
###################################################################  

fileToCard(key, token, image, cardid)