import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv("netflixTitles.csv")


type_counts = data['type'].value_counts()


plt.bar(type_counts.index, type_counts.values, width=0.5, color="orange")

plt.xlabel('Type')
plt.ylabel('Amount')
plt.title('Number of Titles by Type')


plt.savefig('chart')
plt.show()


