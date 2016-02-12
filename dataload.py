#========================================================================
#========= pour lire les données qui sont dans le fichier .pkl ==========
#========================================================================
import os
import pickle

class Document(object):
	pass
	
a = 0
b = 0 
fname = open('H:/M2 recherche/Stage/somedocs.pkl','rb')
data = pickle.load(fname)
#=============== lire les données ===============================
for doc in data:
	#====== lire et enregistrer toutes les documents ===========
	try:
		output=open('H:/M2 recherche/Stage/MyDataSet/allData/'+str(a)+'.txt','w')
		output.write(str(doc.__dict__))
		a += 1
	except ValueError:
		print("Oops!  some thing goes wrrong in doc loading...N°"+str(a)+" ")	
	#====== lire et enregistrer les tweets ===========
	if ("tweet" in dir(doc)): 
		try:
			twt=open('H:/M2 recherche/Stage/MyDataSet/tweets/'+str(b)+'.txt','w')
			twt.write(str(doc.__dict__))
			b += 1
		except ValueError:
			print("Oops!  some thing goes wrrong in tweets loading...N°"+str(b)+" ")	
	#====== lire et enregistrer les transcriptions ===========
	else:
		if ("videofilepath" in dir(doc)): 
			try:
				trans=open('H:/M2 recherche/Stage/MyDataSet/transcriptions/'+str(b)+'.txt','w')
				trans.write(str(doc.__dict__))
				b += 1
			except ValueError:
				print("Oops!  some thing goes wrrong in transcriptions loading...N°"+str(b)+" ")
		else:
		#=============== lire et enregistrer les journaux  ===============
			try:
				jrn=open('H:/M2 recherche/Stage/MyDataSet/journaux/'+str(b)+'.txt','w')
				jrn.write(str(doc.__dict__))
				b += 1
			except ValueError:
				print("Oops!  some thing goes wrrong in journaux loading...N°"+str(b)+" ")

