import pandas as pd
df = pd.read_csv('/home/gayathri/Documents/Projects/evv2gfcr/FrequencyGenerator/FrequencyData/germany_2020_01.csv.zip', index_col=0)

print(df)

#data = (f - 50)/1000
#data*1000 + 50 = f

df['Frequency'] = df['Frequency']/1000 + 50
print(df)