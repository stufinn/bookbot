import sys
from stats import count_words, count_characters, create_list_of_dict, sort_list_of_dicts

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    # print(book_text)  # Print the first 1000 characters of the book
    char_count_dictionary = count_characters(book_text)
    list_of_cc_dict = create_list_of_dict(char_count_dictionary)
    sorted_list = sort_list_of_dicts(list_of_cc_dict)
    # print(sorted_list)
    for item in sorted_list:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()