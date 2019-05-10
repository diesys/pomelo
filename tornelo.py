#!/usr/bin/env python3

import math, sys, json, os.path

# cartella dei tornei
tornei_dir = os.path.dirname('data/')

def scriviTorneo(torneo):
	# scrivi su file
	with open(torneo['FILE'], 'w') as file_json:
		json.dump(torneo, file_json)

def importaTorneo(torneo):
	# leggi da file
	with open(tornei_dir + '/' + torneo + '/' + torneo + '.json', 'r') as json_torneo:
		dict_torneo = json.load(json_torneo)
		# print(dict_torneo)
	
	return dict_torneo

# crea un nuovo torneo con 'torneo' come nome di default
def nuovoTorneo(nome="torneo"):

	# percorso del file e cartella che conterra' il dizionario
	file_path = tornei_dir + '/' + nome + '/' + nome + '.json'
	dir_path = os.path.dirname(file_path)
	# dir_path = os.path.dirname(tornei_dir + '/' + nome + '/' + file_name)
	
	# dizionario torneo base vuoto
	torneo = { 'NOME' : nome, 'FILE' : file_path, 'GIOCATORI' : {}, 'MATCHES' : {}  }
	
	# controlla se esiste la cartella col nome del torneo
	if not os.path.exists(dir_path):
		os.makedirs(dir_path)

		# controlla se esiste il file json del torneo se no lo crea e ci mette il contenuto dell'attuale dizionario
		if not os.path.exists(file_path):
			with open(file_path, 'w') as fp:
				json.dump(torneo, fp)

	else:
		print('Nome presente, cambiare nome per favore.\n')
		return
	
	return torneo

def aggiungiGiocatore(torneo, nome):
    # Aggiunge al torneo un nuovo Giocatore 'nome'. Controlla per prima cosa che
    # non esiste un altro giocatore con lo stesso nome. In caso positivo viene
    # aggiunto il Giocatore. Gli viene assegnato un punteggio iniziale di 1440 e
    # gli viene associato un numero d' iscrizione.
    
	#controlla che non ci sia un giocatore con lo stesso NOME
	for id in range(len(torneo['GIOCATORI'])):
		if torneo['GIOCATORI'][str(id)]['NOME'] == nome:
			print('Nome gia in uso: scegliere un altro NOME')
			return torneo
	
	# crea un dizionario ausiliario che verra' copiato nel torneo, l'ID e' anche chiave (univoca)
	nuovoID = torneo['NOME'] + '_' + str(len(torneo['GIOCATORI']))
	nuovoGiocatore = {'NOME' : nome, 'ID' : nuovoID, 'PUNTI' : 1440, 'MATCH' : 0}

	# aggiunge il nuovo giocatore al torneo
	torneo['GIOCATORI'][str(len(torneo['GIOCATORI']))] = nuovoGiocatore

	# scrivi su file
	scriviTorneo(torneo)

	return torneo

def eliminaGiocatore(torneo, nome):
    # Elimina dal torneo il Giocatore 'NOMEX'. Nella torneo e nella classifica del
    # torneo al posto dei dati di tale giocatore sara' presente una riga del tipo
    # ['ND',...] 
	
	for id in range(len(torneo['GIOCATORI'])):
		if torneo['GIOCATORI'][str(id)]['NOME'] == nome:
			# imposta valori oltre i limiti al posto di cancellare, preserva l'ID
			torneo['GIOCATORI'][str(id)]['NOME'] = 'ND'
			torneo['GIOCATORI'][str(id)]['PUNTI'] = -9999
			torneo['GIOCATORI'][str(id)]['MATCH'] = -1
	
	# scrivi su file
	scriviTorneo(torneo)

def nuoviPunteggiXY(torneo, giocatoreX, giocatoreY, risultatoX):
    # Calcola i nuovi di due giocatori dopo una partita. Il risultato 
    # è 1 se vince il primo giocatore, 0 se perde e 0.5 se pareggiano.
	
	for id in range(len(torneo['GIOCATORI'])):
		if torneo['GIOCATORI'][str(id)]['NOME'] == giocatoreX:
			punteggioX = int(torneo['GIOCATORI'][str(id)]['PUNTI'])
			matchX = int(torneo['GIOCATORI'][str(id)]['MATCH'])
	
	for id in range(len(torneo['GIOCATORI'])):
		if torneo['GIOCATORI'][str(id)]['NOME'] == giocatoreY:
			punteggioY = int(torneo['GIOCATORI'][str(id)]['PUNTI'])
			matchY = int(torneo['GIOCATORI'][str(id)]['MATCH'])

	#calcola risultato per il giocatoreY
	risultatoY = 1 - risultatoX

	#calcola risultato atteso per il giocatoreX e il giocatoreY
	attesoX = 1/2 + (math.atan((punteggioX - punteggioY)/200)) / math.pi
	attesoY = 1 - attesoX
	
	#calcolo coefficienti moltiplicativi per il giocatoreX e il giocatoreY 
	if (matchX > 8 and punteggioX > 1600):
		coefficienteX = 10
	elif (matchX < 6):
		coefficienteX = 40
	else:
		coefficienteX = 20
	if (matchY > 8 and punteggioY > 1600):
		coefficienteY = 10
	elif (matchY < 6):
		coefficienteY = 40
	else:
		coefficienteY = 20

	#calcolo punteggi parziali del giocatoreX e giocatoreY
	parzialeX = round((risultatoX - attesoX) * coefficienteX)
	parzialeY = round((risultatoY - attesoY) * coefficienteY)

	#calcolo punteggi totali del giocatoreX e giocatoreY
	punteggioX = punteggioX + parzialeX
	punteggioY = punteggioY + parzialeY
	
	return [punteggioX, punteggioY]

