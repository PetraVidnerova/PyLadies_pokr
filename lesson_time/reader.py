def read_bible_lines(num=10):
    text = ""
    with open("bible_part.txt", "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i > num:
                return text
            text += line
    return text
