def count_chars(s):
    res_dict = {}
    for c in s:
        if c not in res_dict:
            res_dict[c] = 1
        else:
            res_dict[c] += 1

    sorted_keys = sorted(res_dict.keys())
    sorted_dict = {k: res_dict[k] for k in sorted_keys}

    return sorted_dict


def ex2():
    s = input("Enter a string: ")
    res = count_chars(s)
    print(res)
    return res
