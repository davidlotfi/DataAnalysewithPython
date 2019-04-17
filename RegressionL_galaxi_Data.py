import matplotlib.pyplot as plt
import pandas as pd

fig, ax = plt.subplots()
# Load in data
galaxis = pd.read_csv("hubble_data.csv")

# Create violinplot
ax.violinplot(galaxis["distance"], vert=False)

# Show the plot
plt.show()