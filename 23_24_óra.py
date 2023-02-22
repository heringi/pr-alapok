"""
szoveg = "hello világa!"
for karakter in szoveg:
    print(karakter,end="")
"""

"""
for szam in range(50,101,3):
    print(szam, end = " ")
"""
"""
for szam in range(50,100,3):
    if szam % 2 == 0:
        print(szam,end=" ")
"""

nev = input("Kérem a nevedet: ")
for karakter in nev:
    nev_kicsi = nem_kicsi + karakter.épwer()
print(nev_kicsi)
#  print(karakter.lower(),end="")    