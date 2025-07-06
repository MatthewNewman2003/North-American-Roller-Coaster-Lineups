import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("North American Coaster Lineups.csv")

sns.boxplot(x=df["Park"], y=df["Rating out of 10"] )

plt.show()
