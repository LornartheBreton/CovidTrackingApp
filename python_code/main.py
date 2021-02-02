import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import os

today=datetime.today().strftime('%Y-%m-%d')
location = input("Location: ") # Location to be monitored
limit_a = (0.88,15) #(Percentile of people no longer infectious,days since symptoms)
limit_b = (0.95,20) 
people_day=float(input("People you meet in a day:"))#People you meet in a day

given_period=1
#Creating and filtering Dataframes
df=pd.read_csv("mexican_projections.csv")
df2=df[df.location_name==location]
df2=df2.dropna()

#Calculation of the contagion vectors column
most_recent=df2.est_infections_mean.rolling(limit_a[1]-1).sum()
contagion_a=((df2.est_infections_mean.rolling(limit_b[1]-1).sum()-most_recent)
            *(1-limit_a[0]))
contagion_b=((df2.est_infections_mean.rolling(limit_b[1]).sum()-contagion_a)
            *(1-limit_b[0]))
df2['contagion_vectors']=most_recent+contagion_a+contagion_b

#Calcutation of the period's contagion probability 
df2['contagion_probability']=(df2['contagion_vectors']/df2['population']
                            *people_day*given_period)

ans = df2[df2.date==today]['contagion_probability'].values[0]
print(ans)

