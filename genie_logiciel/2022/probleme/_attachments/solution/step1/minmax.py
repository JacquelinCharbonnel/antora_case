#!/bin/env python3
import sys
from acquisition import from_cmdline

def minmax(l):
    """
    Cette fonction récursive retourne le minmax de la liste passée en argument.
    """
    if type(l[0])==int:
        maxi.append(max(l))
    else:
        for i in l:
            minmax(i)

if __name__=="__main__":
    # programme principal
    l = from_cmdline()                   # récupération de la liste
    maxi = []
    minmax(l)
    print(min(maxi))
