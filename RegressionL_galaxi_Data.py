import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression


fig, ax = plt.subplots()

# Load in data
galaxis = pd.read_csv("hubble_data.csv")
#print(galaxis.head())
x=galaxis[[0]]
y=galaxis[[1]]
#reg=LinearRegression().fit(galaxis["distance"],galaxis["recession_velocity"])
reg=LinearRegression().fit(x,y)

plt.scatter(galaxis["distance"],galaxis["recession_velocity"])
plt.plot(galaxis["distance"],galaxis["recession_velocity"])
plt.xticks()
plt.yticks()


# Show the plot
plt.show()