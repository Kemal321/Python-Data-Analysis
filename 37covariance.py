import numpy as np

x = [45, 37, 42, 35, 39]
y = [38, 31, 26, 28, 33]

data = np.array([x,y])

print(data)

varco = np.cov(data,bias=True) # bias true olursa popülasyon üzerinden işlem yapar false ise örneklem üzerinden işlem yapar. 

print(varco)

# karşılaştırmak için varyansları hesaplayacak olursak zaten diagonldaki değerler çıkacaktır. 
print(np.var(x),np.var(y))
