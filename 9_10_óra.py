# Első feladat 9dk tankönyv

IDEI_ÉV = 2022
print(type(IDEI_ÉV))
print( 'Az idei év :',IDEI_ÉV, sep='--->')
felhasználó_kora = input('hány éves vagy?')
print(type(felhasználó_kora))
print('Te most', felhasználó_kora,'éves vagy.')
felhasználó_kora = int(felhasználó_kora)
print(type (felhasznalo_kora))
születési_év = IDEI_ÉV - felhasználó_kora
print('Ekkor születtél:', születési_év,'.', sep='')

print(type(felhasználó_kora))
felhasználó_kora = str(felhasználó_kora)
print(type(felhasználó_kora))
print('És milyen ' + felhasználó_kora + 'évesnek lenni? ')
print('És milyen ' , felhasználó_kora , 'évesnek lenni? ')

#második program
gondolt_szám = 4
tipp = input('Gondoltam egy számra. Tippeld meg! ')
tipp = int(tipp)
if tipp == gondolt_szám:
    print('Ügyes!')
    print('Gratulálok.')
else:
    print('Hosszan gondolkodtál rajta?')
    print('Nem érte meg.')
print('Pápá.'))