import cv2
import numpy as np


"""
Fazer comentarios
"""
# + uma forma de cometar

"""
Tambem é poissivel isto ser uma string mas tem de ser atrivuida a uma variavael
"""

# exemplos:
name= "Nowell strike"

home= "fevbrt, egre"

sites= '''wegethythtr
egergegergergergergergegerg'''

bio= """erwgergergergergregerg
egergergergergrgrgergergergergergerger"""


#Integer numbers
year=2010
year=int ("2010")  #tranfoemar uma string num inteiro

#float numbers
pi=3.14
pi=float("3.14")  #tranfoemar uma string num float

#fixed point numbers
from decimal import Decimal
price= Decimal("0.02")



#represnetar Null
optional_data = None

#Lists
#Lists can be heterogeneous
favourites= []     #empty list

#appending
favourites.append(42)       #Can store 42

#Extending
favourites.extended(["Python", True])  #Remove de list condition and add the valus

#Equivalent to
favourite= [42,"Python", True]



#Dictionary
#Set by Key /Get by key 
person['name']='Nowell Strite'

#Update 
person.update({
    'favourites': [42, 'food'],
    'gender': 'male',
})

#Any inmutable object can  be dictionary key
person[42]= 'favourite number'
person[(44.47,-73.21)]= 'coordinates'


