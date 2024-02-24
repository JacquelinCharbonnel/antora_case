#!/bin/env python3
import sys, re
from acquisition import from_file

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
    # programme principal
    f = open(sys.argv[1], "r")
    for line in f:
        lline = re.split(r' +',line.rstrip("\n"))
        l = from_file(lline)                     
        print(f"{l=}")
        print(f"{profondeur(l)=}")
