
'''
Az ELDÖNTÉS esetében azt vizsgáljuk,
hogy szerepel-e egy bizonyos tulajdonságú elem az adatsorban (itt a listában).
    
A program azt vizsgálja, hogy van-e hárommal osztható szám a listában.


lista = [2, 5, 4, 8, 9, 11, 10, 12]

talalat = False
index = 0
while index < len(lista) and not talalat:
    if lista[index] % 3 == 0:
        talalat = True
    index = index + 1

if talalat:
    print('Van a listában hárommal osztható szám.')
else:
    print('Nincs a listában hárommal osztható szám.')
'''

'''
    A KIVÁLASZTÁS esetében azt tudjuk, hogy szerepel (legalább) egy bizonyos tulajdonságú elem 
    az adatsorban (itt a listában), és ennek az elemnek az indexére vagyunk kíváncsiak.

    A program azt vizsgálja, hogy hányadik indexű helyen áll a hárommal osztható szám a listában. 
    Az első ilyen elem előfordulása érdekel bennünket.  
'''
"""
lista = [2, 5, 4, 8, 9, 11, 10, 12]

talalat = False
index = 0
while not talalat:
        if lista[index] % 3 == 0:
            talalat = True
        index = index + 1

print('A hárommal osztható szám indexe a listában: ', index-1)
"""

lista1 = [2, 5, 4, 8, 9, 11, 10, 12]

def eldontes(lista):
    talalat = False
index = 0
while index < len(eldontes) and not talalat:
    if eldontes [index] % 3 == 0:
        talalat = True
        index = index + 1
        
        if talalat:
            print("Van a listában hárommal osztható szám.")
        else:
            print("Nincs a listában hárommal osztható szám")
            

kereses_tetele(lista2)
eldontes_tetele(lista1)