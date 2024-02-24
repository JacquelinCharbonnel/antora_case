#!/bin/env python3
import sys, re
from acquisition import from_cmdline, from_stdin, from_file

def profondeur(l):
    """
    Cette fonction renvoie la profondeur de la liste passée en argument.
    """

    def _profondeur(l,p):
        nonlocal prof
        for i in l:
            if type(i)==int:
                if p>prof:
                    prof = p
            else:
                _profondeur(i,p+1)

    prof=float("-inf")
    _profondeur(l,1)
    return(prof)

if __name__=="__main__":
  if len(sys.argv)==1:  # depuis stdin
    while True:
        line = input("? ").rstrip("\n").strip()
        if line=="":
            break
        lline = re.split(r' +',line.rstrip("\n"))
        l = from_stdin(lline)                      # récupération d'une liste
        print(profondeur(l))

  elif len(sys.argv)==2:  # depuis un fichier
    fl = open(sys.argv[1], "r")
    for line in fl:
      lline = re.split(r' +',line.rstrip("\n"))
      l = from_file(lline)                     # récupération d'une liste
      print(profondeur(l))

  else: # depuis la ligne de commande
    l = from_cmdline()                         # récupération de la liste
    print(profondeur(l))
