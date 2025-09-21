import pytest
from .vowels import count_vowels

#  функция правильно считает гласные в строке, содержащей только гласные англ
def test_only_vowels_english():
    assert count_vowels("aeiouAEIOU") == 10  # все символы — гласные

#  функция правильно считает гласные в строке, содержащей только гласные русский
def test_only_vowels_russian():
    assert count_vowels("аеёиоуыэюяАЕЁИОУЫЭЮЯ") == len("аеёиоуыэюяАЕЁИОУЫЭЮЯ")

#  функция возвращает 0 для строки, не содержащей гласных
def test_no_vowels():
    assert count_vowels("bcdfg BCDFG") == 0  # нет гласных

# функция правильно считает гласные в смешанных строках (включая прописные и строчные буквы).
def test_mixed_string_english():
    assert count_vowels("Hello World") == 3  # e, o, o

def test_mixed_string_russian():
    assert count_vowels("Привет Мир") == 3  # и, е, и


def test_empty_string():
    assert count_vowels("") == 0


######  Parametrized Decorator ########

@pytest.mark.parametrize(
    "input_str, expected",
    [
        # Только гласные (английские)
        ("aeiouAEIOU", 10),
        # Только гласные (русские)
        ("аеёиоуыэюяАЕЁИОУЫЭЮЯ", len("аеёиоуыэюяАЕЁИОУЫЭЮЯ")),
        # Без гласных
        ("bcdfg BCDFG", 0),
        # Смешанная строка (английский)
        ("Hello World", 3),  # e, o, o
        # Смешанная строка (русский)
        ("Привет Мир", 3),   # и, е, и
        # Пустая строка
        ("", 0),
    ]
)
def test_count_vowels(input_str, expected):
    assert count_vowels(input_str) == expected