import random
import matplotlib.pyplot as plt

n=100

a=[random.randint(-10,10) for i in range(n)]
print('a=',a)

plt.plot(a,'bo')
plt.show()

