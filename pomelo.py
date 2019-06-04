#!/usr/bin/env python3

import math
import sys
import json
import os.path
import time

# cartella dei tornei
tornei_dir = os.path.dirname('r/')

def scriviTorneo(torneo):
	# scrivi su file
	with open(torneo['JSON_DATA'], 'w') as file_json:
		json.dump(torneo, file_json)


def importaTorneo(torneo):
	# leggi da file
	file_path = tornei_dir + '/' + str(torneo) + '/' + str(torneo) + '.json'
	with open(file_path, 'r') as file_json:
		dict_torneo = json.load(file_json)

	aggiornaRanking(dict_torneo)

	return dict_torneo


# crea un nuovo torneo
def nuovoTorneo(nome):

	# percorso del file e cartella che conterra' il dizionario
	dir_path = tornei_dir + '/' + nome
	file_path = dir_path + '/' + nome + '.json'
	# dir_path = os.path.dirname(file_path)
	# dir_path = os.path.dirname(tornei_dir + '/' + nome + '/' + file_name)

	# dizionario torneo base vuoto
	# torneo = {'NOME': nome, 'FILE': file_path,
	torneo = {'NOME': nome, 'FOLDER': dir_path, 'JSON_DATA': 'file_path',
           'GIOCATORI': {}, 'MATCHES': [], 'RANKING': []}

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
	nuovoGiocatore = {'NOME': nome, 'ID': nuovoID, 'RANK': 1440, 'MATCH': 0}

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
			torneo['GIOCATORI'][str(id)]['RANK'] = -9999
			torneo['GIOCATORI'][str(id)]['MATCH'] = -1

	# scrivi su file
	scriviTorneo(torneo)


def nuoviPunteggiXY(torneo, giocatoreX, giocatoreY, risultatoX):
    # Calcola i nuovi di due giocatori dopo una partita. Il risultato
    # è 1 se vince il primo giocatore, 0 se perde e 0.5 se pareggiano.

	for id in range(len(torneo['GIOCATORI'])):
		if torneo['GIOCATORI'][str(id)]['NOME'] == giocatoreX:
			punteggioX = int(torneo['GIOCATORI'][str(id)]['RANK'])
			matchX = int(torneo['GIOCATORI'][str(id)]['MATCH'])

	for id in range(len(torneo['GIOCATORI'])):
		if torneo['GIOCATORI'][str(id)]['NOME'] == giocatoreY:
			punteggioY = int(torneo['GIOCATORI'][str(id)]['RANK'])
			matchY = int(torneo['GIOCATORI'][str(id)]['MATCH'])

	#calcola risultato per il giocatoreY
	risultatoY = 1 - risultatoX

	#calcola risultato atteso per il giocatoreX e il giocatoreY
	attesoX = 1/2 + (math.atan((punteggioX - punteggioY)/200)) / math.pi
	attesoY = 1 - attesoX

	#calcolo coefficienti moltiplicativi per il giocatoreX e il giocatoreY
	if (matchX > 9 and punteggioX > 1569):
		coefficienteX = 10
	elif (matchX < 6):
		coefficienteX = 40
	else:
		coefficienteX = 20
	if (matchY > 9 and punteggioY > 1569):
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
		[nuovoPunteggioX, nuovoPunteggioY] = nuoviPunteggiXY(
			torneo, giocatoreX, giocatoreY, risultatoX)

		#aggiornamento dati giocatoreX nel torneo
		for id in range(len(torneo['GIOCATORI'])):
			if torneo['GIOCATORI'][str(id)]['NOME'] == giocatoreX:
				torneo['GIOCATORI'][str(id)]['RANK'] = nuovoPunteggioX
				torneo['GIOCATORI'][str(
					id)]['MATCH'] = torneo['GIOCATORI'][str(id)]['MATCH'] + 1

		#aggiornamento dati giocatoreY nel torneo
		for id in range(len(torneo['GIOCATORI'])):
			if torneo['GIOCATORI'][str(id)]['NOME'] == giocatoreY:
				torneo['GIOCATORI'][str(id)]['RANK'] = nuovoPunteggioY
				torneo['GIOCATORI'][str(
					id)]['MATCH'] = torneo['GIOCATORI'][str(id)]['MATCH'] + 1

	now = time.localtime()
	dataora = str(now[3]) + ':' + str(now[4]) + ' - ' + \
            str(now[2]) + '/' + str(now[1])

	# aggiorna classifica
	aggiornaRanking(torneo)
	torneo['MATCHES'].append(
		(giocatoreX, giocatoreY, risultatoX, '(' + dataora + ')'))

	return scriviTorneo(torneo)


