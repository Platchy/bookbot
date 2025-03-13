#  Bookbot main
import sys
from stats import word_count, letter_count, sort_dictionary

def get_book_text(path):
    book = ""
    with open(path) as f:
        book = f.read()
    return book

def main():
    book_path = ""
    try:
        book_path = sys.argv[1]
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    book_text = get_book_text(book_path)
    count = word_count(book_text)
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    letter_counts = letter_count(book_text)
    sorted_list = sort_dictionary(letter_counts)
    for item in sorted_list:
        print(f"{item['character']}: {item['count']}")
    print("============= END ===============")

main()