def get_text_words(text: str):
    words = text.split()
    return words

def get_chars_dict(text: str):
    characters = {}
    words = text.split()

    for w in words:
        for c in w:
            lowered = c.lower()
            if lowered not in characters:
                characters[lowered] = 1
            else:
                characters[lowered] += 1

    return characters

def print_char_dict(text_file_path: str, text_word_count: int, chars_count_dict: dict[str, int]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {text_file_path}...")

    print("----------- Word Count ----------")
    print(f"Found {text_word_count} total words")

    print("--------- Character Count -------")
    new_dict = dict(sorted(chars_count_dict.items(), key=lambda items: items[1], reverse=True))
    for key, value in new_dict.items():
        if key.isalpha():
            print(f"{key}: {value}")

    print("============= END ===============")
    return new_dict