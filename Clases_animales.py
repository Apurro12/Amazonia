# -*- coding: utf-8 -*-
import random as rand
import numpy as np

class Animales(object):
    def __init__(self,velocidad=1.,vision=1.):
        self.velocidad = velocidad
        self.vision = vision
#        self.hambre = hambre
#        self.vida = vida

    def moverse(self):
        self.dir_mov = [0,0]
        theta = rand.random() # Este es el ángulo respecto del eje x para la dirección de movimiento
        self.dir_mov[0] = np.cos(theta*2.*3.14)
        self.dir_mov[1] = np.sin(theta*2.*3.14) #Poner un pi como la gente
        return self.dir_mov

        
#Tenemos que definir el metodo vision

class Presa(Animales):
    def __init__(self,ID):
        Animales.__init__(self)
        self.velocidad *= 1
        self.vision *= 1
        self.ID = ID

class Depredador(Animales):
    def __init__(self,ID):
        Animales.__init__(self)
        self.velocidad *= 3
        self.vision *= 3
        self.rad_comer = self.vision/3. 
        self.ID = ID
        
    def comer(self,ID_pre_com,lista): # Le pasa el ID de la presa a comer en ID_pre_com, junto con la lista
        del lista(ID_pre_com)         # de presas (en lista). Elimina el elemento list_pre_com de 
        return lista

        


#self.number_dep = territorio.num_dep
#radio_vis = 4.
#for p in lista_dep:
#    aux = p.ver(terr,radio_vis) #Llama al elemento cero de la lista p (que es un elementeo de lista_dep)
    
#preguntar a charly como guardan los objetos de lista_dep en el main

