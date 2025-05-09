import sys
from stats import get_num_words, get_character_count, get_sorted_char_list


def get_book_text(filepath):
    with open(filepath) as f:
        file_contets = f.read()
        return file_contets


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")

    book_text = get_book_text(path_to_book)

    num_words = get_num_words(book_text)     
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    char_count = get_character_count(book_text)
    sorted_list = get_sorted_char_list(char_count)
    print("--------- Character Count -------")
    for char_dict in sorted_list:
        char = char_dict["char"]
        print(f"{char}: {char_dict['num']}")
    
    print("============= END ===============")

main()
