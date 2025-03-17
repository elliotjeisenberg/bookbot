from stats import get_book_word_count, get_character_count, sort_characters_in_dict_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    word_count = get_book_word_count(book_text)
    character_counts = get_character_count(book_text)
    sorted_character_counts = sort_characters_in_dict_list(character_counts)
    print('== == == == == == BOOKBOT == == == == == ==')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print('Found',word_count,'total words')
    print('--------- Character Count -------')
    for character_count in sorted_character_counts:
        print(character_count['char'] + ': ' + str(character_count['count']))



main()