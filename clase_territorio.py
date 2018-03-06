
# coding: utf-8

# In[1]:

import random as rand


# In[6]:

class Territorio(object):
  
    def __init__(self, tamaño, lista_pre, lista_dep): #ATRIBUTOS de territorio
        self.tamaño = tamaño              #un vector que define el tamaño, sería la "diagonal del rect" en 2D
        self.lista_pre = lista_pre            #lista que contiene los objetos presa
        self.lista_dep = lista_dep            #lista que contiene los objetos depredadores
        self.num_pre = len(lista_pre)    #número de presas
        self.num_dep = len(lista_dep)    #número de depredadores  
    
    def asignar_pos(self):
        for i in range(self.num_dep):
            self.pos_dep[i][1] += self.pos_dep[i][0].moverse()[0]
            self.pos_dep[i][2] += self.pos_dep[i][0].moverse()[1]
        for i in range(self.num_pre):
            self.pos_pre[i][1] += self.pos_pre[i][0].moverse()[0]
            self.pos_pre[i][2] += self.pos_pre[i][0].moverse()[1]
#        pass
                
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

        
        self.pos_pre = [[self.lista_pre[i], self.x_pre[i], self.y_pre[i]] for i in range(self.num_pre)]  #genero la lista de
        self.pos_dep = [[self.lista_dep[i], self.x_dep[i], self.y_dep[i]] for i in range(self.num_dep)]  #listas[obj,x,y]
        return (self.pos_pre, self.pos_dep)
   

     #self.pos_pre = list(zip(self.lista_pre, self.x_pre, self.y_pre))        #zip mergea en una lista nueva los elementos i de
     #self.pos_dep = list(zip(self.lista_dep, self.x_dep, self.y_dep))         #cada lista
    
        
    

    

