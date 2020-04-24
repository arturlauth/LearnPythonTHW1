def scan(pos):
    """ test_directions
    scan pos

    Ex: scan north

    :return: ( direction, north)
    :rtype: tuple
    """
    result = pos.split()
    list = []
    for word in result:
        if word == 'north' or word == 'east' or word == 'south':
            pos1 = ('direction', word)
            list.append(pos1)
        else:
            pos1 = ('verb', word)
            list.append(pos1)
    return list