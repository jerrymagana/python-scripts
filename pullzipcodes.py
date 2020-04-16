# ==========================================================================================================================
# Title: pullzipcodes.py
# Author: Jerry Paul Magaña
# Contact: jerrypaulmagana@gmail.com
# Description: Short script used to clean heterogeneous data in a column of an csv file.
# ==========================================================================================================================

import pandas as pd
df = pd.read_csv(r'/home/jpmagana/Documents/Research/Ping Ye Research/2017.addresses.csv')
addresses = df['ADDRESS']
zipcodes = [0 for i in range(len(addresses))]
for i in range(len(addresses)):
    zipcodes[i] = addresses[i][-5:]
for i in range(len(zipcodes)):
    if '3' not in zipcodes[i]:
        zipcodes[i] = 0
print(zipcodes)
f = open('/home/jpmagana/Documents/Research/Ping Ye Research/2017.zipcodes.txt','w+')
for i in range(len(zipcodes)):
    f.write('%s' % zipcodes[i])
f.close

