
# coding: utf-8

# In[1]:

import Clases_animales as animales
import clase_territorio as territorio
import matplotlib.pyplot as plt
import numpy as np

#get_ipython().magic('matplotlib inline')


# In[2]:

tamano = [50,50]


# In[3]:

depredadores = []
for i in range(0,5):
    depredadores.append(animales.Depredador(i))
    


# In[4]:

presas = []
for i in range(0,50):
    presas.append(animales.Presa(i))
    


# In[5]:

pacha = territorio.Territorio(tamano,presas,depredadores)


# In[6]:

pacha.iniciar()



plt.axis([0,tamano[0],0,tamano[1]])
plt.ion()

for i in range(100):
    plt.axis([0,tamano[0],0,tamano[1]])
    pacha.calcular_distancias()
    pacha.asignar_pos()
    plt.scatter([pacha.pos_dep[i][1] for i in range(pacha.num_dep)], [pacha.pos_dep[i][2] for i in range(pacha.num_dep)], c='r')
    plt.scatter([pacha.pos_pre[i][1] for i in range(pacha.num_pre)], [pacha.pos_pre[i][2] for i in range(pacha.num_pre)], c='b')
    plt.savefig('paso'+str(i)+'.png', dpi=100)
    plt.pause(0.5)
    plt.cla()