####### sezione di output

def stampaFormattato(torneo):
	caratteri_omessi = '"{}'
	torneo_formatted = json.dumps(torneo, indent=3, separators=('', ':\t'))

	for char in caratteri_omessi:
		torneo_formatted = torneo_formatted.replace(char, '')

	print(torneo_formatted)

def aggiornaRanking(torneo):
	classifica = []

	for i in torneo['GIOCATORI']:
		if(torneo['GIOCATORI'][i]['RANK'] > 0):						# rank non negativi
			nome = torneo['GIOCATORI'][i]['NOME']
			rank = torneo['GIOCATORI'][i]['RANK']
			partite = torneo['GIOCATORI'][i]['MATCH']

			if(torneo['GIOCATORI'][i]['MATCH'] > 5):
				stabile = True

			else:
				stabile = False

			classifica.append((nome, rank, partite, stabile))
			classifica = sorted(classifica, key=lambda giocatore: (
				giocatore[1], giocatore[2]), reverse=True)  # sort su due criteri (punteggio, partite)

	torneo['RANKING'] = classifica

def rankingStabile(torneo):
	ranking = {'stabili': [], 'instabili': []}

	if(torneo['NOME'] == 'singolo'):
		ranking['n_min_partite'] = 16
	else:
		ranking['n_min_partite'] = 8

	for giocatore in torneo['RANKING']:
		if (giocatore[-1]):
			ranking['stabili'].append(giocatore[0:3])
		else:
			ranking['instabili'].append(giocatore[0:3])
	
	return ranking

def selectGiocatori(torneo):
	# torneo = importaTorneo(torneo)
	giocatori = []

	for gid in torneo['GIOCATORI']:
		giocatori.append(torneo['GIOCATORI'][gid]['NOME'])
		# print(gid, giocatori)

	giocatori.sort()

	return giocatori


def selectGiocatoriHtml(torneo):
	select = ""

	for giocatore in selectGiocatori(torneo):
		select += "<option value='" + giocatore + "'>" + giocatore + "</option>\n"

	return select


def rankingHtml(torneo):
	rankingTable = "<table class = 'table table-sm text-center table-bordered table-striped' ><thead class=''><tr><th scope='col'>Giocatore</th><th scope='col'>Punti</th><th scope='col'>Match</th></tr></thead><tbody>\n"
	
	torneo_rank = rankingStabile(torneo)

	# giocatori stabili
	for giocatore in torneo_rank['stabili']:
		# i evidenzia i primi 8 giocatori, selezionati per le eliminatorie
		if(torneo_rank['stabili'].index(giocatore) < torneo_rank['n_min_partite']):
			classColore = 'table-success success'
		else:
			classColore = ''
		
		rankingTable += "<tr class='" + classColore + "'>\n"
		rankingTable += "    <td>" + str(giocatore[0]) + "</td>\n"
		rankingTable += "    <td>" + str(giocatore[1]) + "</td>\n"
		rankingTable += "    <td>" + str(giocatore[2]) + "</td>\n"
		rankingTable += "</tr>\n"

	if(len(torneo_rank['instabili'])):
		# print("<table class = 'table table-sm text-center table-bordered table-striped' ><thead><tr class='bg-danger text-white'></><th scope='row'>Giocatori fuori classifica</th><th></th><th></th></tr></thead><tbody>")
		rankingInstabiliTable = "<table class = 'table table-sm text-center table-bordered table-striped' ><thead><tr class='bg-danger text-white'></><th scope='row'>Giocatori fuori classifica</th><th></th><th></th></tr></thead><tbody>\n"
		
		# giocatori instabili
		for giocatore in torneo_rank['instabili']:
			rankingInstabiliTable += "<tr>\n"
			rankingInstabiliTable += "    <td>" + str(giocatore[0]) + "</td>\n"
			rankingInstabiliTable += "    <td>" + str(giocatore[1]) + "</td>\n"
			rankingInstabiliTable += "    <td>" + str(giocatore[2]) + "</td>\n"
			rankingInstabiliTable += "</tr>\n"

		rankingInstabiliTable += "</table>\n"

		return rankingTable + rankingInstabiliTable

