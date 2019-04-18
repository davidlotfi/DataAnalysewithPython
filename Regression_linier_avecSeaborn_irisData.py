import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
iris = sns.load_dataset("iris")

#print(iris.head())  #pour afficher le contenue de data
sns.jointplot("petal_length", "petal_width", data=iris,kind="reg" )

# Show the plot
plt.show()