import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data={
    "Months":["January","February","March","April","May","June","July"],
    "USA": [3.0, 2.8, 2.4, 2.3, 2.4, 2.5,2.6],
    "India":[3.34,3.16,2.82,2.59,2.95,2.94,2.93],
    "Japan":[4.0,3.7,3.6,3.6,3.5,3.5,3.4]
}
df=pd.DataFrame(data)
print(df)
plt.plot(df["Months"], df["USA"], 'b.-', label='USA')
plt.plot(df["Months"], df["India"], 'r.-', label='India')
plt.plot(df["Months"], df["Japan"], 'g.-', label='Japan')
plt.legend()
plt.ylabel("Inflation Percentage")
plt.xlabel("Months")
plt.show()
plt.savefig("inflation_graph.png",dpi=300)
#df.to_csv("raw_data.csv")