def partiteHtml(torneo):
	partite = torneo['MATCHES'][::-1]
	partiteTable = "<table class = 'table table-sm text-center table-bordered table-striped' ><thead class=''><tr><th scope='col'>Giocatori<th scope='col'></th><th scope='col'>Esito</th><th scope='col'>Data</th></tr></thead><tbody>\n"
	
	for match in partite:
		partiteTable += "<tr>\n"
		partiteTable += "    <td>" + str(match[0]) + "</td>\n"
		partiteTable += "    <td>" + str(match[1]) + "</td>\n"
		# rimuove la virgola e cambia sistema risultato da algoritmo (0,1) a 1, x, 2
		partiteTable += "    <td>" + str(2 - int(match[2])) + "</td>\n"
		# rimuove le parentesi
		partiteTable += "    <td>" + str(match[3])[1:-1] + "</td>\n"
		partiteTable += "</tr>\n"
	
	partiteTable += "</table>"
	
	return partiteTable
	# print("</table>")

def costruisciIndexHtml(torneo):
	partite = partiteHtml(torneo)
	ranking = rankingHtml(torneo)
	giocatori = selectGiocatoriHtml(torneo)

	index_template = open('templates/tournament_index.html', 'r')
	new_index = open(torneo['FOLDER'] + '/' + 'index.html', 'w')
	
	new_index_content = index_template.read().format(MATCH=partite, RANKING=ranking, GIOCATORI=giocatori)
	
	# T E S T
	# print(new_index_content)
	new_index.write(new_index_content)

	index_template.close()
	new_index.close()

def listTornei():
	for torneo in os.listdir(tornei_dir):
		print(torneo)

######################################################################################################################################################
#COMANDO:                                      A COSA SERVE:

# il dizionario TORNEI contiene tutti i tornei (dizionari a loro volta) con il nome come chiave del torneo, all'int

#
#                                              progressivo che lo rappresenta. Il Giocatore appena iscritto avra' fatto 0 MATCH.
#
#
#
#aggiornaRanking(torneo)                           Ordina i giocatori nella torneo in ordine decrescente dei loro punteggi.
#                                              A parita' di punteggio il giocatore con piu' MATCH sara' ad una posizione piu' alta
#                                              di MATCH disputate.
#                                              Stampa, quindi, la classifica aggiornata.
######################################################################################################################################################

HELP = 'Benvenuto in pomelo (interfaccia CLI), le opzioni sono le seguenti:\n\n  -l \t\t\t\t(--list) mostra la lista dei tornei in \'r/\'\n  -n TORNEO\t\t\t(--new) per creare un torneo con il nome indicato\n  -i TORNEO\t\t\t(--import) per caricare il file json del torneo con il nome indicato (data/NOMETORNEO/NOMETORNEO.json)\n  -a TORNEO GIOCATORE \t\t(--add) aggiunge GIOCATORE a TORNEO\n  -d TORNEO GIOCATORE\t\t(--delete) cancella (azzera i valori di) GIOCATORE in TORNEO\n  -u TORNEO G1 G2 RIS\t\t(--update) aggiorna TORNEO con il RIS (risultato) (0, 0.5, 1) del match tra G1 e G2\n  -m TORNEO\t\t\t(--match) mostra la lista dei match di TORNEO\n  -g TORNEO\t\t\t(--giocatori) mostra la lista dei giocatori in TORNEO\n  -p TORNEO\t\t\t(--print) mostra tutto il contenuto di TORNEO\n  -r TORNEO\t\t\t(--ranking) mostra la classifica di TORNEO\n  --help\t\t\tmostra questo messaggio\n  --test\t\t\tusa dei tornei di test\n'


