from stats import get_num_words
from stats import get_num_characters
from stats import sort_num_characters



def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)

    char_list = []
    for char, count in num_characters.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})
    char_list.sort(reverse=True, key=sort_num_characters)

    print_report(book_path, num_words, char_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(file_path, word_count, chars_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    # Counter loop
    for char_dict in chars_list:
        char = char_dict["char"]
        count = char_dict["count"]
        print(f"{char}: {count}")
    print("============= END ===============")



main()