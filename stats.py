def count_chars(text:str = "") -> dict:
    chars = {}
    for c in text.lower():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def count_words(text:str = "") -> int:
    return len(
        text.split()
    )

def sorted_dicts(chars: dict = {}) -> list[dict]:
    char_counts = sorted(
        [
            {
                "char": key,
                "num": chars[key]
            } for key in chars
        ],
        reverse=True,
        key=lambda item: item["num"]
    )
    return char_counts
