import sys
from stats import get_chars_dict, get_text_words, print_char_dict

def get_book_text(book_path: str):
    with open(book_path) as file:
        text = file.read()
        return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_book = sys.argv[1]
    
    text = get_book_text(path_to_book)
    words = get_text_words(text)
    words_count = len(words)
    chars_count_dict = get_chars_dict(text)

    print_char_dict(path_to_book, words_count, chars_count_dict)
    
main()
