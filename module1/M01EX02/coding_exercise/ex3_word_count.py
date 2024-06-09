def word_count(file_path: str):
    res_dict = {}
    with open(file_path, 'r') as f:
        for line in f:
            for word in line.split():
                word = word.lower()
                if word in res_dict:
                    res_dict[word] += 1
                else:
                    res_dict[word] = 1

    sorted_dict = sorted(res_dict.keys())
    sorted_dict = {k: res_dict[k] for k in sorted_dict}
    return sorted_dict


def ex3():
    file_path = 'P1_data.txt'
    res = word_count(file_path)
    print(res)
    return res
