# -*- coding: utf-8 -*-

__author__      = "Antonella Marabotto, Camilo Amadio, Federico Hernandez, Carlos Raul Medrano "

import pydoc
import random as rand
import numpy as np


"""
En este archivo se encuentran tres clases: **Clase Animales, Clase Depredador y Clase Presa**.
Las ultimas dos clases heredan metodos y atributos de la clase animales.

"""
"""
La **clase Animales** posee 2 atributos:
				
"""
class Animales(object):
    def __init__(self,velocidad=1.,vision=1.):
        """
        :(1)*Velocidad*:define la amplificacion del vector de movimiento unitario. 
	:(2)*Vision*: Define el rango con que el animal detecta a otros.
        :return: None
        """
        self.velocidad = velocidad
        self.vision = vision
#        self.hambre = hambre
#        self.vida = vida

    def moverse(self):
        """
        La clase Animales posee 1 metodo:
	:(1)*moverse()*: devuelve un vector aleatorio que define la direccion de movimiento del animal.
        """
        self.dir_mov = [0,0]
        theta = rand.random() # Defino como theta un angulo aleatorio calculado aleatoriamente respecto del eje x. Define la direccion del movimiento
        self.dir_mov[0] = np.cos(theta*2.*np.pi)#Defino coordenada x del vector
        self.dir_mov[1] = np.sin(theta*2.*np.pi)#Defino coordenada y del vector 
        return self.dir_mov#devuelve un vector con coordenadas x e y que definen la direccion del movimiento.

        
#Tenemos que definir el metodo vision


class Presa(Animales):
    """
    :La **clase Presa** posee 3 atributos:
    :(1 y 2)*Vision y Velocidad*: heredados de Animales, que se re-inicializan en la clase presa.
    :(3)*ID*: Un identificador del objeto presa.
        """
    def __init__(self,ID):
        Animales.__init__(self)
        self.velocidad *= 1#Defino la velocidad de la presa
        self.vision *= 1#Defino el rango de vision de la presa
        self.ID = ID#Defino el ID de la presa


"""
La **clase Depredador** posee 4 atributos:
				(1 y 2)*Vision y Velocidad* heredados de Animales, que se re-inicializan en la clase presa.
				(3)*ID*: Un identificador del objeto depredador.
				(4)*rad_comer*: Radio en el cual un depreador come a la presa.
La **clase Depredador** posee 1 metodo:
				(1) *Comer()*:Elimina de la lista de presas la presa que fue comida por el depredador		
"""
class Depredador(Animales):
    def __init__(self,ID):
        Animales.__init__(self)
        self.velocidad *= 3
        self.vision *= 9 
        self.rad_comer = self.vision/3. 
        self.ID = ID
        
    def comer(self,ID_pre_com,lista): # Le pasa el ID de la presa a comer en ID_pre_com, junto con la lista
        del lista[ID_pre_com]         # Elimina el elemento list_pre_com de la lista.
        return lista

        


#self.number_dep = territorio.num_dep
#radio_vis = 4.
#for p in lista_dep:
#    aux = p.ver(terr,radio_vis) #Llama al elemento cero de la lista p (que es un elementeo de lista_dep)
    
#preguntar a charly como guardan los objetos de lista_dep en el main