## sezione opzioni script
if(len(sys.argv) > 1):  # getting parameters if exist
	options = sys.argv

	## lista dei tornei
	if(options[1] == '-l' or options[1] == '--list'):
		listTornei()
	
	## HELP
	elif(options[1] == '-h' or options[1] == '--help'):
		print(HELP)

	## piu di un argomento
	elif(len(options)>2):
		if(options[1] == '-n' or options[1] == '--new'):
				nuovoTorneo = nuovoTorneo(options[2])
				tornei = {options[2]: nuovoTorneo}

				print("Torneo creato, segui l'help per popolarlo")

		elif(options[1] == '--gen-index'):
			torneo = options[2]
			costruisciIndexHtml(torneo)
		
		elif(options[1] == '-i' or options[1] == '--import'):
				torneo_test = options[2]
				torneo = importaTorneo(torneo_test)
				tornei = {torneo['NOME']: torneo}

		elif(options[1] == '-p' or options[1] == '--print'):
				torneo = options[2]
				torneo = importaTorneo(torneo)
				stampaFormattato(torneo)

		elif(options[1] == '-a' or options[1] == '--add'):
				torneo = options[2]
				torneo = importaTorneo(torneo)

				if(len(options) > 3):
					giocatore = options[3]
					aggiungiGiocatore(torneo, giocatore)
				else:
					print('Manca il nome del giocatore!')

		elif(options[1] == '-d' or options[1] == '--delete'):
				torneo = options[2]
				torneo = importaTorneo(torneo)

				if(len(options) > 3):
					giocatore = options[3]

					eliminaGiocatore(torneo, giocatore)

				else:
					print('Manca il nome del giocatore!')


		elif(options[1] == '-u' or options[1] == '--update'):
				torneo = options[2]
				torneo = importaTorneo(torneo)

				if(len(options) > 5):
					giocatore1 = options[3]
					giocatore2 = options[4]
					esito_match = float(options[5])			# [0, 0.5, 1]

					aggiornaTorneo(torneo, giocatore1, giocatore2, esito_match)

				else:
					print('Manca qualcosa! Inserisci Giocatore1 Giocatore2 Risultato')

		elif(options[1] == '-r' or options[1] == '--ranking'):
				torneo = options[2]
				torneo = importaTorneo(torneo)
				
				ranking = rankingStabile(torneo)

				caratteri_omessi = ",'[(]"
				caratteri_sostituiti = ")"

				if any("--html" in o for o in options):
					print(rankingHtml(torneo))

				else:
					ranking_str = ' ' + str(ranking['stabili'])

					if(len(ranking['instabili'])):
						ranking_str += '\n== Match < 6 ==\n ' + str(ranking['instabili'])

					for char in caratteri_omessi:
						ranking_str = ranking_str.replace(char, '')

					ranking_str = ranking_str.replace(caratteri_sostituiti, '\n')

					print(ranking_str)


		## lista dei giocatori
		elif(options[1] == '-g' or options[1] == '--giocatori'):
				torneo = importaTorneo(options[2])

				if any("--html" in o for o in options):
					print(selectGiocatoriHtml(torneo))

				else:
					giocatori = str(selectGiocatori(torneo))
					caratteri_omessi = "'[(])"
					caratteri_sostituiti = ", "

					for char in caratteri_omessi:
						giocatori = giocatori.replace(char, '')

					giocatori = giocatori.replace(caratteri_sostituiti, '\n')
					print(giocatori)


		elif(options[1] == '-m' or options[1] == '--match'):
				torneo = options[2]
				torneo = importaTorneo(torneo)
				# la lista invertita per visualizzare l'ultima in alto
				# matches = torneo['MATCHES'][::-1]
				# la lista NON invertita per visualizzare l'ultima in basso da TERMINALE
				matches = torneo['MATCHES']

				if any("--html" in o for o in options):
					print(partiteHtml(torneo))

				else:
					matches = ' ' + str(matches)

					matches = matches.replace('[', '')
					matches = matches.replace('],', '\n')
					matches = matches.replace(', 0.0', ': 2')
					matches = matches.replace(', 0.5', ': X')
					matches = matches.replace(', 1.0', ': 1')
					matches = matches.replace('1,', '1')
					matches = matches.replace('X,', 'X')
					matches = matches.replace('2,', '2')
					matches = matches.replace(', ', ' - ')
					# matches = matches.replace('- (', ' ')

					caratteri_omessi = "[]',"
					for char in caratteri_omessi:
						matches = matches.replace(char, '')

					print(matches)

				torneo_test = options[2]

	else:
		print('Manca il nome del torneo!')
else:
	print(HELP)
