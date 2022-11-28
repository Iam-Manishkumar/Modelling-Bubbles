#Manish Kumar Patterns in comunication ecosystems A3 Bubble model

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats 
import random

# Parameters
s=0
nosmootD6 = 0.4
d6 = nosmootD6/(1+pow(nosmootD6,(2/3)))
listInf = []
listCont = []
indx = []
smoothing = 0.3
avcontag = 1.0

listD6 = []
#lists
for x in range(250):
    listD6.append(stats.lognorm(0.38, scale=np.exp(0)).ppf(random.uniform(0, 1)))
meanD6 = sum(listD6)/len(listD6)
sd_D6 = np.std(listD6)

listE6 = listD6/meanD6
meanE6 = sum(listE6)/len(listE6)
sd_E6 = np.std(listE6)

listF6 = 1+(nosmootD6/sd_E6)*(listE6 -1)
meanF6 = sum(listF6)/len(listF6)
sd_F6 = np.std(listF6)

for x in range(249):
    if x == 0:
        listCont.append(avcontag*(1-smoothing) + smoothing*listF6[x])
    else:
        listCont.append(listCont[x-1]*(1-smoothing)+(smoothing)*listF6[x]*avcontag)

meanCont = sum(listCont)/len(listCont)
sd_Cont = np.std(listCont)

for x in range(249):
    if x == 0:
        listInf.append(listCont[x])
    else:
        listInf.append(listCont[x]*listInf[x-1])
    indx.append(x)

plt.figure(1)
plt.plot(indx,listCont, 'b', label = "Contagiousness")
plt.plot(indx,listInf,'r-o', label = "Infections")
plt.title("Graph for infection model")
plt.ylabel("Infected population")
plt.xlabel("Time steps")
plt.legend(loc="upper left")

plt.show()
