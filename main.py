
# coding: utf-8

# In[1]:

import Clases_animales as animales
import clase_territorio as territorio


# In[2]:

tamaño = [20,20]
lista_pre = ['p1','p2','p3']
lista_dep = ['d1','d2','d3']


# In[3]:

a = territorio.Territorio(tamaño,lista_pre,lista_dep)


# In[4]:

a.iniciar()


# ## Ahora tenemos que generar animales con IDs

# In[5]:

depredadores = []
for i in range(0,20):
    depredadores.append(animales.Depredador(i))
    


# In[6]:

presas = []
for i in range(0,50):
    presas.append(animales.Presa(i))
    


# In[8]:

b = territorio.Territorio(tamaño,presas,depredadores)


# In[9]:

b.iniciar()


# In[19]:

b.asignar_pos()


# In[ ]:



