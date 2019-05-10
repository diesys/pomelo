#!/usr/bin/env python3

import math, sys, json

def nuovoTorneo(nome="torneo"):
    """
    Crea un nuovo dizionario torneo vuoto. Si usa per creare un nuovo torneo.
    """

	torneo = {'NOME' : nome, 'GIOCATORI' : {} }
	
	return torneo

	# DA GESTIRE PER IL FUTURO POSSIBILI NOMI GIA' DEIFINITI O UGUALI
	# try:
	# 	tornei['NOME']
	
	# except NameError:
	# 	print("Torneo con questo nome presente, prova un alro nome\n")
	
	# else:
	

def aggiungiGiocatore(torneo, nome):
    """
    Aggiunge al torneo un nuovo Giocatore 'nome'. Controlla per prima cosa che
    non esiste un altro giocatore con lo stesso nome. In caso positivo viene
    aggiunto il Giocatore. Gli viene assegnato un punteggio iniziale di 1440 e
    gli viene associato un numero d' iscrizione.
    """
	#controlla che non ci sia un giocatore con lo stesso NOME
	for id in range(len(torneo['GIOCATORI'])):
		if torneo['GIOCATORI'][id]['NOME'] == nome:
			print('Nome gia in uso: scegliere un altro NOME')
			return torneo
	
	# crea un dizionario ausiliario che verra' copiato nel torneo, l'ID e' anche chiave (univoca)
	nuovoID = torneo['NOME'] + '_' + str(len(torneo['GIOCATORI']))
	nuovoGiocatore = {'NOME' : nome, 'ID' : nuovoID, 'PUNTI' : 1440, 'MATCH' : 0}

	# aggiunge il nuovo giocatore al torneo
	torneo['GIOCATORI'][len(torneo['GIOCATORI'])] = nuovoGiocatore

	return torneo

def eliminaGiocatore(torneo, nome):
    """
    Elimina dal torneo il Giocatore 'NOMEX'. Nella torneo e nella classifica del
    torneo al posto dei dati di tale giocatore sara' presente una riga del tipo
    ['ND',...] 
    """
	for id in range(len(torneo['GIOCATORI'])):
		if torneo['GIOCATORI'][id]['NOME'] == nome:
			# imposta valori oltre i limiti al posto di cancellare, preserva l'ID
			torneo['GIOCATORI'][id]['NOME'] = 'ND'
			torneo['GIOCATORI'][id]['PUNTI'] = -9999
			torneo['GIOCATORI'][id]['MATCH'] = -1

def nuoviPunteggiXY(torneo, giocatoreX, giocatoreY, risultatoX):
    """
    Calcola i nuovi di due giocatori dopo una partita. Il risultato 
    è 1 se vince il primo giocatore, 0 se perde e 0.5 se pareggiano.
    """
	for id in range(len(torneo['GIOCATORI'])):
		if torneo['GIOCATORI'][id]['NOME'] == giocatoreX:
			punteggioX = torneo['GIOCATORI'][id]['PUNTI']
			MATCHX = torneo['GIOCATORI'][id]['MATCH']
	for id in range(len(torneo['GIOCATORI'])):
		if torneo['GIOCATORI'][id]['NOME'] == giocatoreY:
			punteggioY = torneo['GIOCATORI'][id]['PUNTI']
			MATCHY = torneo['GIOCATORI'][id]['MATCH']

	#calcola risultato per il giocatoreY
	risultatoY = 1 - risultatoX

	#calcola risultato atteso per il giocatoreX e il giocatoreY
	attesoX = 1/2 + (math.atan((punteggioX - punteggioY)/200)) / math.pi
	attesoY = 1 - attesoX
	
	#calcolo coefficienti moltiplicativi per il giocatoreX e il giocatoreY 
	if (MATCHX > 8 and punteggioX > 1600):
		coefficienteX = 10
	elif (MATCHX < 6):
		coefficienteX = 40
	else:
		coefficienteX = 20
	if (MATCHY > 8 and punteggioY > 1600):
		coefficienteY = 10
	elif (MATCHY < 6):
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
    """
    Calcola i punti ottenuti dopo che il giocatoreX ha sfidato il giocatoreY,
    ottenendo un risultatoX = 0 (sconfitta) oppure 0.5 (pareggio) oppure 1
    (vittoria). (giocatoreX e giocatoreY sono i numeri d' iscrizione dei
    due giocatori che partecipano al torneo). Aggiorna quindi la torneo con i
    nuovi punteggi dei giocatori giocatoreX e giocatoreY.
    """
	if (risultatoX != 1 and risultatoX != 0.5 and risultatoX != 0):
		print('Risultato della partita errato')
		return  

	if (giocatoreX == giocatoreY):
		print('Un giocatore non puo giocare contro se stesso')
		return
	
	trovatoX = False
	for id in range(len(torneo['GIOCATORI'])):
		if torneo['GIOCATORI'][id]['NOME'] == giocatoreX:
			trovatoX = True
	if not trovatoX:
		print('GiocatoreX non presente al torneo')
		return

	trovatoY = False
	for id in range(len(torneo['GIOCATORI'])):
		if torneo['GIOCATORI'][id]['NOME'] == giocatoreY:
			trovatoY = True
	if not trovatoY:
		print('GiocatoreY non presente al torneo')
		return
	
	else:
		#calcola nuovi punteggi del giocatoreX e giocatoreY
		[nuovoPunteggioX, nuovoPunteggioY] = nuoviPunteggiXY(torneo, giocatoreX, giocatoreY, risultatoX)

		#aggiornamento dati giocatoreX nel torneo
		for id in range(len(torneo['GIOCATORI'])):
			if torneo['GIOCATORI'][id]['NOME'] == giocatoreX:
				torneo['GIOCATORI'][id]['PUNTI'] = nuovoPunteggioX
				torneo['GIOCATORI'][id]['MATCH'] = torneo['GIOCATORI'][id]['MATCH'] + 1

		#aggiornamento dati giocatoreY nel torneo
		for id in range(len(torneo['GIOCATORI'])):
			if torneo['GIOCATORI'][id]['NOME'] == giocatoreY:
				torneo['GIOCATORI'][id]['PUNTI'] = nuovoPunteggioY
				torneo['GIOCATORI'][id]['MATCH'] = torneo['GIOCATORI'][id]['MATCH'] + 1
		return 


