# Cap 4 tema 2
# Accesarea fiserelor, citirea si scrierea
# PF - 27/05/2016

# --------------------------------------------------------------------------------------------------#
# Creati un program care sa citeasca toate liniile unui text (guta.txt) sub forma unei liste si     #
# afisati lista. Scrieti o linie intr-un fisier, cu un text la alegere                              #
# Cititi primul fisier intr-un singur sir de caractere apoi afisati-l.                              #
# --------------------------------------------------------------------------------------------------#

f=open('guta1.txt', 'r+')
# lines = f.readlines()
# print(lines)
#f.write('\n fc bn?')
text=f.read()
print(text)
f.close()
