import glob
import os, sys
import pickle
#===============================================================================
#======== pour ouvrir et lire un fichier .txt  =================================
#===============================================================================
 
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
		if (char == "'" or char == '"'):
			char = " "
		else:
			char = char
		#print(char)
		if not char: break
		data+=char
	#content = strm.read()
	oneLine = data.replace('\n', '')
	return oneLine
#=======================================================================
# ======= le chargement des données (la lecture de .pkl)
#======================================================================
class Document(object):
	pass
	
n = 0 
fname = open('H:/M2 recherche/Stage/lyesdata.pkl','rb')
data = pickle.load(fname)


#====================================================================
#=======    génération automatique de .arrf    ======================
#====================================================================
"""
at_class="{"
for doc1, doc2, linktype in data:
	try:
		at_class+=str(linktype)+","
	except ValueError:
		print("Oops!  some thing qoes wrrong when building links")	
at_class+="}"
"""	
arff_header = """
@relation tweets

@ATTRIBUTE text1 STRING
@ATTRIBUTE text2 STRING
@ATTRIBUTE class {dev,pos,ant,qd}

@DATA
"""
text=""
for doc1, doc2, linktype in data:
#	print(doc1)
	try:
		d1=open('H:/M2 recherche/Stage/d1.txt','w')
		d1.write(doc1.text)
		d1.close()
		
		d2=open('H:/M2 recherche/Stage/d2.txt','w')
		d2.write(doc2.text)
		d2.close()
		
		lec_fichier = ouvrir_fichier("H:/M2 recherche/Stage/d1.txt", "r")
		text += "\'"+str(lire_fichier(lec_fichier))+"\'"+","
				
		lec_fichier2 = ouvrir_fichier("H:/M2 recherche/Stage/d2.txt", "r")
		text += "\'"+str(lire_fichier(lec_fichier2))+"\'"+","
		
		text+=linktype+"\n"
		
		output=open('H:/M2 recherche/Stage/datasets/train4.arff','w')
	except ValueError:
		print("Oops!  pb...")
	try:
		output.write(str(arff_header))
		output.write(str(text))
	except ValueError:
		print("Oops!  some thing goes wrrong...")
	


