# trazi kljuc u malom temlejtu
def create_str(template, index):
    key = []
    while index < len(template) and template[index].isspace():
        index += 1
    while index < len(template) and template[index].isalpha():
        key.append(template[index])
        index += 1
    while index < len(template) and template[index].isspace():
        index += 1
    return key, index


def read_key(template, index):
    key, index = create_str(template, index)
    if template[index] != '}' or index + 1 >= len(template) or template[index + 1] != '}':
        raise ValueError("Did not find closing braces")
    return ''.join(key), index + 2

# renderuje mali tempplate


def render_small_template(template, data):
    final_sml_tep_list = []
    index = 0
    while index < len(template):
        ch = template[index]
        if ch == '{' and index + 1 < len(template) and template[index+1] == '{':
            key, index = read_key(template, index + 2)
            if key not in data:
                raise ValueError('The specified key in list does not exist')
            else:
                value = data[key]
                for ch in value:
                    final_sml_tep_list.append(ch)
                continue
        else:
            final_sml_tep_list.append(ch)
            index += 1
    return ''.join(final_sml_tep_list)

# vraca mali template  od zagrada gde je for do end ako nadje end u poslednjoj zagradi i index pre zagrada gde je end.
# ako nema end varca prazan string i 0 , da bi u render() mogao da proverim da li je dobro petlja zatvorena.


def create_small_template(template, index):
    sml_template_list = []
    while index < len(template):
        ch = template[index]
        if ch == '{' and index + 1 < len(template) and template[index+1] == '{':
            key, index = read_key(template, index + 2)
            if key != 'end':
                sml_template_list.append("{{")
                for ch in key:
                    sml_template_list.append(ch)
                sml_template_list.append('}}')
                continue

            else:
                return ''.join(sml_template_list), index + 2
        else:
            sml_template_list.append(ch)
            index += 1
    return '', 0

# proverava da li se nalazi for i kljuc u prvim zagradama i vraca kljuc iz data i vraca index + 2


def find_for_loop(template, index):
    data_key_list, index = create_str(template, index)
    if template[index] != '}' or index + 1 < len(template[index + 1]) or template[index + 1] != '}':
        raise ValueError(
            "Did not find closing braces, or did not use alpha in brackets ")
    return ''.join(data_key_list), index + 2

# vraca prvi string posle zagrada, da bi u render proverio da li je on kljuc ili for, i index`


def make_choice(template, index):
    key, index = create_str(template, index)
    return ''.join(key), index


def render(template, data):
    final_list = []
    index = 0
    while index < len(template):
        ch = template[index]

        if ch == '{' and index + 1 < len(template) and template[index + 1] == "{":
            first_key, index = make_choice(template, index + 2)
            if first_key == 'for':
                key_in_data, index = find_for_loop(template, index)
                if key_in_data not in data:
                    raise ValueError(
                        'The specified key in dict does not exist')
                sml_template, index = create_small_template(template, index)
                if not sml_template:
                    raise ValueError('Did not close loop')
                values = data[key_in_data]
                final_list.append('\n')
                for value in values:
                    sml_template_replaced = render_small_template(
                        sml_template, value)

                    for ch in sml_template_replaced:
                        final_list.append(ch)
                    final_list.append('\n')
                    continue

            elif first_key in data:
                if template[index] != '}' or index + 1 >= len(template) or template[index + 1] != '}':
                    raise ValueError("Did not find closing braces")
                index += 2
                value = data[first_key]
                for ch in value:
                    final_list.append(ch)
                continue
            else:
                raise ValueError("Did not find key or 'for'")
        else:
            final_list.append(ch)
            index += 1
    return ''.join(final_list)
