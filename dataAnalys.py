import numpy as np
a=np.array([0,30,45,60,90])
b=np.array([[0,2,3,4,5,6],  #matrice
           [7,8,9,77,88,99]])
print(a)
print(b)
print("----------------------------------------")
c=np.arange(12).reshape(4,3)
print(c)
print("----------------------------")
d=np.full((10,20),5)

print(d)

print(f" la dimention de table :{d.ndim}")
print(f" la taille de table :{d.size}")
print(f" la form de table :{d.shape}")
print(f" la type de table :{d.dtype}")
print(f"element dans l 1er ligne est 6eme colones  {d[0,6]}")
d[0,6]=7
d[1,6]=8
d[2,6]=1
print(d)