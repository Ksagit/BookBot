from stats import get_num_words, get_character_count


def get_book_text(filepath):
    with open(filepath) as f:
        file_contets = f.read()
        return file_contets


def main():
    num_words = get_num_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")
    print(get_character_count(get_book_text("books/frankenstein.txt")))


main()
