#!/usr/bin/env python3

import math
import sys
import json
import os
import re
import time
# import html
from shlex import quote

# cartella dei tornei
tornei_dir = os.path.dirname('r/')

def scriviTorneo(torneo):
	# scrivi su file
	with open(torneo['JSON_DATA'], 'w') as file_json:
		json.dump(torneo, file_json)


def importaTorneo(torneo):
	# leggi da file
	torneo_name = torneo.replace(" ", "_")
	
	file_path = tornei_dir + '/' + torneo_name + '/' + torneo_name + '.json'
	with open(file_path, 'r') as file_json:
		dict_torneo = json.load(file_json)

	aggiornaRanking(dict_torneo)

	return dict_torneo


# crea un nuovo torneo
def nuovoTorneo(nomeStr):
	# prevents errors in shell execution and escaping
	nome = nomeStr.replace(" ", "_")
	# percorso del file e cartella che conterra' il dizionario 
	dir_path = tornei_dir + '/' + nome
	file_path = dir_path + '/' + nome + '.json'
	imgs_path = dir_path + '/img'
	qr_path = imgs_path + '/qr.png'
	# logo_path = imgs_path + '/logo.png'

	# dizionario torneo base vuoto
	# vecchio: torneo = {'NOME': nome, 'FILE': file_path,
	torneo = {'NOME': nomeStr, 'FOLDER': dir_path, 'JSON_DATA': file_path,
		'GIOCATORI': {}, 'MATCHES': [], 'RANKING': [], 'LOGO': ''}

	# controlla se esiste la cartella col nome del torneo
	if (not os.path.exists(file_path) and not os.path.exists(dir_path)):
		os.makedirs(dir_path)
		os.makedirs(imgs_path)

		# controlla se esiste il file json del torneo se no lo crea e ci mette il contenuto dell'attuale dizionario
		# if not os.path.exists(file_path):
		# data
		with open(file_path, 'w') as fp:
			json.dump(torneo, fp)
		
		# qr
		qrApiUrl = "\"https://api.qrserver.com/v1/create-qr-code/?size=100x100&data=" + "http://flowin.space/pomelo/r/" + nome + "\""
		with open(qr_path, 'w') as fp:
			command = str("wget -O r/" + nome + "/img/qr.png " + qrApiUrl)
			os.system(command)
			# print("\n\nCOMMAND\n", command, '\n\n')
		
		# logo
		# with open(file_path, 'w') as fp:
		# 	json.dump(torneo, fp)

		costruisciIndexHtml(nome)
		costruisciIndexHtml('index')
		
		return
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
    # Elimina dal torneo il Giocatore 'NOME'. Nella torneo e nella classifica del
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


def nuoviPunteggiXY(torneo, giocatore1, giocatore2, risultato1):
    # Calcola i nuovi di due giocatori dopo una partita. Il risultato
    # è 1 se vince il primo giocatore, 0 se perde e 0.5 se pareggiano.

	for id in range(len(torneo['GIOCATORI'])):
		if torneo['GIOCATORI'][str(id)]['NOME'] == giocatore1:
			punteggio1 = int(torneo['GIOCATORI'][str(id)]['RANK'])
			matchX = int(torneo['GIOCATORI'][str(id)]['MATCH'])

	for id in range(len(torneo['GIOCATORI'])):
		if torneo['GIOCATORI'][str(id)]['NOME'] == giocatore2:
			punteggio2 = int(torneo['GIOCATORI'][str(id)]['RANK'])
			matchY = int(torneo['GIOCATORI'][str(id)]['MATCH'])

	#calcola risultato per il giocatore2
	risultato2 = 1 - risultato1

	#calcola risultato atteso per il giocatore1 e il giocatore2
	atteso1 = 1/2 + (math.atan((punteggio1 - punteggio2)/200)) / math.pi
	atteso2 = 1 - atteso1

	#calcolo coefficienti moltiplicativi per il giocatore1 e il giocatore2
	if (matchX > 9 and punteggio1 > 1569):
		coefficienteX = 10
	elif (matchX < 6):
		coefficienteX = 40
	else:
		coefficienteX = 20
	if (matchY > 9 and punteggio2 > 1569):
		coefficienteY = 10
	elif (matchY < 6):
		coefficienteY = 40
	else:
		coefficienteY = 20

	#calcolo punteggi parziali del giocatore1 e giocatore2
	parzialeX = round((risultato1 - atteso1) * coefficienteX)
	parzialeY = round((risultato2 - atteso2) * coefficienteY)

	#calcolo punteggi totali del giocatore1 e giocatore2
	punteggio1 = punteggio1 + parzialeX
	punteggio2 = punteggio2 + parzialeY

	return [punteggio1, punteggio2]


