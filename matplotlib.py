from matplotlib import pyplot as plt
x=[1,2,3,4,5,6]
y=[3**i+2 for i in x]
plt.plot(x,y)
plt.show()

###############

x=[1,2,3,4,5,6]
y=[2,3,4,5]
plt.plot(x,y)
plt.show()

plt.figure(figsize=(3,3))
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title("hii")
plt.plot(x,y,color='red',maker=0)
plt.plot(x,y,r++)
plt.plot(x,y,color="green",marker="^",linestyle="--")

plt.scatter(x,y,color="r",marker="+")

person=['a','s','d','f']
height=[123,234,534,564]
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.bar(person,height)
plt.show()


########sine wave

x=np.linespace(0,2*np.pi,100)
y=np.sin(x)

plt.plot(x,y,'r--',x,np.con(x),'b-')
plt.legend(['sine','cosine'])
plt.savefig(['it curve'])
plt.show()




from matlotlib import pyplot as plt
import numpy as np
import pandas as pd
import math

u=int(input)
a=int(input)
t=int(input)

v=[u+a*t]
d=[u*t + .5*a*t**2]
plt.plot(v,d)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()






