def get_num_words(text):
    words = text.split()
    return len(words)


def get_character_count(text):
    character_dict = {}
    for character in text:
        character = character.lower()
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict


def sort_on(dict):
     return dict["num"]


def get_sorted_char_list(dict):
    list = []
    for char, count in dict.items():
            item_dict = { "char": char, "num": count}
            if char.isalpha():
                list.append(item_dict)
    list.sort(reverse=True, key=sort_on)
    return list
