
# coding: utf-8


# In[1]:

import random as rand
import numpy as np


# In[6]:

class Territorio(object):
  
    def __init__(self, tamano, lista_pre, lista_dep): #ATRIBUTOS de territorio
        self.tamano = tamano              #un vector que define el tamano, sería la "diagonal del rect" en 2D
        self.lista_pre = lista_pre            #lista que contiene los objetos presa
        self.lista_dep = lista_dep            #lista que contiene los objetos depredadores
        self.num_pre = len(lista_pre)    #número de presas
        self.num_dep = len(lista_dep)    #número de depredadores  
    
    def asignar_pos(self):
        for i in range(self.num_dep):
            self.pos_dep[i][1] = (self.pos_dep[i][1]+self.pos_dep[i][0].moverse()[0]*self.pos_dep[i][0].velocidad)%tamano  #self.pos_dep[i][0] es el dep
            self.pos_dep[i][2] = (self.pos_dep[i][2]+self.pos_dep[i][0].moverse()[1]*self.pos_dep[i][0].velocidad)%tamano  #i que tiene su velocidad
        for i in range(self.num_pre):
            self.pos_pre[i][1] = (self.pos_pre[i][1]+self.pos_pre[i][0].moverse()[0]*self.pos_pre[i][0].velocidad)%tamano  #self.pos_pre[i][0] es la pre
            self.pos_pre[i][2] = (self.pos_pre[i][2]+self.pos_pre[i][0].moverse()[1]*self.pos_pre[i][0].velocidad)%tamano  #i que tiene su velocidad
#        pass

    def calcular_distancias(self):
#        x_pre_cerc = [0]*self.num_dep
#        y_pre_cerc = [0]*self.num_dep
        pre_mas_cerc = [0]*self.num_dep                            #lista de longitud  num_dep con las presas más cercanas
        for i in range(self.num_dep):                              #para cada depredador
            pre_vecinas = []
            dist_pre_vecinas = []
            for j in range(self.num_pre):
                dist = np.linalg.norm(np.array(self.pos_dep[i][1:])-np.array(self.pos_pre[j][1:])) #Calcula distancia entre
                if dist < self.pos_dep[i][0].vision:                                               #dep i y pre j
                    pre_vecinas.append(j)                          #arma lista de presas vecinas  
                    dist_pre_vecinas.append(dist)                  #arma lista de distancias de presas vecinas 
            if len(pre_vecinas) > 0: 
                k = dist_pre_vecinas.index(min(dist_pre_vecinas))  #encuentra el índice de la presa más cercana
                pre_mas_cerc[i] = self.pos_pre[k]
#                x_pre_cerc[i] = self.pos_pre[k][1]
#                y_mas_cerc[i] = self.pos_pre[k][|2]
            else:
#                x_pre_cerc[i] = None
#                y_mas_cerc[i] = None
                pre_mas_cerc[i] = None                             #
        return pre_mas_cerc                                        #devuelve lista de la presa más cercana de cada depredador
                                                                   #yo quiero la posicion de la presa para que el cazador se
                                                                   #mueva en esa dirección. Implementar en depredador.

    def iniciar(self):
        
        self.x_dep = []
        self.y_dep = []
        if self.num_dep > 0:
            for j in range(0, self.num_dep):
                self.x_dep.append(rand.random()*self.tamano[0])  #genera una posición random a partir de números
                self.y_dep.append(rand.random()*self.tamano[1])  #enteros dentro del rango 0 y el valor máximo de 
                                                                    #x o y, que están definidos por el vector tamano
        self.x_pre = []
        self.y_pre = []
        if self.num_pre > 0:
            for j in range(0, self.num_pre):
                self.x_pre.append(rand.random()*self.tamano[0])
                self.y_pre.append(rand.random()*self.tamano[1])

        
        self.pos_pre = [[self.lista_pre[i], self.x_pre[i], self.y_pre[i]] for i in range(self.num_pre)]  #genero la lista de
        self.pos_dep = [[self.lista_dep[i], self.x_dep[i], self.y_dep[i]] for i in range(self.num_dep)]  #listas[obj,x,y]
#        return (self.pos_pre, self.pos_dep)
   

     #self.pos_pre = list(zip(self.lista_pre, self.x_pre, self.y_pre))        #zip mergea en una lista nueva los elementos i de
     #self.pos_dep = list(zip(self.lista_dep, self.x_dep, self.y_dep))         #cada lista
    
        
    

    

