import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r'/home/jpmagana/Documents/Research/Ping Ye Research/2017.clean.data.csv')
dfhousehold = df['HOUSEHOLD']
dfseniors = df['SENIORS']
dfchildren = df['CHILDREN']
dfcounty = df['COUNTY']
county = ['Hall','Dawson','Lumpkin','Gwinnett','Jefferson','White','Jackson','Barrow','Newton','Baldwin','Habersham','Forsyth','Banks']
household = [0 for x in range(len(county))]
seniors = [0 for x in range(len(county))]
children = [0 for x in range(len(county))]
for i in range(len(dfhousehold)):
    for j in range(len(county)):
        if dfcounty[i] == county[j]:
            household[j] = household[j] + dfhousehold[i]
            seniors[j] = seniors[j] + dfseniors[i]
            children[j] = children[j] + dfchildren[i]
        else:
            continue
print(county)
print(household)
print(seniors)
print(children)

fig = plt.figure()
ax = fig.add_axes([0,0,2,2])
ax.bar(county,household, color='b')
ax.set_xlabel('Counties')
ax.set_ylabel('Number of Individuals')
ax.set_title('2017 Total Usage By County')
plt.show()