def aggiornaTorneo(torneo, giocatore1, giocatore2, risultato1):
    # Calcola i punti ottenuti dopo che il giocatore1 ha sfidato il giocatore2,
    # ottenendo un risultato1 = 0 (sconfitta) oppure 0.5 (pareggio) oppure 1
    # (vittoria). (giocatore1 e giocatore2 sono i numeri d' iscrizione dei
    # due giocatori che partecipano al torneo). Aggiorna quindi la torneo con i
    # nuovi punteggi dei giocatori giocatore1 e giocatore2.

	if (risultato1 != 1 and risultato1 != 0.5 and risultato1 != 0):
		print('Risultato della partita errato')
		return

	if (giocatore1 == giocatore2):
		print('Un giocatore non puo giocare contro se stesso')
		return

	trovato1 = False
	for id in range(len(torneo['GIOCATORI'])):
		if torneo['GIOCATORI'][str(id)]['NOME'] == giocatore1:
			trovato1 = True
	if not trovato1:
		print('GiocatoreX non presente al torneo')
		return

	trovato2 = False
	for id in range(len(torneo['GIOCATORI'])):
		if torneo['GIOCATORI'][str(id)]['NOME'] == giocatore2:
			trovato2 = True
	if not trovato2:
		print('GiocatoreY non presente al torneo')
		return

	else:
		#calcola nuovi punteggi del giocatore1 e giocatore2
		[nuovoPunteggio1, nuovoPunteggio2] = nuoviPunteggiXY(
			torneo, giocatore1, giocatore2, risultato1)

		#aggiornamento dati giocatore1 nel torneo
		for id in range(len(torneo['GIOCATORI'])):
			if torneo['GIOCATORI'][str(id)]['NOME'] == giocatore1:
				torneo['GIOCATORI'][str(id)]['RANK'] = nuovoPunteggio1
				torneo['GIOCATORI'][str(
					id)]['MATCH'] = torneo['GIOCATORI'][str(id)]['MATCH'] + 1

		#aggiornamento dati giocatore2 nel torneo
		for id in range(len(torneo['GIOCATORI'])):
			if torneo['GIOCATORI'][str(id)]['NOME'] == giocatore2:
				torneo['GIOCATORI'][str(id)]['RANK'] = nuovoPunteggio2
				torneo['GIOCATORI'][str(
					id)]['MATCH'] = torneo['GIOCATORI'][str(id)]['MATCH'] + 1

	now = time.localtime()
	dataora = str(now[3]) + ':' + str(now[4]) + ' - ' + \
            str(now[2]) + '/' + str(now[1])

	# aggiorna classifica
	aggiornaRanking(torneo)
	torneo['MATCHES'].append(
		(giocatore1, giocatore2, risultato1, '(' + dataora + ')'))

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
		rankingInstabiliTable = "<table id='rankingInstabili' class = 'table table-sm text-center table-bordered table-striped' ><thead><tr class='bg-danger text-white'></><th scope='row'>Giocatori fuori classifica</th><th></th><th></th></tr></thead><tbody>\n"
		
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
	partiteTable = "<table class = 'table table-sm text-center table-bordered table-striped' ><thead class=''><tr><th scope='col' style='border-right:none;'>   Giocatori<th scope='col' style='border-left:none;'></th><th scope='col'>Esito</th><th scope='col'>Data</th></tr></thead><tbody>\n"
	
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

