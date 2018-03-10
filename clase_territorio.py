# coding: utf-8
"""Clase Pacha

Desarrolladores:
    Antonella Marabotto, Camilo Amadio, Federico Hernandez, Carlos Raul Medrano.

Atributos:
    La **clase Pacha** posee 5 atributos:
        *tamano* (es el tamano de la caja de simulación)
        *lista_pre* (lista de objetos presas)  
        *lista_dep* (lista de objetos depredadores)
        *num_pre* (número de presas)
        *num_dep* (número de depredadores) 

Metodos:
    3 métodos:
        *iniciar()*: inicializa el territorio con posiciones aleatorias para las presas y los depredadores. Genera las listas pos_pre y pos_dep que contienen listas adentro de la forma [ID animal, pos x, pos y]
        *calcular_distancias()*: corre un loop sobre los i depredadores sobre las j presas y calcula las distancias entre los mismos. En el medio pregunta si el depredador i está en condiciones de comer a una presa, en funcion del atributo radio de vision ("rad_vis") de los depredadores. En caso afirmativo, llama al método del depredador, "comer(presa_a_ser_comida,lista_de_presas)" y actualiza las listas removiendo la presa. Luego, llama al metodo descansar(qué_depredador_descansará,tamano_del_ecosist),                                                             del depredador. Este método manda al depredador a su cueva y, en el paso siguiente el depredador aparece en su cueva en una posición random.
        *asignar_pos()*: teniendo en cuenta los atributos de cada animal, calcula un vector random para que se mueva y actualiza las posiciones.

"""




import random as rand
import numpy as np
import pydoc

class Pacha(object):
    """
    Attributes:
	tamaño=tamano	Dimensiones del territorio [x,y]
	lista_pre	Lista que contiene las presas
	lista_dep	Lista que contiene los depredadores
	num_pre		número de presas
	num_dep		número de depredadores
    """
    def __init__(self, tamano, lista_pre, lista_dep): #ATRIBUTOS de territorio
        """Defino los atributos de la clase pacha, el tamaño(tamano, dtype=float), la cantidad de 
        predadores (lista_dep, es una lista), y la cantidad de presas (lista_pre, es una lista).
        Parametros:
            tamano[x,y]:Tamano del territorio. Es un espacio bidimensional definido por x e y.
            lista_pre[]: Lista de presas.
            lista_dep[]: Lista de predadores             
"""
        self.tamano = tamano                  #un vector que define el tamano, sería la "diagonal del rect" en 2D
        self.lista_pre = lista_pre            #lista que contiene los objetos presa
        self.lista_dep = lista_dep            #lista que contiene los objetos depredadores
        self.num_pre = len(lista_pre)    #número de presas
        self.num_dep = len(lista_dep)    #número de depredadores
        self.pos_cueva = []
        self.cueva_ID = []  
        self.despl_dep = []
        self.despl_dep_ID = []
    
    def asignar_pos(self):







        """Define posiciones nuevas para presas y predadores. Toma en cuenta su velocidad y su
        posicion anterior. En el caso de los predadores existen dos posibilidades para asignar una
        posicion. Las presas siempre son reasignadas en funcion del metodo moverse() de la clase
        animal.
        Caso(1). El predador no comio en la instancia anterior. Entonces asigna una nueva posicion
        en funcion de su posicion anterior y la direccion de los vectores generados en el metodo
        moverse() de la clase Animal; si es una presa a ese vector lo amplifica por el parametro 
        velocidad dada a la presa; si es un predador a ese vector lo amplifica por el parametro
        velocidad de los depredadores.
        Caso(2). El predador en la instancia anterior comio una presa. Entonces la nueva posicion
        del predador estara confinada a una region donde las presas no puede acceder. 
"""


####   DEPREDADORES

        for i in range(self.num_dep):

            if self.lista_dep[i] in self.cueva_ID:         #si el dep i está en cueva_ID (o sea, comió y vuelve a su cueva)
               z = self.cueva_ID.index(self.lista_dep[i])  #busca el índice del depredador i en la lista cueva_ID 
               self.pos_dep[i] = self.pos_cueva[z]
            
            elif self.lista_dep[i] in self.despl_dep_ID:          #si el dep i caza entonces se mueve con el vector
               z = self.despl_dep_ID.index(self.lista_dep[i])     #desplazamiento (el % es por las cond. period)
               self.pos_dep[i][1] = (self.pos_dep[i][1]+self.despl_dep[z][1]*self.lista_dep[i].velocidad)%self.tamano[0]
               self.pos_dep[i][2] = (self.pos_dep[i][2]+self.despl_dep[z][2]*self.lista_dep[i].velocidad)%self.tamano[1]

            else:           

                self.pos_dep[i][1] = (self.pos_dep[i][1]+self.pos_dep[i][0].moverse()[0]*self.pos_dep[i][0].velocidad)%self.tamano[0]  #self.pos_dep[i][0] es el dep
                self.pos_dep[i][2] = (self.pos_dep[i][2]+self.pos_dep[i][0].moverse()[1]*self.pos_dep[i][0].velocidad)%self.tamano[1]  #i que tiene su velocidad
        

        self.pos_cueva = []         #vacía las listas para el próximo paso
        self.cueva_ID = []
        self.despl_dep = []
        self.despl_dep_ID = []

