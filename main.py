import base64
from random import randint

import requests
from bs4 import BeautifulSoup

WORD_LIST_FILENAME = "words.txt"
SEMANTLE_BASE_URL = "https://semantle.com/?word="
ENCODING = "utf-8"


def _pick_random_word() -> str:
    with open(WORD_LIST_FILENAME) as word_list_file:
        word_list = [word.strip().lower() for word in word_list_file]
    max_range = len(word_list)
    random_idx = randint(0, max_range-1)
    random_word = word_list[random_idx]
    return random_word


def _base64_word(word: str, number_suffix: int = None) -> str:
    if not number_suffix:
        number_suffix = randint(1337, 999999)
    str_to_encode = f"{word}{number_suffix}".encode(ENCODING)
    encoded_bytes = base64.b64encode(str_to_encode)
    encoded_str = str(encoded_bytes, ENCODING)
    return encoded_str


def _get_url_for_semantle() -> str:
    new_word = _pick_random_word()
    base64_word_and_suffix = _base64_word(new_word)
    url = f"{SEMANTLE_BASE_URL}{base64_word_and_suffix}"
    return url


def _get_team_code_for_semantle(game_url: str) -> str:
    response = requests.get(f"{game_url}#")
    if not response.ok:
        raise Exception("There was a problem getting the team code from Semantle")
    html_body = response.text
    full_soup = BeautifulSoup(html_body, "lxml")
    team_code = full_soup.find(id="team")
    return team_code


def main():
    url = _get_url_for_semantle()
    # team_code = _get_team_code_for_semantle(url)
    print(f"URL:\t{url}")
    # print(f"Team Code:\t{team_code}")


if __name__ == '__main__':
    main()
