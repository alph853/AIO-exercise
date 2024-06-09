import re


def check_input_sliding_window(input_list: str, k: str, num_list: list):
    if input_list[0] == '[' and input_list[-1] == ']':
        input_list = input_list[1:-1]

    try:
        num_list[:] = list(
            map(int, re.sub(r'[^\d-]', ' ', input_list).split()))
    except:
        print("Invalid input. Please enter a list of integers separated by whitespace.")
        return False

    try:
        k = int(k)
    except:
        print("Invalid input. k must be a positive integer.")
        return False

    if k <= 0:
        print("Invalid input. k must be greater than 0.")
        return False

    if len(num_list) < k:
        print("Invalid input. The list must contain at least k elements.")
        return False

    print(num_list)
    return True


def sliding_window(num_list, k):
    res_list = [max(num_list[:k])]
    for i in range(1, len(num_list)-k+1):
        if num_list[i+k-1] >= res_list[-1]:
            res_list.append(num_list[i+k-1])
        else:
            res_list.append(max(num_list[i:i+k]))

    return res_list


def ex1():
    sample_num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    sample_k = 3
    sample_res = [5, 5, 5, 5, 10, 12, 33, 33]
    assert sliding_window(sample_num_list, sample_k) == sample_res

    input_list = input("Enter a list of integers (e.g '1 2 3 4'): ")
    k = input("Enter a positive integer k: ")

    num_list = []
    if check_input_sliding_window(input_list, k, num_list):
        res = sliding_window(num_list, int(k))
        print(res)
        return res