###   PRESAS

        for i in range(self.num_pre):
            self.pos_pre[i][1] = (self.pos_pre[i][1]+self.pos_pre[i][0].moverse()[0]*self.pos_pre[i][0].velocidad)%self.tamano[0]  #self.pos_pre[i][0] es la pre
            self.pos_pre[i][2] = (self.pos_pre[i][2]+self.pos_pre[i][0].moverse()[1]*self.pos_pre[i][0].velocidad)%self.tamano[1]  #i que tiene su velocidad




    def calcular_distancias(self):

        """Funcion que calcula la distancia minima entre un depredador y alguna presa. Distingue entre las presas que están 
          dentro del rango de visión y la que ya cayó dentro del rango de comer.


           Return: Pre_mas_cerc[].


        """
          
        pre_mas_cerc = [0]*self.num_dep                            #lista de longitud  num_dep con las presas más cercanas
        for i in range(self.num_dep):                              #para cada depredador
            
#            print(i,'  LAMAO') 

            pre_vecinas = []
            dist_pre_vecinas = []
            componentes_dist_pre_v = []
            for j in range(self.num_pre):
                #dist = np.linalg.norm(np.array(self.pos_dep[i][1:])-np.array(self.pos_pre[j][1:])) #Calcula distancia entre
                dx = -self.pos_dep[i][1]+self.pos_pre[j][1]
                dy = -self.pos_dep[i][2]+self.pos_pre[j][2]
                
#                print(i, j, dx)

                if dx > self.tamano[0]*0.5:
                    dx += -self.tamano[0]
                if dx <= -self.tamano[0]*0.5:
                    dx += self.tamano[0]
                if dy > self.tamano[1]*0.5:
                    dy += -self.tamano[1]
                if dy <= -self.tamano[1]*0.5:
                    dy += self.tamano[1]

                dist = np.sqrt(dx*dx+dy*dy)
                if dist < self.pos_dep[i][0].vision:                                               #dep i y pre j
                    pre_vecinas.append(j)                          #arma lista de presas vecinas  
                    dist_pre_vecinas.append(dist)                  #arma lista de distancias de presas vecinas 
                    componentes_dist_pre_v.append([dx,dy])

            if len(pre_vecinas) > 0:
                l = dist_pre_vecinas.index(min(dist_pre_vecinas))            #encuentra el índice de distancia minima
                                                                             #entre una presa "j" y el dep "i". 
                k = pre_vecinas[l]                                           #Busca la presa presa "j" en la lista de 
                                                                             #presas vecinas.
                                                                             # distancia al predador i
                if min(dist_pre_vecinas) < self.lista_dep[i].rad_comer: 

                    self.lista_pre = self.lista_dep[i].comer(k, self.lista_pre)    
                    del self.pos_pre[k]                                          
                    self.num_pre = len(self.lista_pre)                           
                    pos_cueva_dep = self.lista_dep[i].descansar(self.lista_dep[i], self.tamano)  #lista [id_dep,cuevax,cuevay] 
                    self.pos_cueva.append(pos_cueva_dep)                                         #lista de listas
                    self.cueva_ID.append(self.lista_dep[i])                               #estas listas va a usar asignar_pos
             
                elif min(dist_pre_vecinas) < self.lista_dep[i].vision:
                    self.despl_dep.append(self.lista_dep[i].cazar(self.lista_dep[i],componentes_dist_pre_v[l])) #llamo a cazar 
                    self.despl_dep_ID.append(self.lista_dep[i])                                   # y le paso las componentes 
                                                                                                  # del vector desplazamiento
                                                                                          #estas listas va a usar asignar_pos

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
                self.x_dep.append(rand.random()*(self.tamano[0]/4)+self.tamano[0]/4)  #genera una posición random a partir de números
                self.y_dep.append(rand.random()*(self.tamano[1]/4)+self.tamano[1]/4)  #enteros dentro del rango 0 y el valor máximo de 
                                                                    #x o y, que están definidos por el vector tamano
        self.x_pre = []
        self.y_pre = []
        if self.num_pre > 0:
            for j in range(0, self.num_pre):
                self.x_pre.append(rand.random()*(self.tamano[0]/6)+self.tamano[1]/2)
                self.y_pre.append(rand.random()*(self.tamano[1]/6)+self.tamano[1]/2)

        
        self.pos_pre = [[self.lista_pre[i], self.x_pre[i], self.y_pre[i]] for i in range(self.num_pre)]  #genero la lista de
        self.pos_dep = [[self.lista_dep[i], self.x_dep[i], self.y_dep[i]] for i in range(self.num_dep)]  #listas[obj,x,y]
        #estas dos líneas hacen lo que haría un zip pero sin el problema de las tuplas

#        return (self.pos_pre, self.pos_dep)
   

