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
