# 310 Dictionare
# Lucrul cu liste si dictionare
# PF - 27/05/2016

lista_filme = list ( )  # lista contine dictionare cu filme. Un film, un dictionar
film= dict ( )

# 	populam dictionarul pentru film1
film['Director'] = 'Alejandro G. Inarritu'
film['Title'] = 'The Revenant'
film['Release year'] = '2015'
film['Running Time'] = '156 minutes'
film['Rating'] = 'AG-15'
print(film)

# populam lista cu datele din dictionar
lista_filme.append ( film )

film = {}

# populam dictionarul pentru film2
film['Director'] = 'Radu Jude'
film['Title'] = 'Aferim!'
film['Release Year'] = '2015'
film['Running Time'] = '108 min'
film['Rating'] = 'AG-12'

# populam lista cu datele din dictionar
lista_filme.append ( film )
print ( lista_filme )

# selectie elem convenabile din lista prin keys
keys = ['Title', 'Director']

for item in lista_filme:
	print ( "*" * 30 )
	for key in keys:
		print ( key, ': ', item[key] )
print ( 30 * "*" )
