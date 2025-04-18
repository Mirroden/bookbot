import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    file = sys.argv[1]

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents

from stats import (count_words, count_characters, sort_dicts)


def main():
    book_text = get_book_text(file)
    word_count = count_words(book_text)
    characters = count_characters(book_text)
    sort_dict = sort_dicts(characters)
    
    print("========== BOOKBOT ==========")
    print(f"book found at {file}")
    print("-------- Word Count ---------")
    print(f"Found {word_count} total words")
    print("------ Character Count ------")
    
    for char_dict in sort_dict:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============ END ============")
    

main()