def aggiornaTorneo(torneo, giocatoreX, giocatoreY, risultatoX):
    # Calcola i punti ottenuti dopo che il giocatoreX ha sfidato il giocatoreY,
    # ottenendo un risultatoX = 0 (sconfitta) oppure 0.5 (pareggio) oppure 1
    # (vittoria). (giocatoreX e giocatoreY sono i numeri d' iscrizione dei
    # due giocatori che partecipano al torneo). Aggiorna quindi la torneo con i
    # nuovi punteggi dei giocatori giocatoreX e giocatoreY.

	if (risultatoX != 1 and risultatoX != 0.5 and risultatoX != 0):
		print('Risultato della partita errato')
		return  

	if (giocatoreX == giocatoreY):
		print('Un giocatore non puo giocare contro se stesso')
		return
	
	trovatoX = False
	for id in range(len(torneo['GIOCATORI'])):
		if torneo['GIOCATORI'][str(id)]['NOME'] == giocatoreX:
			trovatoX = True
	if not trovatoX:
		print('GiocatoreX non presente al torneo')
		return

	trovatoY = False
	for id in range(len(torneo['GIOCATORI'])):
		if torneo['GIOCATORI'][str(id)]['NOME'] == giocatoreY:
			trovatoY = True
	if not trovatoY:
		print('GiocatoreY non presente al torneo')
		return
	
	else:
		#calcola nuovi punteggi del giocatoreX e giocatoreY
		[nuovoPunteggioX, nuovoPunteggioY] = nuoviPunteggiXY(torneo, giocatoreX, giocatoreY, risultatoX)

		#aggiornamento dati giocatoreX nel torneo
		for id in range(len(torneo['GIOCATORI'])):
			if torneo['GIOCATORI'][str(id)]['NOME'] == giocatoreX:
				torneo['GIOCATORI'][str(id)]['PUNTI'] = nuovoPunteggioX
				torneo['GIOCATORI'][str(id)]['MATCH'] = torneo['GIOCATORI'][str(id)]['MATCH'] + 1

		#aggiornamento dati giocatoreY nel torneo
		for id in range(len(torneo['GIOCATORI'])):
			if torneo['GIOCATORI'][str(id)]['NOME'] == giocatoreY:
				torneo['GIOCATORI'][str(id)]['PUNTI'] = nuovoPunteggioY
				torneo['GIOCATORI'][str(id)]['MATCH'] = torneo['GIOCATORI'][str(id)]['MATCH'] + 1
		return 

	# scrivi su file
	scriviTorneo(torneo)


####### sezione di output

def stampaFormattato(torneo):
	caratteri_omessi = '"{}'
	torneo_formatted = json.dumps(torneo, indent=3, separators=('', ':\t'))

	for char in caratteri_omessi:
		torneo_formatted = torneo_formatted.replace(char, '')

	print(torneo_formatted)




######################################################################################################################################################
#COMANDO:                                      A COSA SERVE:

# il dizionario TORNEI contiene tutti i tornei (dizionari a loro volta) con il nome come chiave del torneo, all'int

#
#                                              progressivo che lo rappresenta. Il Giocatore appena iscritto avra' fatto 0 MATCH.
#
#
#
#classifica(torneo)                           Ordina i giocatori nella torneo in ordine decrescente dei loro punteggi.
#                                              A parita' di punteggio il giocatore con piu' MATCH sara' ad una posizione piu' alta
#                                              di MATCH disputate.
#                                              Stampa, quindi, la classifica aggiornata.
######################################################################################################################################################

HELP = 'Benvenuto in torneo-web (interfaccia CLI), le opzioni sono le seguenti:\n\n  -n NOME_TORNEO\t\tper creare un torneo con il nome indicato\n  --help\t\t\tmostra questo messaggio\n  --test\t\t\tusa dei tornei di test\n'


## sezione opzioni script
if(len(sys.argv) > 1):                                              ## getting parameters if exist
	options = sys.argv
	
	if(options[1] == '-n' or options[1] == '-new'):
		if(len(options)>2):
			nuovoTorneo = nuovoTorneo(options[2])
			print("Torneo creato, segui l'help per popolarlo\n")
		else:
			print('Manca il nome del torneo!\n')
	
	if(options[1] == '--test'):
		## test
		torneo_test = 'ping'

		# torneo = nuovoTorneo(torneo_test)
		torneo = importaTorneo(torneo_test)
		tornei = {torneo['NOME'] : torneo}
		# torneo = aggiungiGiocatore(tornei[torneo_test], 'Aacca')
		# torneo = aggiungiGiocatore(tornei[torneo_test], 'michele')
		# aggiornaTorneo(tornei[torneo_test], 'michele', 'Aacca', 1)
		aggiornaTorneo(tornei[torneo_test], 'michele', 'Aacca', 0)

		stampaFormattato(tornei[torneo_test])
		# stampa su std output
		# json.dump(tornei['pingpong'], sys.stdout)

	if(options[1] == '-h' or options[1] == '--help'):	
		print(HELP)
else:                                  
	print(HELP)	
