# 102 Numere
# Numere
# PF - 06/10/2017 v3


# Integer (int), float, numere complexe:

print ( 4 + 3 )         # adunare

print ( 5 - 2 )         # scadere

print ( 5 * 2 )         # inmultire

print ( 8 / 2 )         # impartire (exacta - rezultat float)

print ( 8 / 3 )         # impartire (exacta - rezultat float)

print ( 8.0 // 3 )      # impartire (doar catul)

print ( 8 % 3 )         # modulo (doar restul)

print ( ((7 + 3) * 2) / 4 )    # operatii cu mai multi operatori ( doar paranteze rotunde)
                               # operatorul * se mentioneaza chiar daca sunt paranteze
print ( (2 + 2j) * (2 + 1j) )       # operatii cu numere complexe

print ( 5 ** 7 )                    # ridicarea la putere

# lucrul cu numere complexe
(2 + 1j).real
(2 + 1j).imag
(2 + 1j).conjugate( )

# Conversii de numere

print(int ( '1fa0', 16 ))   # transforma un string in numar din baza dorita in baza 10
                            # cat reprezinta "1fa0" din baza 16 in baza 10?

print(int( '75'))           # transforma un string, care contine doar cifre, in numar int
                            # daca daza este 10 nu trebuie mentionata
print(int ( '2.5' ))               # eroare, nu putem transforma direct in string daca are si zecimale

print( int ( float ( '2.5' ) ) )
                            # float face transformarea in numar, int elimina zecimalele

input ( "Apasa <enter> pt a iesi." )


