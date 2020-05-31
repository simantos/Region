import pandas as pd
regione1= "Puglia"
download=pd.read_csv("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv")
regioni= download
area = regioni[regioni["denominazione_regione"]== regione1]
morti=(area["deceduti"])
totale_positivi=(area["totale_positivi"])
dimessi_guariti=(area["dimessi_guariti"])

