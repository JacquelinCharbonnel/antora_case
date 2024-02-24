#!/bin/env python3
import sys, acquisition

"""
    Ce programme sort le min des max des listes lues.  
"""

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
    acquisition.run(minmax)
