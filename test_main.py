from main import get_min_rating
import pytest


@pytest.mark.parametrize(
    "input, expected",
    [
        ("7", 7),
        ("7.5", 7.5),
        ("0", 0),
        ("10", 10),
        (" 8 . 5", 8.5),
    ],
)
def test_get_min_rating_valid(mocker, input, expected):
    mock_input = mocker.patch("builtins.input")

    mock_input.return_value = input
    assert get_min_rating() == expected


def test_get_min_rating_not_valid(mocker):
    mock_input = mocker.patch("builtins.input")

    mock_input.side_effect = [" ", "1"]
    assert get_min_rating() == 1

    mock_input.side_effect = ["letters", "2"]
    assert get_min_rating() == 2

    mock_input.side_effect = ["1 letter", "3"]
    assert get_min_rating() == 3

    mock_input.side_effect = ["11", "4"]
    assert get_min_rating() == 4
