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

