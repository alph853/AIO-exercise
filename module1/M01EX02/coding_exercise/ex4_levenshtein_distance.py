import numpy as np


def levenshtein_distance(source: str, target: str):
    """
    Calculate the Levenshtein distance and give sequence of edits between two strings.
    Follow notations given in the exercise specs.

    """

    M, N = len(source) + 1, len(target) + 1
    D = np.zeros(shape=(M, N), dtype=[('dist', int), ('parent', (int, 2))])

    # init first row and column for 'dist' and 'parent'
    for i in range(M):
        D[i, 0] = i, (i-1, 0)
    for i in range(N):
        D[0, i] = i, (0, i-1)

    for i in range(1, M):
        for j in range(1, N):
            # [0]del, [1]ins, [2]sub
            cost = (1, 1, 0 if (source[i-1] == target[j-1]) else 1)
            parent_index = [(i-1, j), (i, j-1), (i-1, j-1)]

            list_of_changes = [
                (D[pIdx]['dist'] + c, pIdx) for pIdx, c in zip(parent_index, cost)
            ]

            D[i, j] = min(list_of_changes, key=lambda x: x[0])

    edits = []
    i, j = M-1, N-1

    while (i, j) != (0, 0):
        p = D[i, j]['parent'][0], D[i, j]['parent'][1]
        if p == (i-1, j):
            edits.append(f"delete '{source[i-1]}' at index {i-1}")
        elif p == (i, j-1):
            edits.append(f"insert '{target[j-1]}' at index {j-1}")
        elif p == (i-1, j-1) and source[i-1] != target[j-1]:
            edits.append(
                f"substitute '{source[i-1]}' with '{target[j-1]}' at index {i-1}")
        i, j = p

    edits.reverse()
    return D[-1, -1]['dist'], edits


def ex4():
    source = input("Input source string: ")
    target = input("Input target string: ")
    distance, edits = levenshtein_distance(source, target)

    print(
        f"\n_Levenshtein distance from '{source}' to '{target}' is \n\t{distance}")
    print(f"_Sequence of edits: ")
    for i in range(len(edits)):
        print(f"{i+1}: {edits[i]}")
