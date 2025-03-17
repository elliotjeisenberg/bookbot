from stats import get_book_word_count, get_character_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    book_text = get_book_text('books/frankenstein.txt')
    word_count = get_book_word_count(book_text)
    character_counts = get_character_count(book_text)
    print(word_count,'words found in the document')
    print(character_counts)



main()