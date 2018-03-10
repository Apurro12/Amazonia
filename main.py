# coding: utf-8
"""Proyecto Amazonia

Este programa genera un ecosistema. La dinamica de los objetos responde a la interaccion de presas y predadores. Ambos son libres de moverse por el territorio (Todos los atributos y metodos del mismo se encuentran en el archivo "clase_territorio.py"), las predadores tienen la capacidad de comer a las presas y de perseguirlas (Todos los atributos y metodos de presas y predadores se encuentran el archivo "Clases_animales.py").

Desarrolladores: 
    Antonella Marabotto, Camilo Amadio, Federico Hernandez, Carlos Raul Medrano

Parametros:
    tamano[]: Tamano de el territorio(pacha)
    depredadores[]: Lista de depredadores
    presas[]: Lista de presas
     
"""


import Clases_animales as animales
import clase_territorio as territorio
import matplotlib.pyplot as plt
import numpy as np
import pydoc

#get_ipython().magic('matplotlib inline')


# In[2]:
#El usuario define el tamaño del territorio
tamano = [50,50]


# In[3]:
#El usuario define la cantidad de depredadores que se van a generar
depredadores = []
for i in range(2):
    depredadores.append(animales.Depredador(i))
    


# In[4]:
#El usuario define el numero de presas que se van a gerenar
presas = []
for i in range(15):
    presas.append(animales.Presa(i))
    


# In[5]:
#Instanciamos el objeto territorio: inicializamos el tamaño, el numero de presas y predadores
pacha = territorio.Pacha(tamano,presas,depredadores)


# In[6]:

#Definimos las posiciones de presas y predadores
pacha.iniciar()


#Visualizacion de la dinamica del ecosistema
plt.axis([0,tamano[0],0,tamano[1]])
plt.ion()

for i in range(1000):
    plt.axis([0,tamano[0],0,tamano[1]])
    pacha.calcular_distancias()
    pacha.asignar_pos()
    plt.scatter([pacha.pos_dep[i][1] for i in range(pacha.num_dep)], [pacha.pos_dep[i][2] for i in range(pacha.num_dep)], c='r')
    plt.scatter([pacha.pos_pre[i][1] for i in range(pacha.num_pre)], [pacha.pos_pre[i][2] for i in range(pacha.num_pre)], c='b')
#    plt.savefig('paso'+str(i)+'.png', dpi=100)
    plt.pause(0.1)
    plt.cla()