def costruisciIndexHtml(torneo_in):
	torneo_in = torneo_in.replace(' ', '_')
	# is going to build the main index
	if(torneo_in == '_ALL_'):
		costruisciIndexHtml('index')
		for torneo_nome in listTornei():
			# torneo = importaTorneo(torneo_nome)
			# print(torneo)
			costruisciIndexHtml(torneo_nome)

	elif(torneo_in == 'index'):
		index_template = open('templates/index.html', 'r')
		new_index = open('index.html', 'w')
		tornei = listTornei('html')
	
		new_index_content = index_template.read().format(TORNEI=tornei)
		new_index.write(new_index_content)
		index_template.close()
		new_index.close()
	else:
		if(torneo_in in listTornei()):
			torneo = importaTorneo(torneo_in)
		else:
			torneo = nuovoTorneo(torneo_in)

		partite = partiteHtml(torneo)
		ranking = rankingHtml(torneo)
		giocatori = selectGiocatoriHtml(torneo)

		index_template = open('templates/tournament_index.html', 'r')
		new_index = open(torneo['FOLDER'] + '/' + 'index.html', 'w')

		if(torneo['LOGO'] != ''):
			logo_url = torneo['LOGO']
		else:
			logo_url = '/pomelo/img/pomelo.png'
	
		new_index_content = index_template.read().format(TORNEO=torneo['NOME'], MATCH=partite, RANKING=ranking, GIOCATORI=giocatori, LOGO=logo_url, URL=torneo['FOLDER'])
		new_index.write(new_index_content)
		index_template.close()
		new_index.close()
	
	# T E S T
	# print(new_index_content)


def listTornei(out='none'):
	dirs = os.listdir(tornei_dir)

	if(out == 'stout'):
		for torneo in dirs:
			print(torneo)
		return
	
	elif(out == 'html'):
		select = ''
		for torneo in sorted(dirs):
			select += "<option value='" + torneo + "'>" + torneo.replace("_", " ") + "</option>\n"
		return select
	else:
		return dirs


# parses php input and removes any single bracket
def parse(input):
	if(re.search("^[']{0,1}[A-z0-9 ]*[']{0,1}$", input)):
		return (input.replace("'", ""), 'argument')
	elif(re.search("^'{0,1}-{1,2}[A-z]*-{0,1}[A-z]*'{0,1}$", input)):
		return (input.replace("'", ""), 'option')
	else:
		print('INPUT ERRATO! Inserisci solo caratteri alfanumerici e spazi')
		return 



######################################################################################################################################################

HELP = 'Benvenuto in pomelo (interfaccia CLI), le opzioni sono le seguenti:\n\n  -l \t\t\t\t(--list) mostra la lista dei tornei in \'r/\'\n\n  -n TORNEO\t\t\t(--new) per creare un torneo con il nome indicato\n\n  TORNEO -i\t\t\t(--import) per caricare il file json del torneo con il nome indicato (data/NOMETORNEO/NOMETORNEO.json)\n  TORNEO -a GIOCATORE \t\t(--add) aggiunge GIOCATORE a TORNEO\n  TORNEO -d GIOCATORE\t\t(--delete) cancella (azzera i valori di) GIOCATORE in TORNEO\n  TORNEO -u G1 G2 RIS\t\t(--update) aggiorna TORNEO con il RIS (risultato) (0, 0.5, 1) del match tra G1 e G2\n  TORNEO -m\t\t\t(--match) mostra la lista dei match di TORNEO\n  TORNEO -g\t\t\t(--giocatori) mostra la lista dei giocatori in TORNEO\n  TORNEO -p\t\t\t(--print) mostra tutto il contenuto di TORNEO\n  TORNEO -r\t\t\t(--ranking) mostra la classifica di TORNEO\n\n  --help\t\t\tmostra questo messaggio\n'
ERR_INPUT = 'INPUT ERRATO! Inserisci solo caratteri alfanumerici e spazi\n'

######################################################################################################################################################

debug=False
# debug=True

