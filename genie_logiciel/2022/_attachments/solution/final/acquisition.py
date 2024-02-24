#!/bin/env python3
import sys,re

def from_stdin(lline):
    def _mklist():
        nonlocal i
        l = []          # liste courante
        while True:
            if lline[i]=="[":   # c'est une liste de listes
                i+=1                 # argument suivant
                if i!=1:             # pour la première liste, on ne fait rien
                    l.append(_mklist())    # sinon on construit cette sous-liste et on la met dans la liste courante
            elif lline[i]=="]": # c'est la fin de la liste,
                i+=1
                return l             # on renvoie la liste courante
            else:                  # c'est une liste d'entiers
                l.append(int(lline[i]))   
                i+=1
    i = 0
    return _mklist()

def from_file(l0):
    """
    Cette fonction construit la liste 
    correspondant à la représentation chaine de caractère fourni en argument.
    """

    def _build():
        nonlocal i
        l = []          # sous-liste courante
        while True:
            if l0[i]=="[":   # c'est une sous-liste de listes
                i+=1                 
                if i!=1:             # pour la première sous-liste, on ne fait rien
                    l.append(_build())    # sinon on construit cette sous-liste et on la met dans la sous-liste courante
            elif l0[i]=="]": # c'est la fin de la sous-liste courante,
                i+=1
                return l             # on renvoie la sous-liste courante
            else:                  # c'est une sous-liste d'entiers
                l.append(int(l0[i]))   
                i+=1
    i = 0
    res = _build()
    return res

def from_cmdline():
    """
    Cette fonction construit la liste 
    à partir des arguments fournis sur la ligne de commande.
    Elle retourne la liste construite.
    """
    def _construire():
        nonlocal i  
        l = []          
        while True:
            if sys.argv[i]=="[":   
                i+=1               
                if i!=2:                  # pour la première liste, on ne fait rien
                    l.append(_construire()) 
            elif sys.argv[i]=="]":        # c'est la fin de la liste,
                i+=1
                return l                  # on renvoie la liste constuite
            else:                         # c'est une liste d'entiers
                l.append(int(sys.argv[i]))   
                i+=1
    i = 1                              # indice pour parcourir les arguments
    return _construire()

def run(f):
  if len(sys.argv)==1:  # depuis stdin
    while True:
        line = input("? ").rstrip("\n").strip()
        if line=="":
            break
        lline = re.split(r' +',line.rstrip("\n"))
        l = from_stdin(lline)                      # récupération d'une liste
        print(f(l))

  elif len(sys.argv)==2:  # depuis un fichier
    fl = open(sys.argv[1], "r")
    for line in fl:
      lline = re.split(r' +',line.rstrip("\n"))
      l = from_file(lline)                     # récupération d'une liste
      print(f(l))

  else: # depuis la ligne de commande
    l = from_cmdline()                         # récupération de la liste
    print(f(l))

