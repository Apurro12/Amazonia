
# coding: utf-8

__author__      = "Antonella Marabotto, Camilo Amadio, Federico Hernandez, Carlos Raul Medrano "


import random as rand
import numpy as np
import pydoc

class Territorio(object):
    """
    Attributes:
	tamaño=tamano	Dimensiones del territorio [x,y]
	lista_pre	Lista que contiene las presas
	lista_dep	Lista que contiene los depredadores
    """
    def __init__(self, tamano, lista_pre, lista_dep): #ATRIBUTOS de territorio
        self.tamano = tamano                  #un vector que define el tamano, sería la "diagonal del rect" en 2D
        self.lista_pre = lista_pre            #lista que contiene los objetos presa
        self.lista_dep = lista_dep            #lista que contiene los objetos depredadores
        self.num_pre = len(lista_pre)    #número de presas
        self.num_dep = len(lista_dep)    #número de depredadores  
    
    def asignar_pos(self):
        "Define posiciones nuevas para presas y predadores. Toma en cuenta su velocidad y su posicion anterior"
        for i in range(self.num_dep):
            self.pos_dep[i][1] = (self.pos_dep[i][1]+self.pos_dep[i][0].moverse()[0]*self.pos_dep[i][0].velocidad)%self.tamano  #self.pos_dep[i][0] es el dep
            self.pos_dep[i][2] = (self.pos_dep[i][2]+self.pos_dep[i][0].moverse()[1]*self.pos_dep[i][0].velocidad)%self.tamano  #i que tiene su velocidad
        for i in range(self.num_pre):
            self.pos_pre[i][1] = (self.pos_pre[i][1]+self.pos_pre[i][0].moverse()[0]*self.pos_pre[i][0].velocidad)%self.tamano  #self.pos_pre[i][0] es la pre
            self.pos_pre[i][2] = (self.pos_pre[i][2]+self.pos_pre[i][0].moverse()[1]*self.pos_pre[i][0].velocidad)%self.tamano  #i que tiene su velocidad

    def calcular_distancias(self):
        """Funcion que calcula la distancia minima distancia entre un predador y alguna presa.
           Return: Pre_mas_cerc.

        """
          
        pre_mas_cerc = [0]*self.num_dep                            #lista de longitud  num_dep con las presas más cercanas
        for i in range(self.num_dep):                              #para cada depredador
            pre_vecinas = []
            dist_pre_vecinas = []
            for j in range(self.num_pre):
                #dist = np.linalg.norm(np.array(self.pos_dep[i][1:])-np.array(self.pos_pre[j][1:])) #Calcula distancia entre
                dx = np.linalg.norm(np.array(self.pos_dep[i][1])-np.array(self.pos_pre[j][1]))
                dy = np.linalg.norm(np.array(self.pos_dep[i][2])-np.array(self.pos_pre[j][2]))

                if (dx > self.tamano[0]*0.5):
                    dx -= self.tamano[0]
                if (dx <= -self.tamano[0]*0.5):
                    dx += self.tamano[0]
                if (dx > self.tamano[1]*0.5):
                    dy -= self.tamano[1]
                if (dx <= -self.tamano[1]*0.5):
                    dy += self.tamano[1]

                dist = np.sqrt(dx*dx+dy*dy)
                if dist < self.pos_dep[i][0].vision:                                               #dep i y pre j
                    pre_vecinas.append(j)                          #arma lista de presas vecinas  
                    dist_pre_vecinas.append(dist)                  #arma lista de distancias de presas vecinas 

            if len(pre_vecinas) > 0: 
                k = dist_pre_vecinas.index(min(dist_pre_vecinas))            #encuentra el índice de la presa más cercana
                self.lista_pre = self.lista_dep[i].comer(k, self.lista_pre)       #actualizo lista_pre
                del self.pos_pre[k]                                          #actualizo lista pos_pre
                self.num_pre = len(self.lista_pre)                           #actualizo el num de presas en el territorio 
#               pre_mas_cerc[i] = self.pos_pre[k]
                
#            else:
#                pre_mas_cerc[i] = None                             #
#        return pre_mas_cerc                                        #devuelve lista de la presa más cercana de cada depredador
                                                                   #yo quiero la posicion de la presa para que el cazador se
                                                                   #mueva en esa dirección. Implementar en depredador.

    def iniciar(self):
        "Inicializa las posiciones de los animales en el territorio."
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
        #estas dos líneas hacen lo que haría un zip pero sin el problema de las tuplas

#        return (self.pos_pre, self.pos_dep)
   

