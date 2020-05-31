import pandas as pd
import matplotlib.pyplot as plt 
regione1= "Puglia"
regione2="Sicilia"
regione3="Lombardia"
download=pd.read_csv("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv")
regioni= download
area = regioni[regioni["denominazione_regione"]== regione1]
morti=(area["deceduti"])
totale_positivi=(area["totale_positivi"])
dimessi_guariti=(area["dimessi_guariti"])



fig = plt.figure(figsize=(12,10))

fig1 = plt.subplot(1,1,1)
plt.yticks(fontsize=20)

#plt.yscale("log")
#plt.title(regione1 + " / " +regione2, fontsize = 35)

fig1.plot(morti, marker='D', label='Decessi '+ regione1)
fig1.plot(totale_positivi, marker='D',label='Totale positivi '+ regione1)
fig1.plot(dimessi_guariti, marker='D',label='Dimessi guariti '+ regione1)
plt.show()
