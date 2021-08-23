import string

lst_check = [chr(i) for i in range(ord('a'), ord('z') + 1)]


def is_pangram(s):
    s = s.lower()
    lst = list()
    for i in s:
        if i in lst_check and i not in lst:
            lst.append(i)

    return len(lst) == len(lst_check)