#!/usr/vin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Any

class Stack():
    """IMPORTANTE: Cuando una variable o función tiene '__' significa que es algo que va a ser privado, no se puede modificar """
    __slots__ = ['__values'] # Es un 'list' de python que voy a utilizar para guardar mi pila

    """ NOTA: 'self' hace referencia a mi mismo. El self es para conocer mi estado interno es como el this de java """

    def __init__(self, iterable = None): # Si no se crea un objeto iterable el parametro toma el valor None
        self._values = [] # Crea una lista vacia
        if iterable is not None:
            for value in iterable:
                self.push(value)

    def is_empty(self): # Retorna True si esta vacia
        return len(self._values) == 0

    @Property # Lo protege de que el usuario externo borre algo
    def top(self): #Tope de mi lista
        assert not self._is_empty(), 'No se puede operar con una pila vacia' # Es una regla, si no se cumple imprime el mensaje
        ## assert not: Es como un if siempre debe suceder lo que pide
        return self._values[-1]

    def clear(self):
        self._values.clear()

    def push(self,values):
        self._values.append(value)

    def pop(self): # Saca el último elemento de la pila
        assert not self._is_empty(), 'No se puede operar con una pila vacia'
        return self._values.pop() # Si tiene elementos implementa el pop
      
    def copy(self): # Crea una copia de un elemento 
        new_Stack = Stack() # Hace que dos celdas diferentes tengan el mismo elemento
        new_Stack._values = self._values.copy()
        return new_stack

    def __len__(self): # Retorna el tamaño de self._values
        return len(self._values)

    def __eq__(self, other): # Se invoca cuando hay un ==
        return self._values = = other__values

    def __repr__(self): # Imprime la pila implementada
        return 'Pila([' + ','.join(repr(x) for x in self._values) + '])'

                                                                                                                               
