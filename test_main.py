from main import get_genre
from main import get_min_rating
from main import get_int
from main import gather_minmax_dates
from main import gather_minmax_reviews
from main import gather_user_preferences
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


@pytest.mark.parametrize(
    "input, min_val, max_val, expected",
    [
        ("5", None, None, 5),
        ("", None, None, ""),
        ("3", 4, 10, 4),  # below min -> clamp to min
        ("15", 1, 10, 10),  # above max -> clamp to max
    ],
)
def test_get_int_valid(mocker, input, min_val, max_val, expected):
    mock_input = mocker.patch("builtins.input")
    mock_input.return_value = input
    assert get_int("prompt: ", min_val, max_val) == expected


def test_get_int_invalid(mocker):
    mock_input = mocker.patch("builtins.input")
    mock_input.side_effect = ["notnumber", "5"]
    assert get_int("prompt: ") == 5


def test_get_genre_valid(mocker):
    mock_input = mocker.patch("builtins.input")
    mock_input.return_value = "action"
    assert get_genre() == "action"


def test_get_genre_scifi_variants(mocker):
    mock_input = mocker.patch("builtins.input")
    mock_input.return_value = "sci fi"
    assert get_genre() == "sci-fi"


def test_get_genre_invalid(mocker):
    mock_input = mocker.patch("builtins.input")
    mock_input.return_value = "unknown"
    assert get_genre() == ""


def test_gather_minmax_dates_valid(mocker):
    mocker.patch("builtins.input", side_effect=["2000", "2020"])
    assert gather_minmax_dates() == (2000, 2020)


def test_gather_minmax_dates_blank(mocker):
    mocker.patch("builtins.input", side_effect=["", ""])
    assert gather_minmax_dates() == ("", "")


def test_gather_minmax_reviews_valid(mocker):
    mocker.patch("builtins.input", side_effect=["100", "1000"])
    assert gather_minmax_reviews() == (100, 1000)


def test_gather_minmax_reviews_blank(mocker):
    mocker.patch("builtins.input", side_effect=["", ""])
    assert gather_minmax_reviews() == ("", "")


def test_gather_user_preferences(mocker):
    mocker.patch(
        "builtins.input",
        side_effect=[
            "action",  # genre
            "7",  # rating
            "2000",  # min_date
            "2020",  # max_date
            "100",  # min_reviews
            "1000",  # max_reviews
        ],
    )

    result = gather_user_preferences("base_url")
    assert "genres=action" in result
    assert "user_rating=7.0" in result
    assert "release_date=2000,2020" in result
    assert "num_votes=100,1000" in result
