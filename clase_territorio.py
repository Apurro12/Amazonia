
# coding: utf-8

# In[1]:

import random as rand


# In[6]:

class Territorio(object):
  
    def __init__(self, tamaño, lista_pre, lista_dep): #ATRIBUTOS de territorio
        self.tamaño = tamaño              #un vector que define el tamaño, sería la "diagonal del rect" en 2D
        self.lista_pre = lista_p            #lista que contiene los objetos presa
        self.lista_dep = lista_d            #lista que contiene los objetos depredadores
        self.num_pre = len(lista_p)    #número de presas
        self.num_dep = len(lista_d)    #número de depredadores  
    
    def asignar_pos(self):
        self.pos_dep[:][1] += self.pos_dep[:][0].moverse().mov[0]
        self.pos_dep[:][2] += self.pos_dep[:][0].moverse().mov[1]
        self.pos_pre[:][1] += self.pos_pre[:][0].moverse().mov[0]
        self.pos_pre[:][2] += self.pos_pre[:][0].moverse().mov[1]
        pass
                
    def iniciar(self):
        
        self.x_dep = []
        self.y_dep = []
        if self.num_dep > 0:
            for j in range(0, self.num_dep):
                self.x_dep.append(rand.random()*self.tamaño[0])  #genera una posición random a partir de números
                self.y_dep.append(rand.random()*self.tamaño[1])  #enteros dentro del rango 0 y el valor máximo de 
                                                                    #x o y, que están definidos por el vector tamaño
        self.x_pre = []
        self.y_pre = []
        if self.num_pre > 0:
            for j in range(0, self.num_pre):
                self.x_pre.append(rand.random()*self.tamaño[0])
                self.y_pre.append(rand.random()*self.tamaño[1])

        
        self.pos_pre = list(zip(lista_pre, self.x_pre, self.y_pre))         #zip mergea en una lista nueva los elementos i de
        self.pos_dep = list(zip(lista_dep, self.x_dep, self.y_dep))         #cada lista
        return (self.pos_pre, self.pos_dep)
    
        
    

    


# In[10]:

tamaño = [20,20]
lista_pre = ['p1','p2','p3']
lista_dep = ['d1','d2','d3']


# In[11]:

a = Territorio(tamaño,lista_p,lista_d)


# In[12]:

a.iniciar()


# In[14]:

a.pos_dep


# In[15]:

a.x_pre


# In[ ]:



