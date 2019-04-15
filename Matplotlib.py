import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,10,100)

plt.plot(x,x ,label='linear')
plt.legend()
plt.show()   #pour afficher la figure


n=1024
x=np.random.normal(0,1,n)
y=np.random.normal(0,1,n)

plt.scatter(x,y)
plt.show()