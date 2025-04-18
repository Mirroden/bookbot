def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lowercase = text.lower()
    characters = (*lowercase,)
    count_dict = {}
    for character in characters:
        if character in count_dict:
            count_dict[character] += 1
        else:
            count_dict[character] = 1
    return count_dict

def sort_dicts(char_dict):
    char_list = []
    for char,count in char_dict.items():
        char_list.append({"char":char, "count":count})
    def sort_on(dict):
        return dict["count"]
    char_list.sort(reverse=True, key=sort_on)
    return char_list

