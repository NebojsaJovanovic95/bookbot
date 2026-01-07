from stats import count_words, count_chars, sorted_dicts

def get_book_text(path: str = "")->str:
    with open(path) as f:
        file_contents: str = f.read()
    return file_contents

def main():
    book_text: str = get_book_text(
        path = "books/frankenstein.txt"
    )
    num_words:int = count_words(text = book_text)
    chars = count_chars(book_text)
    print(f"Found {num_words} total words")
    sorted_list = sorted_dicts(chars=chars)
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

if __name__ == "__main__":
    main()
