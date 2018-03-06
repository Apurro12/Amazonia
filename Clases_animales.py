
# coding: utf-8

# In[1]:

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

    def ver(self,):
#        self.self_pos = self.pos_d[1,2]
        pass
        
#Tenemos que definir el metodo vision

class Presa(Animales):
    def __init__(self):
        Animales.__init__(self)
        self.velocidad *= 2
        self.vision *= 4

class Depredador(Animales):
    def __init__(self):
        Animales.__init__(self)
        self.velocidad *= 4
        self.vision *= 4


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



