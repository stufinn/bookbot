def count_words(book_string):
    word_list = book_string.split()
    num_of_words = len(word_list)
    return num_of_words

def count_characters(string):
    character_count = {}
    for char in string:
        lower_char = char.lower()
        if lower_char not in character_count:
            character_count[lower_char] = 1
        else:
            character_count[lower_char] = character_count[lower_char] + 1
    return character_count

def create_list_of_dict(dict):
    new_list=[]
     # Iterate over the items in each dictionary   
    for key in dict:
        new_list.append({"char": key, "num": dict[key] })
    return new_list

def sort_on(items):
    return items["num"]

# Given a list of dictionaries, sort them
def sort_list_of_dicts(list_of_dicts):
    # print(list_of_dicts)
    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts






# def sort_on(items):
#     return items[""]

# 1. Create a list of dictionaries - one for each character
# e.g. [ { char: a, num: 456 }, { char: b, num: 34 } ]