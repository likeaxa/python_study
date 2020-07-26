def get_next(s):
    lenth = len(s)
    next = [-1] * lenth
    next[0] = -1
    index = 1
    while index < lenth:
        t = next[index - 1]
        while s[t + 1] != s[index] and t > 0:
            t = next[t]
        if s[t + 1] == s[index]:
            next[index] = t + 1
        else:
            next[index] = -1
        index = index + 1
    return next


def kmp(s, p):
    next = get_next(p)
    s_lenth = len(s)
    p_lenth = len(p)
    i, j = 0, 0
    while i < s_lenth:
        while j < p_lenth:
            if s[i] == p[j]:
                i = i + 1
                j = j + 1
                if j == p_lenth:
                    return p
            else:
                i = i + 1
                j = next[j] + 1
    return None


print(kmp('ABCADABCAC', 'ABCAE'))
