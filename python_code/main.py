import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
#import os
import json

#The code below was used to test the formula locally
"""
today=datetime.today().strftime('%Y-%m-%d')#Get today's date
location = input("Location: ") # Location to be monitored
people_day=1#People you meet in a day
"""
limit_a = (0.88,15) #(Percentile of people no longer infectious,days since symptoms)
limit_b = (0.95,20) 
given_period=1#Number of days on the time period (1 is one day, 30 is 30 days)

#Creating and filtering Dataframes
df=pd.read_csv("mexican_projections.csv")
df=df.dropna()

#Calculation of the contagion vectors column
most_recent=df.est_infections_mean.rolling(limit_a[1]-1).sum()
contagion_a=((df.est_infections_mean.rolling(limit_b[1]-1).sum()-most_recent)
            *(1-limit_a[0]))
contagion_b=((df.est_infections_mean.rolling(limit_b[1]).sum()-contagion_a)
            *(1-limit_b[0]))
df['contagion_vectors']=most_recent+contagion_a+contagion_b

#Uploading the Dataframe to the cloud
df.to_json(r'data_with_contagion_vectors.json')
#The below code was used to test the formula locally
"""
#Calcutation of the period's contagion probability 
df2['contagion_probability']=(df2['contagion_vectors']/df2['population']
                            *people_day*given_period)

ans = df2[df2.date==today]['contagion_probability'].values[0]
print(ans)
"""
