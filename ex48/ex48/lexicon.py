def scan(pos):
    """ test_directions
    scan pos

    Ex: scan north

    :return: ( direction, north)
    :rtype: tuple
    """
    result = pos.split()
    list = []
    i = 0
    for word in result:
        pos1 = ('direction', word)
        list.append(pos1)
        i += 1
    return list