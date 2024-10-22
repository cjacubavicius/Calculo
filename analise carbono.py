import pandas
import matplotlib.pyplot as plt
df = pandas.read_csv("Car Fuel and Emissions 2000-2013.csv")
print("=-=-=-= CORRELAÇÃO ENTRE ANO E CO2 -=-=-=-=\n")
print(df.sort_values(by="co2", ascending=False)[["year", "co2"]].corr("pearson"))
df.plot.scatter(x="year", y="co2")
plt.show()