import sys
 
def ouvrir_fichier(fichier, mode):
    try: # gestion d'exception
        strm = open(fichier, mode)
    except(IOError):
        print ("Impossible d'ouvrir le fichier '", fichier, "'Veuillez réessayer")
        sys.exit()
    else:
        return strm
 
def lire_fichier(strm):
    #Lire une ligne
	#data = strm.readline()
	data=""
	while 1:
		char = strm.readline(1)          # Lire le fichier caractère
		if (char == "'"):
			char = " "
		else:
			char = char
		#print(char)
		if not char: break
		data+=char
	#content = strm.read()
	oneLine = data.replace('\n', '')
	return oneLine
#========================================================================
import glob
import os, sys
arff_header = """
@relation tweets

@ATTRIBUTE text1 STRING
@ATTRIBUTE text2 STRING
@ATTRIBUTE class {reaction,developpement,résumé,posteriorite,quasi_duplicat,citation,parodie}

@DATA
"""
#=========================================================================
text=""
ma_liste = [(0,2,'reaction'), (2,3,'developpement'), (3,4,'résumé'),(6,7,'citation'),(1,8,'quasi_duplicat'),(10,9,'reaction'),
(21,20,'quasi_duplicat'),(4,18,'parodie'),(10,19,'reaction'),(13,2,'reaction'),(11,12,'parodie'),
(13,27,'reaction'),(31,45,'posteriorite'),(13,26,'reaction'),(34,23,'reaction'),(20,40,'posteriorite'),
(1,2,'citation'),(5,33,'posteriorite'),(42,2,'reaction'),(13,2,'quasi_duplicat'),(22,52,'reaction')]
#>>> ma_liste.insert(2, 'c') # On insère 'c' à l'indice 2
for x in ma_liste:
	print (x[2])
	print('\n')
	lec_fichier = ouvrir_fichier("H:\M2 recherche\Stage\data2/"+str(x[0])+".txt", "r")
	text += "\'"+str(lire_fichier(lec_fichier))+"\'"+","
	lec_fichier = ouvrir_fichier("H:\M2 recherche\Stage\data2/"+str(x[1])+".txt", "r")
	text += "\'"+str(lire_fichier(lec_fichier))+"\'"+","
	text+=str(x[2])+"\n"
	output=open('H:/M2 recherche/Stage/datasets/train2.arff','w')
	try:
		output.write(str(arff_header))
		output.write(str(text))
	except ValueError:
		print("Oops!  some thing goes wrrong...")

		