import pandas as pd
regione1= "Puglia"
download=pd.read_csv("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv")
regioni= download
area = regioni[regioni["denominazione_regione"]== regione1]
morti=(area["deceduti"])
totale_positivi=(area["totale_positivi"])
dimessi_guariti=(area["dimessi_guariti"])
pd.set_option('display.max_rows', None)
data=download.drop(columns=["lat","long","codice_regione",
      "ricoverati_con_sintomi","totale_ospedalizzati","terapia_intensiva",
      "isolamento_domiciliare","variazione_totale_positivi","tamponi",
      "casi_testati","nuovi_positivi","totale_positivi","note_it","note_en","stato","data"])


data["ratio"]=data["deceduti"].tail(21)/data["totale_casi"].tail(21)*100
format_dict = {'ratio': '{:.2%}'}
(data
 .style
 .format(format_dict)
 .hide_index()
 .highlight_max(color='lightgreen')
 .highlight_min(color='#cd4f39'))

print(data.tail(21))
