#!/bin/env python3
import sys, re, acquisition

"""
    Ce programme sort les listes listes dans lesaquelles les sous-listes sont triées.  
"""

def tri(l):
    def _tri(l):
        """
        Cette fonction récursive tri la liste passée en argument.
        """
        if type(l[0])==int:
            l.sort()
        else:
            for i in l:
                _tri(i)
    _tri(l)
    return l

if __name__=="__main__":
    acquisition.run(tri)
