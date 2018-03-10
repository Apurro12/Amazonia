


# -*- coding: utf-8 -*-


















"""Clase Animales

En este archivo se generan tres clases: __Clase Animales__, __Clase Depredador__ y __Clase Presa__.
Las ultimas dos clases heredan metodos y atributos de la clase animales. El objetivo es generar objetos con atributos y metodos que les permitan interactuar con el territorio. La clase Animales genera atributos y metodos que comparten tanto las presas como los predadores. Entre ellos la capacidad de moverse a una determinada velocidad y de tener un radio de vision para detectar a otros animales.
Las presas juegan un rol pasivo en este ecosistema, merodean por el territorio.
Los predadores merodean por el territorio, pero ademas tienen la capacidad de comer presas, de cazarlas y de descansar luego de comer una presa. 

Desarrolladores: 
    Antonella Marabotto, Camilo Amadio, Federico Hernandez, Carlos Raul Medrano
"""




import pydoc
import random as rand
import numpy as np


class Animales(object):
    """Generador del objeto animales.
    Objeto que define dos metodos y dos atributos comunes tanto a presas como predadores: Radio de
    vision, Velocidad, moverse() y __init__().
    Attributes:
        (1)Velocidad(float)	Define la amplificacion del vector de movimiento unitario. 
	(2)Vision(float) 	Define el rango con que el animal detecta a otros.
    """
    def __init__(self,velocidad=0.1,vision=1.):


        """Define los atributos de la clase animal, velocidad y vision; los dos son floats.
        Parametros:
            Velocidad(float): Definida por el usuario. Es un parametro que indica cuanto se 
            amplifica el vector generado en moverse().
            vision(float): Definida por el usuario. Es un parametro que indica el radio de
            deteccion de otros animales.
    """

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
    """Generador del objeto Presa.
    Esta clase produce presas, cuya principal caracteristica es la de moverse aleatoriamente en el
    espacio generado. Se mueven a una velocidad en todas las instancias del programa.
    Attributes:
         La __clase Presa__ posee 3 atributos:
         (1 y 2)Vision (float) y Velocidad(float): heredados de Animales, que se re-inicializan en la clase presa.
         (3)ID(int): Un identificador del objeto presa.

        """
    def __init__(self,ID):
        "Define el valor de los atributos de la presa"
        Animales.__init__(self)
        self.velocidad *= 5#Defino la velocidad de la presa
        self.vision *= 1#Defino el rango de vision de la presa
        self.ID = ID#Defino el ID de la presa



class Depredador(Animales):
    """
    Generador del objeto depredador
    Esta clase produce un objeto que hereda de la clase animales los atributos vision y velocidad.
    Tiene los metodos comer, que le permite atrapar una presa y removerla del sistema; el metodo
    descansar, una vez que come una presa el depredador queda confinado a una region donde no hay
    presas, y por ello no puede comer en esa partida. Hereda de la clase animal el metodo moverse 
    que le permite moverse aleatoriamente a menos que la distancia a una presa sea menor que su
    radio de vision, en cuyo caso persigue a la presa.

    Attributes:
         La __clase Depredador__ posee 4 atributos:
         (1 y 2)Vision y Velocidad: heredados de Animales, que se re-inicializan en la clase
         presa.
         (3)ID: Un identificador del objeto depredador. 
         (4)_rad_comer_: Radio en el cual un depreador come a la presa.
        """
    def __init__(self,ID):
        """



        Define el valor de los atributos del predador: Velocidad, vision, radio de comer
        (rad_com), y ID.
>>>>>>> parent of 049707f... Revert "Terminada la documentacion. Carga de los archivos html y la doc en los archvos .py"
        """
        Animales.__init__(self)
        self.velocidad *= 15
        self.vision *= 15 
        self.rad_comer = 2 #self.vision 
        self.ID = ID
        
    def comer(self,ID_pre_com,lista): 



        """Metodo que elimina a la presa que fue comida por el depredador. Devuelve una lista.
        Parametros:
             ID_pre_com(int): Es un indicador de la presa que fue comida
             lista[]: Es una lista con las presas

"""

        del lista[ID_pre_com]         # Elimina el elemento list_pre_com de la lista.
        return lista

    def descansar(self,ID_dep, tamano):               # Luego de comer el depredador va a descansar a su cueva
        """El metodo descansar hacer que si el depredador come una presa, luego sea confinado a
        una region del territorio donde no hay presas y por ello no puede alimentarse hasta la
        siguiente partida.
        Parametros:
             ID_dep(int): Es un indicador de cada depredador
             tamano []: Tamano del territorio
     """
        pos_cueva_dep = [0,0,0]
        pos_cueva_dep[0] = ID_dep
        pos_cueva_dep[1] = rand.random()*(tamano[0]/6)    # se define una posición random dentro de la cueva
        pos_cueva_dep[2] = rand.random()*(tamano[1]/6)
        return pos_cueva_dep    

    def cazar(self,ID_dep, componentes):
        desplazamiento = [0,0,0]
        desplazamiento[0] = ID_dep
        desplazamiento[1] = (componentes[0]/(np.sqrt(componentes[0]**2+componentes[1]**2)))
        desplazamiento[2] = (componentes[1]/(np.sqrt(componentes[0]**2+componentes[1]**2)))            

        return desplazamiento


#self.number_dep = territorio.num_dep
#radio_vis = 4.
#for p in lista_dep:
#    aux = p.ver(terr,radio_vis) #Llama al elemento cero de la lista p (que es un elementeo de lista_dep)
    
#preguntar a charly como guardan los objetos de lista_dep en el main

