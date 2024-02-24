#!/bin/env python3
import sys,re
from acquisition import from_cmdline, from_stdin, from_file

def minmax(l):
    def _minmax(l):
        """
        Cette fonction récursive retourne le minmax de la liste passée en argument.
        """
        if type(l[0])==int:
            maxi.append(max(l))
        else:
            for i in l:
                _minmax(i)
    maxi = []
    _minmax(l)
    return min(maxi)

if __name__=="__main__":
  if len(sys.argv)==1:  # depuis stdin
    while True:
        line = input("? ").rstrip("\n").strip()
        if line=="":
            break
        lline = re.split(r' +',line.rstrip("\n"))
        l = from_stdin(lline)                      # récupération d'une liste
        print(minmax(l))

  elif len(sys.argv)==2:  # depuis un fichier
    fl = open(sys.argv[1], "r")
    for line in fl:
      lline = re.split(r' +',line.rstrip("\n"))
      l = from_file(lline)                     # récupération d'une liste
      print(minmax(l))

  else: # depuis la ligne de commande
    l = from_cmdline()                         # récupération de la liste
    print(minmax(l))

