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
	

fname = open('H:/M2 recherche/Stage/lyesdata.pkl','rb')
data = pickle.load(fname)
a = 0 
b = 0
#====================================================================
#=======    génération des docs liés    ======================
#====================================================================
for doc1, doc2, linktype in data:
#	print(doc1)
	try:
		d1=open('H:/M2 recherche/Stage/datalink/doc 1/'+str(a)+'.txt','w')
		d1.write(str(doc1.__dict__))
		d1.close()
		
		d2=open('H:/M2 recherche/Stage/datalink/doc 2/'+str(b)+'.txt','w')
		d2.write(str(doc2.__dict__))
		d2.close()
		a += 1
		b += 1		 
		
	except ValueError:
		print("Oops!  pb...")
	
	


