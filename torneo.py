import math

def nuovoTorneo():
	return []

def aggiungiGiocatore(torneo, nome):
	i = 0
	#controlla che non ci cia un giocatore con lo stesso nome
	while i < len(torneo):
		if torneo[i] == nome:
			print('Nome gia in uso: scegliere un altro nome')
			return torneo
		i = i + 4
	numero = int((len(torneo) / 4)) + 1   # where len(torneo): 
	giocatore = [nome, numero, 1440, 0]
	torneo = torneo + giocatore
	return torneo

def eliminaGiocatore(torneo, nome):
	i = 0
	while i < len(torneo):
		if torneo[i] == nome:
			torneo[i : i+4] = ['ND', -1, -9999, -1]
			#forza l'uscita
			return
		else:
			i = i+4
	print('Giocatore non eliminabile partecipante al torneo')
	return

def aggiornaTorneo(torneo, giocatoreX, giocatoreY, risultatoX):
	if risultatoX != 1 and risultatoX != 0.5 and risultatoX != 0:
		print('Risultato della partita errato')
		return 
	if giocatoreX == giocatoreY:
		print('Un giocatore non puo giocare contro se stesso')
		return
	if giocatoreX > int((len(torneo) / 4)) or giocatoreX < 0 or giocatoreY > int((len(torneo) / 4)) or giocatoreY < 0:
		print('Almeno uno dei due giocatori non partecipa al torneo')
		return
	else:
		i = 1
		while i < len(torneo):
			if torneo[i] == giocatoreX:
				iX = i+1
				punteggioX = torneo[i+1]
				partiteX = torneo[i+2]

				#forza l'uscita
				i = i + len(torneo) + 2
			else:
				i = i+4
		
		#caso in cui il giocatore 'giocatoreX' e' stato eliminato dal torneo in precedenza
		if i == len(torneo) + 1:
			print('Almeno uno dei due giocatori eliminato dal torneo')
			return
		j = 1
		while j < len(torneo):
			if torneo[j] == giocatoreY:
				jY = j + 1
				punteggioY = torneo[j+1]
				partiteY = torneo[j+2]
				#forza l'uscita
				j = j + len(torneo) + 2
			else:
				j = j+4
		
		#caso in cui il giocatore 'giocatoreY' e' stato eliminato dal torneo in precedenza
		if j == len(torneo) + 1:
			print('Almeno uno dei due giocatori eliminato dal torneo')
			return
		
		#calcolo valore atteso per il giocatoreX e il giocatoreY
		EX = 1/2 + (math.atan((punteggioX - punteggioY)/200)) / math.pi
		EY = 1 - EX
		risultatoY = 1 - risultatoX

		#calcolo coefficienti moltiplicativi kX e kY 
		if partiteX > 8 and punteggioX > 1600:
			kX = 10
		elif partiteX < 6:
			kX = 40
		else:
			kX = 20
		if partiteY > 8 and punteggioY > 1600:
			kY = 10
		elif partiteY < 6:
			kY = 40
		else:
			kY = 20

		#calcolo punteggi parziali del giocatoreX e giocatoreY
		parzialeX = round((risultatoX - EX) * kX)
		parzialeY = round((risultatoY - EY) * kY)

		#calcolo punteggi totali del giocatoreX e giocatoreY
		punteggioX = punteggioX + parzialeX
		punteggioY = punteggioY + parzialeY

		#aggiornamento torneo
		torneo[iX] = punteggioX
		torneo[iX+1] = torneo[iX+1] + 1
		torneo[jY] = punteggioY
		torneo[jY+1] = torneo[jY+1] + 1
		
		return 

def classifica(torneo):
	if len(torneo) > 4:
		i = 2
		j = 2
		while i < len(torneo):
			massimo = torneo[i]
			partiteMassimo = torneo[i+1] 
			giocatoreMassimo = torneo[i-2 : i+2]
			indiceMassimo = i
			j = i+4
			while j < len(torneo):
				if torneo[j] > massimo:
					massimo = torneo[j]
					partiteMassimo = torneo[j+1]
					giocatoreMassimo = torneo[j-2 : j+2]
					indiceMassimo = j
				#A parita' di punteggio il giocatore con piu' partite sarà ad una posizione piu' alta
				elif torneo[j] == massimo and torneo[j+1] > partiteMassimo:
					massimo = torneo[j]
					partiteMassimo = torneo[j+1]
					giocatoreMassimo = torneo[j-2 : j+2]
					indiceMassimo = j
				j = j+4
			torneo[indiceMassimo-2 : indiceMassimo+2] = torneo[i-2 : i+2]
			torneo[i-2 : i+2] = giocatoreMassimo
			i = i+4
	
	print('------------------CLASSIFICA------------------\n')
	
	i = 0
	
	while i < len(torneo):
		if (torneo[i+3] < 6):
			print(torneo[i], 'nc', torneo[i+3])
		else:
			print(torneo[i], torneo[i+2 : i+4])
		print('\n')
		i = i+4
	
	print('##############################################')
	return

######################################################################################################################################################
#COMANDO:                                      A COSA SERVE:
#
#torneo = nuovoTorneo()                       Crea una nuova torneo vuota. Si usa per creare un nuovo torneo.
#
#torneo = aggiungiGiocatore(torneo, 'NomeX') Aggiunge al torneo un nuovo Giocatore 'nomeX'. Controlla per prima cosa che non esiste
#                                              un altro giocatore con lo stesso nome. In caso positivo viene aggiunto il Giocatore.
#                                              Gli viene assegnato un punteggio iniziale di 1440 e gli viene associato un numero d' iscrizione 
#                                              progressivo che lo rappresenta. Il Giocatore appena iscritto avra' fatto 0 partite.
#
#eliminaGiocatore(torneo,'nomeX')             Elimina dal torneo il Giocatore 'nomeX'. Nella torneo e nella classifica del torneo
#                                              al posto dei dati di tale giocatore sarà presente una riga del tipo ['ND',...] 
#
#aggiornaTorneo(torneo, m, n, r)             Calcola i punti ottenuti dopo che il giocatore m ha sfidato il giocatore n,
#                                              ottenendo un risultato r = 0 (sconfitta) oppure 0.5 (pareggio) oppure 1 (vittoria).
#                                              (m e n sono i numeri d' iscrizione dei due giocatori che partecipano al torneo).
#                                              Aggiorna quindi la torneo con i nuovi punteggi dei giocatori m e n.
#
#classifica(torneo)                           Ordina i giocatori nella torneo in ordine decrescente dei loro punteggi.
#                                              A parita' di punteggio il giocatore con piu' partite sarà ad una posizione piu' alta
#                                              di partite disputate.
#                                              Stampa, quindi, la classifica aggiornata.
######################################################################################################################################################