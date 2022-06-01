import base64
from random import randint

WORD_LIST_FILENAME = "words.txt"
SEMANTLE_BASE_URL = "https://semantle.com/nearby_1k/"


def _pick_random_word() -> str:
    with open(WORD_LIST_FILENAME) as word_list_file:
        word_list = [word.strip() for word in word_list_file]
    max_range = len(word_list)
    random_idx = randint(0, max_range-1)
    random_word = word_list[random_idx]
    return random_word


def _base64_word(word: str, number_suffix: int = None) -> str:
    if not number_suffix:
        number_suffix = randint(1337, 999999)
    str_to_encode = f"{word}{number_suffix}".encode("utf-8")
    encoded_bytes = base64.b64encode(str_to_encode)
    encoded_str = str(encoded_bytes, "utf-8")
    return encoded_str


def _get_url_for_semantle(base64_word_and_suffix: str) -> str:
    url = f"https://semantle.com/?word={base64_word_and_suffix}"
    return url


def main():
    new_word = _pick_random_word()
    base_64_word_and_suffix = _base64_word(new_word)
    url = _get_url_for_semantle(base_64_word_and_suffix)
    print(f"URL: {url}")


if __name__ == '__main__':
    main()
