from stats import count_words, count_characters, create_list_of_dict, sort_list_of_dicts

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_text)
    print(f"Found {word_count} total words")
    # print(book_text)  # Print the first 1000 characters of the book
    char_count_dictionary = count_characters(book_text)
    list_of_cc_dict = create_list_of_dict(char_count_dictionary)
    sorted_list = sort_list_of_dicts(list_of_cc_dict)
    print(sorted_list)

main()