#!/usr/bin/env python3
from math import atan, pi
import sys, json
from collections import OrderedDict

class TornElo(object):
    def __init__(self,nome):
        self.nome = nome
        self.giocatori = {}

    def __str__(self):
        s = "="*(len(self.nome)+2)+"\n "+self.nome+"\n"+"="*(len(self.nome)+2)+"\n"
        for id in self.classifica():
            s+=str(self.giocatori[id]['NOME'])
            s+=" ("+str(self.giocatori[id]['ID'])+"):"
            s+="\t"+str(self.giocatori[id]['PUNTI'])+" pt"
            s+="\t("+str(self.giocatori[id]['MATCH'])+" partite)\n"
        return s

    def aggiungiGiocatore(self,nome):
        """
        Aggiunge al torneo un nuovo Giocatore 'nome'. Controlla per prima cosa che
        non esiste un altro giocatore con lo stesso nome. In caso positivo viene
        aggiunto il Giocatore. Gli viene assegnato un punteggio iniziale di 1440 e
        gli viene associato un numero d' iscrizione.
        """
	#controlla che non ci sia un giocatore con lo stesso NOME
        for id in range(len(self.giocatori)):
            if self.giocatori[id]['NOME'] == nome:
                print('Nome gia in uso: scegliere un altro NOME')
                return
	
	# crea un dizionario ausiliario che verra' copiato nel torneo, l'ID e' anche chiave (univoca)
        nuovoID = self.nome + '_' + str(len(self.giocatori))
        nuovoGiocatore = {'NOME' : nome, 'ID' : nuovoID, 'PUNTI' : 1440, 'MATCH' : 0}

	# aggiunge il nuovo giocatore al torneo
        self.giocatori[len(self.giocatori)] = nuovoGiocatore
    
    def eliminaGiocatore(self, nome):
        """
        Elimina dal torneo il Giocatore 'nome'. Nella torneo e nella classifica del
        torneo al posto dei dati di tale giocatore sara' presente una riga del tipo
        ['ND',...] 
        """
        for id in range(len(self.giocatori)):
            if self.giocatori[id]['NOME'] == nome:
                # imposta valori oltre i limiti al posto di cancellare, preserva l'ID
                self.giocatori[id]['NOME'] = 'ND'
                self.giocatori[id]['PUNTI'] = -9999
                self.giocatori[id]['MATCH'] = -1
                break

    def cercaGiocatore(self,nome):
        for id in range(len(self.giocatori)):
            if self.giocatori[id]['NOME'] == nome:
                return True
        return False

    def aggiornaPunteggioX(self,nome,nuovoPunteggio):
        """
        Cambia il punteggio del giocatore 'nome'
        (incrementa di 1 il valore 'MATCH')
        """
        if self.cercaGiocatore(nome):
            for id in range(len(self.giocatori)):
                if self.giocatori[id]['NOME'] == nome:
                    self.giocatori[id]['PUNTI'] = nuovoPunteggio
                    self.giocatori[id]['MATCH'] = self.giocatori[id]['MATCH'] + 1
        else:
            print("Giocatore "+nome+" non trovato.")


    def nuoviPunteggiXY(self,giocatoreX,giocatoreY,risultatoX):
        """
        Calcola i nuovi di due giocatori dopo una partita. Il risultato 
        è 1 se vince il primo giocatore, 0 se perde e 0.5 se pareggiano.
        """
        #TODO: Ritornare errori se i giocatori non esistono
        for id in range(len(self.giocatori)):
            if self.giocatori[id]['NOME'] == giocatoreX:
                punteggioX = self.giocatori[id]['PUNTI']
                MATCHX = self.giocatori[id]['MATCH']

        for id in range(len(self.giocatori)):
            if self.giocatori[id]['NOME'] == giocatoreY:
                punteggioY = self.giocatori[id]['PUNTI']
                MATCHY = self.giocatori[id]['MATCH']

        #calcola risultato per il giocatoreY
        risultatoY = 1 - risultatoX
        
        #calcola risultato atteso per il giocatoreX e il giocatoreY
        attesoX = 1/2 + (atan((punteggioX - punteggioY)/200)) / pi
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

    def aggiornaPunteggi(self,giocatoreX,giocatoreY,risultatoX):
        """
        Calcola i punti ottenuti dopo che il giocatoreX ha sfidato il giocatoreY,
        ottenendo un risultatoX = 0 (sconfitta) oppure 0.5 (pareggio) oppure 1
        (vittoria). (giocatoreX e giocatoreY sono i numeri d' iscrizione dei
        due giocatori che partecipano al torneo). Aggiorna quindi la torneo con i
        nuovi punteggi dei giocatori giocatoreX e giocatoreY.
        """
        if not self.cercaGiocatore(giocatoreX):
            print('GiocatoreX non presente al torneo')
            return

        if not self.cercaGiocatore(giocatoreY):
            print('GiocatoreY non presente al torneo')
            return

        if (giocatoreX == giocatoreY):
            print('Un giocatore non puo giocare contro se stesso')
            return

        if (risultatoX != 1 and risultatoX != 0.5 and risultatoX != 0):
            print('Risultato della partita errato')
            return  

        #calcola nuovi punteggi del giocatoreX e giocatoreY
        [nuovoPunteggioX, nuovoPunteggioY] = self.nuoviPunteggiXY(giocatoreX,giocatoreY,risultatoX)
        self.aggiornaPunteggioX(giocatoreX,nuovoPunteggioX)
        self.aggiornaPunteggioX(giocatoreY,nuovoPunteggioY)

    def classifica(self):
        """
        Ordina il dizionario self.giocatori rispetto ai punteggi
        """
        classifica = OrderedDict(sorted(self.giocatori.items(), key = lambda kv: kv[1]['PUNTI'], reverse=True))
        return classifica 
