import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
gas=pd.read_csv("/home/smith/Downloads/matplotlib_tutorial-master/gas_prices.csv")
plt.title(" Grades ",fontdict={"fontweight":"bold","fontsize":"15"})
countries=gas.columns
print(countries)
for x in range(1,35):

plt.plot(gas.Year, gas[x], marker="o", label=str(x))
plt.xticks(gas.Year[::3])
plt.ylabel("$dollar$")
plt.xlabel("Year")
plt.legend(loc='upper left')
plt.savefig("gas_prices_fig",dpi=1200)
# plt.show()
# fifa=pd.read_csv("/home/smith/Downloads/matplotlib_tutorial-master/fifa_data.csv")
# #fifa=fifa.iloc[:,2:6:3]
# #print(fifa[fifa['Nationality']=="India"])
# #bins=[0,10,20,30,40,50,60,70,80,90,100]
# bins=[40,50,60,70,80,90,100]
# plt.hist(fifa.Overall,bins=bins)
# plt.xticks(bins)
# plt.title("Fifa")
# plt.ylabel("Number Of Players")
# plt.xlabel("Player's Skill")
plt.show()
