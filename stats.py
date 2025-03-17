def get_book_word_count(book_text:str):
    return len(book_text.split())

def get_character_count(book_text:str):
    character_counts = {}
    for character in book_text.lower():
        if character in character_counts.keys():
            character_counts[character] = character_counts[character] + 1
        else:
            character_counts[character] = 1

    return character_counts