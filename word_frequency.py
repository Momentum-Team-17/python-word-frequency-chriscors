import re
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]
PUNCTUATION = [",", "?", "!", ".", "'", '"']


def read_file(file):
    """Uses open to read a file

    Args:
        file (file ): A file to be read
    """
    with open(file) as opened_file:
        return opened_file.read()


def remove_punctuation(s: str) -> str:
    for punc in PUNCTUATION:
        s = s.replace(punc, "")
    return s


def remove_stop_words(s: str) -> str:
    for word in STOP_WORDS:
        if word in s:
            s = s.replace(f'/b{word}/b', "")
    return s

# def remove_stop_words(s):
#     list = s.split()
#     return_list = []
#     for word in list:
#         if word not in STOP_WORDS:
#             return_list.append(word)
#     return " ".join(return_list)


def track_counts(s: str) -> dict:
    """Unumerates counts of words in string

    Args:
        s (string): String to be processed
    """
    counts = {}
    for word in s:
        if not counts.get(word):
            counts[word] = "*"
        else:
            counts[word] += "*"
    return counts


def add_spaces(counts: dict) -> dict:
    pass


def print_counts(counts: dict) -> None:
    breakpoint
    for word, count in counts.items():
        print(f'{word} | {count}')

    pass


def print_word_freq(file):
    """Performs word frequency operations

    Args:
        file (string): A file to be read
    """
    file_read = read_file(file)

    stripped_file = remove_punctuation(file_read).lower()

    cleaned_file = remove_stop_words(stripped_file)

    counts = track_counts(cleaned_file.split())

    counts = dict(
        sorted(counts.items(), key=lambda item: item[1], reverse=True))

    counts = add_spaces(counts)

    counts = print_counts(counts)

    pass


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
