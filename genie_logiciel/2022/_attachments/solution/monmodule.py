#!/bin/env python3

import sys, re

def build(l0):
    """
    Cette fonction récursive construit la liste 
    à partir des arguments fournis sur la ligne de commande.
    Elle retourne la liste construite.
    """

    def _build():
        nonlocal i
        l = []          # liste courante
        while True:
            if l0[i]=="[":   # c'est une liste de listes
                i+=1                 # argument suivant
                if i!=1:             # pour la première liste, on ne fait rien
                    l.append(_build())    # sinon on construit cette sous-liste et on la met dans la liste courante
            elif l0[i]=="]": # c'est la fin de la liste,
                i+=1
                return l             # on renvoie la liste courante
            else:                  # c'est une liste d'entiers
                l.append(int(l0[i]))   
                i+=1
    i = 0
    res = _build()
    return res

def from_file(fn):
    listes = []
    f = open(fn, "r")
    for line in f:
        liste = re.split(r' +',line.rstrip("\n"))
        listes.append(build(liste))
    return listes

def from_keyboard():
    listes = []
    while True:
        line = input("? ").rstrip("\n").strip()
        if line=="":
            break
        liste = re.split(r' +',line.rstrip("\n"))
        listes.append(build(liste))
    return listes

def from_cmdline():
    return [ build(sys.argv[1:]) ]

def load():
    argc = len(sys.argv)
    print(argc)
    if argc==1:
        flat_list = from_keyboard()
    elif argc==2:
        flat_list = from_file(sys.argv[1])
    else:
        flat_list = from_cmdline()
    print(f"{flat_list=}")
    # exit()
    return flat_list

# print (from_cmdline())    
# print (from_keyboard())    
# print (from_file("listes.txt"))    