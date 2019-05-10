def nuoviPunteggiXY(torneo, giocatoreX, giocatoreY, risultatoX):
	for id in range(len(torneo['GIOCATORI'])):
		if torneo['GIOCATORI'][id]['NOME'] == giocatoreX:
			punteggioX = torneo['GIOCATORI'][id]['PUNTI']
			partiteX = torneo['GIOCATORI'][id]['PARTITE']
	for id in range(len(torneo['GIOCATORI'])):
		if torneo['GIOCATORI'][id]['NOME'] == giocatoreY:
			punteggioY = torneo['GIOCATORI'][id]['PUNTI']
			partiteY = torneo['GIOCATORI'][id]['PARTITE']

	#calcola risultato per il giocatoreY
	risultatoY = 1 - risultatoX

	#calcola risultato atteso per il giocatoreX e il giocatoreY
	attesoX = 1/2 + (math.atan((punteggioX - punteggioY)/200)) / math.pi
	attesoY = 1 - attesoX
	
	#calcolo coefficienti moltiplicativi per il giocatoreX e il giocatoreY 
	if (partiteX > 8 and punteggioX > 1600):
		coefficienteX = 10
	elif (partiteX < 6):
		coefficienteX = 40
	else:
		coefficienteX = 20
	if (partiteY > 8 and punteggioY > 1600):
		coefficienteY = 10
	elif (partiteY < 6):
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
				torneo['GIOCATORI'][id]['PARTITE'] = torneo['GIOCATORI'][id]['PARTITE'] + 1

		#aggiornamento dati giocatoreY nel torneo
		for id in range(len(torneo['GIOCATORI'])):
			if torneo['GIOCATORI'][id]['NOME'] == giocatoreY:
				torneo['GIOCATORI'][id]['PUNTI'] = nuovoPunteggioY
				torneo['GIOCATORI'][id]['PARTITE'] = torneo['GIOCATORI'][id]['PARTITE'] + 1
		return 