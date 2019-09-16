import random
import matplotlib.pyplot as plt
import math

n=100

a=[random.randint(-10,10) for i in range(n)]
print('a=',a)

plt.plot(a,'bo')
plt.show()

def x_average(a):
  sum_a=sum(a)
  x_average=sum_a/n
  return x_average

avg=x_average(a)
print('average=',avg)

def disp(a):
  d=0
  for  i in range(n):
    d+=(a[i]-avg)**2
    return d
 
d=disp(a)
print('disp=',d)
    
