import pandas as pd
import matplotlib.pyplot as plt

location = input("Location:") # Location to be monitored
location_population = float(input("Population (in thousands):"))*1000 # Population of the location
limit_a = (0.88,10) #(Percentile of people no longer infectious,days since symptoms)
limit_b = (0.95,15) 

people_day=float(input("People you meet in a day:"))#People you meet in a day

given_period=1
#Creating and filtering Dataframes
df=pd.read_csv("data.csv")
df2=df[['location_name','date','est_infections_mean']]
df3=df2[df2.location_name==location]
df3=df3.dropna()

#Calculation of the contagion vectors column
most_recent=df3.est_infections_mean.rolling(limit_a[1]-1).sum()
contagion_a=((df3.est_infections_mean.rolling(limit_b[1]-1).sum()-most_recent)
            *(1-limit_a[0]))
contagion_b=((df3.est_infections_mean.rolling(limit_b[1]).sum()-contagion_a)
            *(1-limit_b[0]))
df3['contagion_vectors']=most_recent+contagion_a+contagion_b

#Calcutation of the period's contagion probability 
df3['contagion_probability']=(df3['contagion_vectors']/location_population
                            *people_day*given_period)

print(df3)
df3.plot(x='date',y='contagion_probability')
plt.show()

