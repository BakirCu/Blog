# pravi string koji je posle kljuc ili vrednost u zavisnosi od break_ch


def create_key_value(uri_str, index, break_ch):
    key = []
    while index < len(uri_str) and uri_str[index] != break_ch:
        key.append(uri_str[index])
        index += 1
    return ''.join(key), index

# pravi i varca recnik


def create_dict(uri_str, index):
    args = {}
    while index < len(uri_str):
        key, index = create_key_value(uri_str, index, '=')
        value, index = create_key_value(uri_str, index + 1, '&')
        args[key] = value
            args[key].append(value)
        index += 1
    return args

# pravi path i poziva funkciju za pravljenje recnika -> i vraca path i recnik


def uri(uri_str):
    path = []
    index = 0
    while index < len(uri_str) and uri_str[index] != '/':
        index += 1
    while index < len(uri_str) and uri_str[index] != '?':
        path.append(uri_str[index])
        index += 1
    args = create_dict(uri_str, index + 1)
    return ''.join(path), args


def main():
    uri_str = 'cm/path?k=1&l=2'
    print(uri(uri_str))
    # ('/path', {'k': '1', 'l': '2'})

    uri_str = 'cm/path?fdk=121&l343=223&fsdd=324&fdk=4'
    print(uri(uri_str))
    # ('/path', {'fdk': '121', 'l343': '223', 'fsdd': '324'})


main()
