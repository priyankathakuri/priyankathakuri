
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("worldometer_data.csv")
font1={'family':'serif','color':'blue','size':20}
font2={'family':'serif','color':'darkred','size':15}
plt.plot(df['TotalCases'], df['Population'])
plt.title("COVID 19",fontdict=font1)
plt.xlabel("POPULATION",fontdict=font2)
plt.ylabel("TOTALCASE",fontdict=font2)
plt.show()