####### sezione di output

def stampaFormattato(torneo):
	caratteri_omessi = '"{}'
	torneo_formatted = json.dumps(torneo, indent=3, separators=('', ':\t'))

	for char in caratteri_omessi:
		torneo_formatted = torneo_formatted.replace(char, '')

	print(torneo_formatted)


# def classifica(torneo):
# 	if (len(torneo) > 4):
# 		i = 2
# 		j = 2
# 		while i < len(torneo):
# 			massimo = torneo[i]
# 			MATCHMassimo = torneo[i+1] 
# 			giocatoreMassimo = torneo[i-2 : i+2]
# 			indiceMassimo = i
# 			j = i+4
# 			while j < len(torneo):
# 				if torneo[j] > massimo:
# 					massimo = torneo[j]
# 					MATCHMassimo = torneo[j+1]
# 					giocatoreMassimo = torneo[j-2 : j+2]
# 					indiceMassimo = j
# 				#A parita' di punteggio il giocatore con piu' MATCH sara' ad una posizione piu' alta
# 				elif torneo[j] == massimo and torneo[j+1] > MATCHMassimo:
# 					massimo = torneo[j]
# 					MATCHMassimo = torneo[j+1]
# 					giocatoreMassimo = torneo[j-2 : j+2]
# 					indiceMassimo = j
# 				j = j+4
# 			torneo[indiceMassimo-2 : indiceMassimo+2] = torneo[i-2 : i+2]
# 			torneo[i-2 : i+2] = giocatoreMassimo
# 			i = i+4
	
# 	print('------------------CLASSIFICA------------------\n')
	
# 	i = 0
	
# 	while (i < len(torneo)):
# 		if (torneo[i+3] < 6):
# 			print(torneo[i], 'nc', torneo[i+3])
# 		else:
# 			print(torneo[i], torneo[i+2 : i+4])
# 		print('\n')
# 		i = i+4
	
# 	print('##############################################')
# 	return


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
		torneo = nuovoTorneo('pingpong')
		tornei = {torneo['NOME'] : torneo}
		torneo = aggiungiGiocatore(tornei['pingpong'], 'michele')
		torneo = aggiungiGiocatore(tornei['pingpong'], 'Aacca')
		aggiornaTorneo(tornei['pingpong'], 'michele', 'Aacca', 1)

		stampaFormattato(tornei)
		json.dump(tornei['pingpong'], sys.stdout)



	if(options[1] == '-h' or options[1] == '--help'):	
		print(HELP)
else:                                  
	print(HELP)	


### DUMP DI UN DIZIONARIO IN UN JSON
## SCRIVE SU FILE
# with open('result.json', 'w') as fp:
	# json.dump(tornei['pingpong'], fp)

## STAMPA SU STD OUTPUT
# json.dump('SomeText', sys.stdout)
