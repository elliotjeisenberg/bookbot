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


def sort_characters_in_dict_list(character_counts:dict):
    sorted_chars = []
    for key, value in character_counts.items():
        if key.isalpha():
            sorted_chars.append({"char":key,"count":value})
    x = sorted(sorted_chars, key=lambda x: x["count"], reverse=True)
    return x
