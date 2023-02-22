
"""
keresztnev = input("add meg a nevedet:")
kor = int(input("add meg a korod:"))
if kor < 1:
    print("A kora alapján", nev, "csecsemo!"
elif kor < 6:
    print("A kora alapján", nev, "kisgyerek!"
elif kor < 12:
    print("A kora alapján", nev, "gyerek!"
elif kor < 16:
    print("A kora alapján", nev, "serdulo!")
elif kor < 25:
    print("A kora alapján", nev, "ifju!")
elif kor < 65:
    print("A kora alapján", nev, "felnott!")
else: print("A kora alapján", nev, "nyugdijas!")


elif kor >= 65:
    print(f"A koranalapjan {nev} nyugdijas!")
    """

lista = (7,8,6,2,15,1,13,5,9,11,12,3,4)
print(lista)
lista_hossza=len(lista)
print(f"A lista hossza: {lista_hossza-1, 0, -1}")
for i in range(lista_hossza-1, 0, -1):
    for j range(0, i):
        if t[j]