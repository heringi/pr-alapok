"""
szam1 = int(input("kérek egy egész számot:"))
szam2 = int(input("kérek egy másik egész számot:"))
if szam1 > szam2:
    print("szam1 nagyobb mint szam2")
if szam2 > szam1:
    print("szam2 nagyobb mint szam1") 
if szam1 == szam2:
    print("szam1 megegyezik szam2-vel") 
"""      
"""
szam1 = int(input("kérek egy egész számot:"))
szam2 = int(input("kérek egy másik egész számot:"))
if szam1 > szam2:
    print("szam1 nagyobb mint szam2")
elif szam2 > szam1:
    print("szam2 nagyobb mint szam1") 
elif szam1 == szam2:
    print("szam1 megegyezik szam2-vel") 
"""
"""
szam1 = int(input("kérek egy egész számot:"))
szam2 = int(input("kérek egy másik egész számot:"))
if szam1 > szam2:
    print("szam1 nagyobb mint szam2")
elif szam2 > szam1:
    print("szam2 nagyobb mint szam1") 
else szam1 == szam2:
    print("szam1 megegyezik szam2-vel") 
    """
"""
x = None 
print(x)
print(type(x))

if x:
    print("Do you think None is True?")
elif x is False:
    print ("Dou you think None is False?")
else:
    print("None is not True, or False, None just None...")
"""

"""
    # -----------------------------------------
    # Bekérek egy osztályzatot, írja ki 1-elégtelen..5-jeles..vagy nem érvényes osztályzat!
     jegy = input("Kérek egy osztályzatot:")
     if jegy == "1":
         print("elégtelen")
     elif jegy == "2":
         print("elégséges")
     elif jegy == "3":
         print("közepes")    
     elif jegy == "4":
         print("jó")  
     elif jegy == "5":
         print("jeles")   
     else:
         print("Érvénytelen osztályzatot adtál")   
         """

"""
         #Bekérek egy pozitív egész számot, és írassuk ki hogy páros vagy páratlan

          szam = int(input("Kérek egy pozitiv egész számot"))
          if szam % 2 == 0:
              print("a szám páros")
          else:
              print("szám páratlan")    
""" 
"""
      
        #Véletlen szám előállítás

        import random

        gondolt_szam = random.randint(1,6)
        print('Súgók:', gondolt_szam)
        tipp = int(input('Gondoltam egy számra. Tippeld meg! '))
        if gondolt_szam = tipp
            print("jól tippeltél")
        else:
            print("nem jól tippeltél")    
"""

            #----------------
            #Generáljunk egy számot 1-1000 között, irassuk ki a számot 

import random

szam = random.randint(1,1000)
print(szam)
if szam%2 == 0 and szam <500:
    print("jó")
else: 
    print("nem jó")
                    