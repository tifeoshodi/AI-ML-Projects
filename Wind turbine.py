import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import pylab
import math
data= pd.read_csv('wind turbine data.txt')
print(data)

#Defining Constants
rho= 1.25 #kg/m^3
V=data['V(m/s)']
D=data['D(m)']
m= [] #mass flow rate list
W= [] #work output list

#print(V[:4])
#print(D[:4])

for i in D:
    A= (math.pi*(D**2))/4
    #print(A[:5])

m= rho*V*A
e= ((V*V)/2)
#print(e[:5])

W= (0.3*m*e)/1000

print("Work Output values(kW):\n", W[:5])
print("\nmass flow rate values(kg/s):\n", m[:5])
data['m(kg/s)']= m
data['W(kW)']= W
print(data)

fig, axes= plt.subplots(dpi=150)
axes.set_title('Work output(kW) against Velocity(m/s)')
axes.set_xlabel('V(m/s)')
axes.set_ylabel('W(kW)')
axes.plot(V[:3],W[:3], 'y')
axes.plot(V[4:7],W[4:7], 'r')
axes.plot(V[8:11],W[8:11], 'g')
axes.plot(V[12:15],W[12:15], 'b')


axes.legend(['D=20','D=40','D=60','D=80'], loc=2)
