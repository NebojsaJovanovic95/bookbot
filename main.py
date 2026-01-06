def get_book_text(path: str = "")->str:
    with open(path) as f:
        file_contents: str = f.read()
    return file_contents

def main():
    print(
        get_book_text(
            path = "books/frankenstein.txt"
        )
    )

if __name__ == "__main__":
    main()
