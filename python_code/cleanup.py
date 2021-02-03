import pandas as pd

inegi = pd.read_csv("inegi.csv")
df2 = pd.read_csv('data.csv')
df2 = df2[['location_name','date','est_infections_mean']]
df2 = df2[df2['location_name'].isin(inegi['location_name'])]
df2 = pd.merge(df2,inegi,on='location_name')

print(df2)

df2.to_csv('mexican_projections.csv')
