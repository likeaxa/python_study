def is_anagram(s, t):
    return sorted(s) == sorted(t)


def is_anagram_map(s, t):
    dic1, dic2 = {}, {}
    for item in s:
        dic1[item] = dic1.get(item, 0) + 1
    for item in t:
        dic2[item] = dic2.get(item, 0) + 1
    return dic1 == dic2


print(is_anagram('abc', "cba"))
print(is_anagram_map('abca', 'bcaa'))
print(is_anagram_map('aa', 'ab'))
