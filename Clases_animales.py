# -*- coding: utf-8 -*-

__author__      = "Antonella Marabotto, Camilo Amadio, Federico Hernandez, Carlos Raul Medrano "

import pydoc
import random as rand
import numpy as np


"""
En este archivo se encuentran tres clases: __Clase Animales__, __Clase Depredador__ y __Clase Presa__.
Las ultimas dos clases heredan metodos y atributos de la clase animales.

"""
"""
La __clase Animales__ posee 2 atributos:
				
"""
class Animales(object):
    """
    Attributes:
        (1)_Velocidad_		Define la amplificacion del vector de movimiento unitario. 
	(2)_Vision_ 		Define el rango con que el animal detecta a otros.
    """
    def __init__(self,velocidad=0.1,vision=1.):
        self.velocidad = velocidad
        self.vision = vision
#        self.hambre = hambre
#        self.vida = vida

    def moverse(self):
        "El metodo moverse gener un vector aleatorio que define la direccion del movimiento"
        self.dir_mov = [0,0]
        theta = rand.random() # Defino como theta un angulo aleatorio calculado aleatoriamente respecto del eje x. Define la direccion del movimiento
        self.dir_mov[0] = np.cos(theta*2.*np.pi)#Defino coordenada x del vector
        self.dir_mov[1] = np.sin(theta*2.*np.pi)#Defino coordenada y del vector 
        return self.dir_mov#devuelve un vector con coordenadas x e y que definen la direccion del movimiento.

        
#Tenemos que definir el metodo vision


class Presa(Animales):
    """
    Attributes:
         La __clase Presa__ posee 3 atributos:
         (1 y 2)_Vision y Velocidad_: heredados de Animales, que se re-inicializan en la clase presa.
         (3)_ID_: Un identificador del objeto presa.

        """
    def __init__(self,ID):
        "Define el valor de los atributos de la presa"
        Animales.__init__(self)
        self.velocidad *= 1#Defino la velocidad de la presa
        self.vision *= 1#Defino el rango de vision de la presa
        self.ID = ID#Defino el ID de la presa


"""
La __clase Depredador__ posee 4 atributos:
				(1 y 2)_Vision y Velocidad_ heredados de Animales, que se re-inicializan en la clase presa.
				(3)_ID_: Un identificador del objeto depredador.
				(4)_rad_comer_: Radio en el cual un depreador come a la presa.
La __clase Depredador__ posee 1 metodo:
				(1) _Comer()_:Elimina de la lista de presas la presa que fue comida por el depredador		
"""
class Depredador(Animales):
    """
    Attributes:
         La __clase Depredador__ posee 3 atributos:
         (1 y 2)_Vision y Velocidad_: heredados de Animales, que se re-inicializan en la clase presa.
         (3)_ID_: Un identificador del objeto presa.
        """
    def __init__(self,ID):
        """
        Define el valor de los atributos del predador.
        """
        Animales.__init__(self)
        self.velocidad *= 10
        self.vision *= 6 
        self.rad_comer = self.vision/3. 
        self.ID = ID
        
    def comer(self,ID_pre_com,lista): 
        "Le pasa el ID de la presa a comer en ID_pre_com, junto con la lista"
        del lista[ID_pre_com]         # Elimina el elemento list_pre_com de la lista.
        return lista

    def descansar(self,ID_dep, tamano):               # Luego de comer el depredador va a descansar a su cueva
        pos_cueva_dep = [0,0,0]
        pos_cueva_dep[0] = ID_dep
        pos_cueva_dep[1] = rand.random()*(tamano[0]/6)    # se define una posición random dentro de la cueva
        pos_cueva_dep[2] = rand.random()*(tamano[1]/6)
        return pos_cueva_dep    


#self.number_dep = territorio.num_dep
#radio_vis = 4.
#for p in lista_dep:
#    aux = p.ver(terr,radio_vis) #Llama al elemento cero de la lista p (que es un elementeo de lista_dep)
    
#preguntar a charly como guardan los objetos de lista_dep en el main

