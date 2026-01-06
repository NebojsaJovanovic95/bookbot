def get_book_text(path: str = "")->str:
    with open(path) as f:
        file_contents: str = f.read()
    return file_contents

def count_words(text:str = "") -> int:
    return len(
        text.split()
    )

def main():
    book_text: str = get_book_text(
        path = "books/frankenstein.txt"
    )
    num_words:int = count_words(text = book_text)
    print(f"Found {num_words} total words")

if __name__ == "__main__":
    main()
