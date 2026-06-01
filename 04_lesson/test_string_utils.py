import pytest
from string_utils import StringUtils


# Функция №1

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("skyeng", "Skyeng"),
    ("java", "Java"),
    ("windows", "Windows")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("", ""),
    (" ", " "),
    ("12345", "12345"),
    ])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Функция №2


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    ("   ", ""),
    ("  python", "python"),
    ("   skyeng", "skyeng"),
    ("    java", "java"),
    ("     windows", "windows")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("skypro", "skypro"),
    ("04 апреля 2023", "04 апреля 2023"),
    ("", ""),
    ("SKYENG", "SKYENG"),
    ("12345", "12345")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# Функция №3

strringUtils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("str1, str2, result", [
    ("Skypro", "o", True),
    ("Skypro", "ro", True),
    ("Skypro", "pro", True),
    ("Skypro", "S", True),
    ("Skypro", "r", True),
    ("Skypro", "k", True)])
def test_strib_positive(str1, str2, result):
    res = strringUtils.contains(str1, str2)
    assert res == result


@pytest.mark.negative
@pytest.mark.parametrize("str1, str2, result", [
    ("Skypro", "a", False),
    ("Skypro", "ra", False),
    ("Skypro", "Str", False),
    ("Skypro", "D", False),
    ("Skypro", "T", False),
    ("Skypro", "z", False),
])
def test_strib_negative(str1, str2, result):
    res = strringUtils.contains(str1, str2)
    assert res == result

# Функция №4


strringUtils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_symbol, expected_out", [
    ("Text", "T", "ext"),
    ("Text", "e", "Txt"),
    ("12345", "2", "1345"),
    ("12345", "45", "123"),
    ("12345", "123", "45"),
    ("12345", "12", "345")
])
def test_delete_symbol_positive(input_str, input_symbol, expected_out):
    assert strringUtils.delete_symbol(input_str, input_symbol) == expected_out


@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol, expected_out", [
    ("Text", "a", "Text"),
    ("Text", "S", "Text"),
    ("12345", "9", "12345"),
    ("test string", "y",
     "test string"),
    ("", "b", ""),
    ("", "", "")
])
def test_delete_symbol_negative(input_str, input_symbol, expected_out):
    assert strringUtils.delete_symbol(input_str, input_symbol) == expected_out
