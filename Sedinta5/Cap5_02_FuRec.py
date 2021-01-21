def adunaRecursiv(nrMin, nrMax):
    """Aduna numerele cuprinse intre minim si maxim"""

    if nrMin > nrMax:
        return 0

    else:
        return nrMin + adunaRecursiv(nrMin + 1, nrMax)
