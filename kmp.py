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


def match(pattern, text):
    """

    :param pattern:
    :param text:
    :return:  list of indices in text where pattern matches; may be empty.
    """
    overlaps = overlap(pattern)
    result = []

    len_pattern = len(pattern)
    len_text = len(text)
    k_bound = len_text - len_pattern + 1

    k = 0
    while k < k_bound:
        x = 0
        for p in pattern:
            if p != text[k + x]:
                break
            x += 1

        if x == len_pattern:
            # found a match
            result.append(k)
            k += x
            continue

        if x == 0:
            k += 1
            continue

        bump = x - overlaps[x - 1]
        if bump < 1:
            raise Exception("bump = %s, k = %s, x = %s" % (bump, k, s))
        k += bump

    return result
