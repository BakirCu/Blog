def string_index_of(string, sub_str, start_index):
    if len(string) < len(sub_str):
        return -1

    for i in range(start_index, len(string) - len(sub_str) + 1):
        found = True

        for j in range(0, len(sub_str)):
            if string[i + j] != sub_str[j]:
                found = False
                break

        if found:
            return i

    return -1


index = string_index_of('abcdbc', 'bc', 2)
print(index)
