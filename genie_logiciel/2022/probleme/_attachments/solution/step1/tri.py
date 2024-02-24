#!/bin/env python3
import sys, re
from acquisition import from_stdin

def tri(l):
    """
    Cette fonction récursive tri la liste passée en argument.
    """
    if type(l[0])==int:
        l.sort()
    else:
        for i in l:
            tri(i)

if __name__=="__main__":
    # programme principal

    while True:
        line = input("? ").rstrip("\n").strip()
        if line=="":
            break
        lline = re.split(r' +',line.rstrip("\n"))
        l = from_stdin(lline)                      # récupération d'une liste
        tri(l)
        print(f"{l=}")
