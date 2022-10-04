import pandas as pd
import requests

r = requests.get('https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')
r = r.json()
df = pd.DataFrame.from_dict((r["cand"]))
df = df[["nm", "vap", "pvap"]][:4]
print(df)