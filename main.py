"""Encodage simple de chaînes en tuples (caractère, count).

Fournit deux implémentations : itérative (`artcode_i`) et récursive
(`artcode_r`).
"""

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """Encodage itératif.

    Args:
        s (str): chaîne à encoder

    Returns:
        list[tuple]: liste (caractère, nombre d'occurrences)
    """

    if not s:
        return []

    result = []
    current = s[0]
    count = 1

    for ch in s[1:]:
        if ch == current:
            count += 1
        else:
            result.append((current, count))
            current = ch
            count = 1

    result.append((current, count))
    return result


def artcode_r(s):
    """Encodage récursif

    Retourne la même sortie que `artcode_i` mais calculée récursivement.
    """

    if not s:
        return []

    first_char = s[0]
    idx = 1
    while idx < len(s) and s[idx] == first_char:
        idx += 1

    return [(first_char, idx)] + artcode_r(s[idx:])

#### Fonction principale


def main():
    """Tester rapidement les fonctions."""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
