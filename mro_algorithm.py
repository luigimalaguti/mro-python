DEBUG = False


def get_char(index, LL):
    single = LL[index]
    char = single[0]
    return char


def get_tails(index, LL):
    tails = []
    other = [l for l in LL[ : index]]
    other += [l for l in LL[index + 1 : ]]
    for tail in other:
        tails += tail[1 : ]
    return tails


def remove_char(char, LL):
    new_LL = []
    for head in LL:
        if head != []:
            if head[0] == char:
                new_LL.append(head[1 : ])
            else:
                new_LL.append(head)
    new_LL = [head for head in new_LL if len(head) != 0]
    return new_LL


def mro_algorithm(root, LL):
    M = [root]

    while True:
        index = 0
        skip = False
        if len(LL) == 0:
            break
        if DEBUG:
            print("LL:\t", LL)
            print("Single:\t", LL[index])
            print("Other:\t", LL[ : index] + LL[index + 1 : ])
            print("Tails\t", get_tails(index, LL))
            print("Char:\t", get_char(index, LL))
            print("Is in:\t", get_char(index, LL) in get_tails(index, LL))
            print("Index:\t", index)
        while get_char(index, LL) in get_tails(index, LL):
            if index != len(LL)  - 1:
                index += 1
            else:
                return None
            if DEBUG:
                print("LL:\t", LL)
                print("Single:\t", LL[index])
                print("Other:\t", LL[ : index] + LL[index + 1 : ])
                print("Tails\t", get_tails(index, LL))
                print("Char:\t", get_char(index, LL))
                print("Is in:\t", get_char(index, LL) in get_tails(index, LL))
                print("Index:\t", index)
        if index == len(LL):
            break
        else:
            M.append(get_char(index, LL))
            LL = remove_char(get_char(index, LL), LL)
            if DEBUG:
                print("M:\t", M)
                print("LL:\t", LL)

    return M


def main():
    # LL = List of linearizations
    # M = final merge list
    # M = merge(LL) = merge(L(1), ..., L(j))

    # Expect: ABCDEFO
    LL = [["B", "D", "E", "O"], ["C", "D", "F", "O"], ["B", "C"]]
    M = mro_algorithm("A", LL)
    print("Merge list:", M)

    # Expect: ABECDFGHIJO
    LL = [["B", "C", "D", "O"], ["E", "C", "F", "G", "O"], ["H", "I", "J", "O"], ["B", "E", "H"]]
    M = mro_algorithm("A", LL)
    print("Merge list:", M)

    # Expect: None
    LL = [["A", "D", "E", "O"], ["B", "E", "D", "O"], ["A", "B"]]
    M = mro_algorithm("C", LL)
    print("Merge list:", M)


if __name__ == "__main__":
    main()