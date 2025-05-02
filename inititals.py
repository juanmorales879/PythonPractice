def abbrev_name(name):
    x = name.split()
    initials = '.'.join(i[0].upper() for i in x)
    return initials

    