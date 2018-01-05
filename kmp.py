def overlap(pattern):
    """

    :param pattern:
    :return:  an array giving the max overlaps for each prefix.  len(array) == len(pattern)
    """

    if not pattern:
        raise Exception("fuck you")

    m = len(pattern)

    f = [0] * m

    k = 1
    x = 0
    while k < m:

        if pattern[k] == pattern[x]:
            f[k] = f[k - 1] + 1
            x += 1
            k += 1
        else:
            if x > 0:
                i = x - 1
                x = f[i]

            if x == 0:
                f[k] = 0
                k += 1

    return f
