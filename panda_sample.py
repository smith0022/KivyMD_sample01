import pandas as pd
import re

df = pd.read_csv('/home/smith/Documents/pandas-master/pokemon_data.csv')

print(df.head(5))
#
# df_xlsx = pd.read_excel('pokemon_data.xlsx')
# print(df_xlsx.head(3))
#
# df = pd.read_csv('pokemon_data.txt', delimiter='\t')
#
# print(df.head(5))
#
# print(df['HP'])
# print(df.columns)
#
# # Read each Column
# print(df[['Name', 'Type 1', 'HP']])
#
# # Read Each Row
# print(df.iloc[0:4])
# for index, row in df.iterrows():
#     print(index, row['Name'])
# df.loc[df['Type 1'] == "Grass"]
# # Read a specific location (R,C)
# print(df.iloc[2,1])
# print(df.sort_values(['Type 1','Speed'],ascending=False))
# df['Total']=df.iloc[:,4:10].sum(axis=1)
# print(df)
# cals=list(df.columns.values)
# print(cals[-1])
# df=df[cals[0:4]+[cals[-1]]+cals[10:12]]
# print(df)
# df.to_csv("modified_poki.csv",index=False)
# df.to_txt("modified_poki.txt",index=False,sep='\t')
# n_df=df.loc[(df['Type 1']=='Grass') & (df['Type 2']=='Poison') & (df['HP']>70)]
# n_df.reset_index(drop=True,inplace=True)
# print(n_df)
# print(df.loc[df['Name'].str.contains('^pi[a:z]*',flags=re.I,regex=True)])
# df.loc[df['Type 1']=='Flamer','Type 1']='Fire'
# print(df.describe())
# f = lambda x: x*2
# print(df)