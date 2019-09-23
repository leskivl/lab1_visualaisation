import random
import matplotlib.pyplot as plt
import math

class Data:
  def get_data(self,a,b,amount):
    if amount<=0: amount=40
    self.n=amount
    r_list=[random.randint(a,b) for i in range(amount)]
    return r_list
  
  def show_graph(self,data):
    plt.plot(data, 'bo', self.average(data), 'go', \
             self.sigma(data), 'ro')
    plt.xlabel('order number')
    plt.ylabel('array')
    plt.title('graph of random array')
    plt.legend(['random number','mean','variance'])
    plt.show()
    
  def average(self,a):
    sum_a=sum(a)
    x_average=sum_a/self.n
    return x_average
  
  def disp(a):
  d=0
  for  i in range(self.n):
    d+=(a[i]-self.average(a))**2
   return d/self.n
  
  def sigma(self, a):
    return math.sqrt(self.disp(a))
  
  
a = Data()

r_list = a.get_data(-10, 10, 0)
avg = a.average(r_list)
d = a.disp(r_list)
s = a.sigma(r_list)
graph = a.show_graph(r_list)

print("random_list ", r_list)
print('average=', avg)
print('dispertion=', d)
print('sigma=', s)