## sezione opzioni script
if(len(sys.argv) > 1):  # getting parameters if exist
	# divides input in option and arguments while safe parsing them
	args = {'option': [], 'arguments': []}
	
	# print(args['option'])
	for arg in sys.argv[1:]:
		parsed = parse(arg)
		
		if(debug):
			print("argv parsed = ", parsed)
		
		# get them string values 
		if(parsed[1] == 'argument'):
			args['arguments'].append(parsed[0])
		elif(parsed[1] == 'option'):
			args['option'].append(parsed[0])

	# first option
	option_arg = args['option'][0]

	## lista dei tornei
	if(option_arg == '-l' or option_arg == '--list'):
		listTornei('stout')
	
	## HELP
	elif(option_arg == '-h' or option_arg == '--help'):
		print(HELP)


	## piu di un argomento
	if(len(args['arguments'])):
		# first argument
		torneo_arg = args['arguments'][0]
		# first option
		option_arg = args['option'][0]
		
		if(debug):
			print("torneo_arg = ", torneo_arg)
			print("option_arg = ", option_arg)

		if(option_arg == '-n' or option_arg == '--new'):
			nuovoTorneo = nuovoTorneo(torneo_arg)
			tornei = {torneo_arg: nuovoTorneo}
			
			if(nuovoTorneo):
				print("Torneo creato, segui l'help per popolarlo")

		elif(option_arg == '--gen-index'):
			# if (torneo_arg != 'index' and torneo_arg != '_ALL_'):
				# torneo = importaTorneo(torneo_arg)
			costruisciIndexHtml(torneo_arg)
		
		elif(option_arg == '-i' or option_arg == '--import'):
				torneo = importaTorneo(torneo_arg)
				tornei = {torneo['NOME']: torneo}

		elif(option_arg == '-p' or option_arg == '--print'):
				torneo = importaTorneo(torneo_arg)
				stampaFormattato(torneo)

		elif(option_arg == '-a' or option_arg == '--add'):
				torneo = importaTorneo(torneo_arg)

				if(len(args['arguments']) > 1):
					giocatore = args['arguments'][1]
					aggiungiGiocatore(torneo, giocatore)
				else:
					print('Manca il nome del giocatore!')

		elif(option_arg == '-d' or option_arg == '--delete'):
				torneo = importaTorneo(torneo_arg)

				if(len(args['arguments']) > 1):
					giocatore = args['arguments'][1]

					eliminaGiocatore(torneo, giocatore)

				else:
					print('Manca il nome del giocatore!')


		elif(option_arg == '-u' or option_arg == '--update'):
				torneo = importaTorneo(torneo_arg)

				if(len(args['arguments']) > 3):
					giocatore1 = args['arguments'][1]
					giocatore2 = args['arguments'][2]
					esito_match = float(args['arguments'][3])			# [0, 0.5, 1]

					aggiornaTorneo(torneo, giocatore1, giocatore2, esito_match)

				else:
					print('Manca qualcosa! Inserisci Giocatore1 Giocatore2 Risultato')

		elif(option_arg == '-r' or option_arg == '--ranking'):
				torneo = importaTorneo(torneo_arg)
				
				ranking = rankingStabile(torneo)

				caratteri_omessi = ",'[(]"
				caratteri_sostituiti = ")"

				if any("--html" in o for o in args['option']):
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
		elif(option_arg == '-g' or option_arg == '--giocatori'):
				torneo = importaTorneo(torneo_arg)

				if any("--html" in o for o in args['option']):
					print(selectGiocatoriHtml(torneo))

				else:
					giocatori = str(selectGiocatori(torneo))
					caratteri_omessi = "'[(])"
					caratteri_sostituiti = ", "

					for char in caratteri_omessi:
						giocatori = giocatori.replace(char, '')

					giocatori = giocatori.replace(caratteri_sostituiti, '\n')
					print(giocatori)


		elif(option_arg == '-m' or option_arg == '--match'):
			torneo = importaTorneo(torneo_arg)
			
			# la lista invertita per visualizzare l'ultima in alto
			matches = torneo['MATCHES']
			matchlist = ""

			if any("--html" in o for o in args['option']):
				print(partiteHtml(torneo))

			else:
				for match in matches:
					# esito, conversione profeta -> mondo
					if(match[2] == 0.5):
						esito = 'X'
					elif(match[2] == 1.0):
						esito = '1'
					else:
						esito = '2'
						
					matchlist += match[0] + " - " + match[1] + ": " + esito + " " + match[3] + "\n"

				print(matchlist)

		else:
			print('Manca il nome del torneo!')
else:
	print(HELP)
