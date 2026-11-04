"""Si vuole analizzare una playlist per una festa. Scrivi un programma in Python strutturato nelle seguenti funzioni:

crea_playlist():
Chiede all'utente quante canzoni sono state aggiunte alla playlist.
Con un ciclo for, acquisisce per ogni traccia:
Il titolo del brano.
Il genere musicale (es. , , , ).
Restituisce un dizionario del tipo titolo_brano: genere.

filtra_generi(playlist):Scorre il dizionario e costruisce un set contenente tutti i generi musicali presenti nella playlist.
Stampa quanti generi diversi sono rappresentati e li elenca a schermo.
Restituisce il set ottenuto.

gestisci_genere(playlist, generi_disponibili):
Chiede all'utente di digitare il nome di un genere per una verifica rapida:
Con un'istruzione if, controlla se il genere è contenuto nel set.
Se è presente: usa un ciclo for per elencare tutti i brani associati a quel genere e conta quante tracce lo compongono.
Se non è presente: informa che nessun brano corrisponde a quella categoria e suggerisce all'utente di provare con uno dei generi presenti nel set."""

def crea_playlist():
  numero_canzoni=int(input("numero canzoni nelle playlist? "))
  elenco={}
  for i in range(0, numero_canzoni):
    titolo_brano=input("inserisci il titolo del brano? ")
    genere_brano=input("inserisci il genere del brano? ")
    elenco[titolo_brano]=genere_brano

  return elenco

def filtra_generi(playlist): 
  filtro=set(playlist.values())
  #for genere in playlist.values():
  # filtro.add(genere)
  return filtro
   
  
elenco=crea_playlist()
print(elenco)
print(filtra_generi(elenco))
  
def gestisci_genere(playlist, generi_disponibili):
  
  
  
  