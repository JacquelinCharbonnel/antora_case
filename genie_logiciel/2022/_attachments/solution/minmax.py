#!/bin/env python3

from monmodule import load

"""
    Soit L le type liste dont les éléments sont soit tous de type int, soit tous de type L.
    Par exemple, l = [ [1,2], [ [2,3,4], [5,4,3,2], [[3,1],[2]]], [0,9] ] est de type L.  

    Ce programme est appelé avec une liste de type L sur la ligne de commande,
    et sort le min des max de ses sous-listes.  

    Avec la liste l ci-dessus, la liste des max est [2, 4, 5, 3, 2, 9] donc le programme sort 2.

    La liste doit être fournie sous la forme : [ [ 1 2 ] [ [ 2 3 4 ] [ 5 4 3 2 ] [ [ 3 1 ] [ 2 ] ] ] [ 0 9 ] ]
"""

def minmax(l):
    """
    Cette fonction récursive retourne le minmax de la liste passée en argument.
    """

    def maxi(l):
        if type(l[0])==int:
            result.append(max(l))
        else:
            for i in l:
                maxi(i)


    result = []
    maxi(l)
    return min(result)

if __name__=="__main__":
    # programme principal
    l = load()                      # récupération de la liste
    print(f"** {l=} **")
    for i in l:
        print(f"{i=}", end=" ")
        print(f"{minmax(i)=}")
