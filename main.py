from bs4 import BeautifulSoup
import requests

GENRES = {
    "action",
    "adventure",
    "animation",
    "biography",
    "comedy",
    "crime",
    "documentary",
    "drama",
    "family",
    "fantasy",
    "history",
    "horror",
    "music",
    "musical",
    "mystery",
    "romance",
    "sci-fi",
    "scifi",
    "sport",
    "thriller",
    "war",
    "western",
}

BASE_URL = "https://www.imdb.com/search/title/?title_type=feature"
HEADERS = {"User-Agent": "Chrome (Windows 10.0; Win64; x64)"}


def get_genre() -> str:
    """Function finds genre through user input

    Returns:
        str: returns genre
    """

    genre = input(
        "\nWhat genre are you in the mood for? (e.g. action, sci-fi, horror)\n"
        "If genre doesn't matter to you, simply press Enter to skip: "
    ).lower()

    if genre in ["scifi", "sci fi", "sci-fi"]:
        return "sci-fi"
    elif genre in GENRES:
        return genre

    return ""


def get_min_rating() -> float:
    """Prompt the user for the minimum IMDb rating they are willing to accept.

    Returns:
        float: A float value representing the minimum rating (0-10).
    """

    while True:
        min_rating = (
            input("\nEnter the minimum IMDb rating you're okay with (0-10): ")
            .strip()
            .replace(" ", "")
        )
        try:
            rating = float(min_rating)

            if rating >= 0 and rating <= 10:
                return rating
        except ValueError:
            print("\n⚠️ Invalid input. Please enter a number, not letters or symbols.")


def get_int(
    prompt: str,
    min_value: int = None,  # type: ignore
    max_value: int = None,  # type: ignore
) -> int | str:
    """Prompt the user for an integer input with optional minimum and maximum limits.

    Args:
        prompt (str): The message to display to the user.
        min_value (int, optional): Minimum allowed value. Defaults to None.
        max_value (int, optional): Maximum allowed value. Defaults to None.

    Returns:
        int | str: The integer entered by the user, or an empty string if input is blank.
    """

    while True:
        value = input(prompt)
        if not value:
            return ""
        try:
            num = int(value)
            if min_value is not None and num < min_value:
                return min_value
            if max_value is not None and num > max_value:
                return max_value
            return num
        except ValueError:
            print("⚠️ Invalid input. Please enter a number, not letters or symbols.")


def gather_minmax_dates() -> tuple:
    """Prompt the user for the earliest and latest release years for movies.

    Returns:
        tuple: A tuple containing the minimum and maximum release years (int or empty string).
    """

    min_date = get_int(
        "\nEnter the earliest release year (Leave blank for no limit): ",
        min_value=1700,
        max_value=2025,
    )

    while True:
        max_date = get_int(
            "Enter the latest release year (Leave blank for no limit): ", max_value=2075
        )
        if min_date != "" and max_date != "" and min_date > max_date:  # type: ignore
            print("\nLatest release year must be more than earliest release year.")
        else:
            break

    return min_date, max_date


def gather_minmax_reviews() -> tuple:
    """Prompt the user for the minimum and maximum number of reviews a movie must have.

    Returns:
        tuple: A tuple containing the minimum and maximum review counts (int or empty string).
    """

    min_review_count = get_int(
        "\nEnter the minimum number of reviews (0-5M) (Leave blank for no limit): ",
        min_value=0,
        max_value=1000000,
    )

    while True:
        max_review_count = get_int(
            "\nEnter the maximum number of reviews (0-5M) (Leave blank for no limit): ",
            max_value=4000000,
        )
        if min_review_count != "" and max_review_count != "" and min_review_count > max_review_count:  # type: ignore
            print(
                "Maximum review count must be more than the minimum number of reviews."
            )
        else:
            break

    return min_review_count, max_review_count


def gather_user_preferences(base_url: str) -> str:
    """Collect all user preferences and build the final IMDb search URL.

    Args:
        base_url (str): The starting IMDb search URL.

    Returns:
        str: The fully constructed search URL with all filters applied.
    """

    print("\n🎬 Welcome to Movie Finder!")
    print("\nI'm excited to help you discover great movies based on your preferences.")

    genre = get_genre()
    if genre != "":
        base_url += f"&genres={genre}"

    min_rating = get_min_rating()
    base_url += f"&user_rating={min_rating},"

    min_date, max_date = gather_minmax_dates()
    base_url += f"&release_date={min_date},{max_date}"

    min_reviews, max_reviews = gather_minmax_reviews()
    base_url += f"&num_votes={min_reviews},{max_reviews}"

    return base_url


def fetch_movie_titles(final_url: str) -> list:
    """Fetch and parse movie titles from the IMDb search results page.

    Args:
        final_url (str): The complete IMDb search URL with filters.

    Returns:
        list: A list of BeautifulSoup elements containing movie titles.
    """

    page = requests.get(final_url, headers=HEADERS)
    soup = BeautifulSoup(page.text, "html.parser")

    name_list = soup.find_all("h3", class_="ipc-title__text ipc-title__text--reduced")

    name_list.pop(len(name_list) - 1)

    return name_list


def main():
    """Main entry point of the Movie Finder program.
    Collects user preferences, fetches results from IMDb, and displays movie titles.
    """

    final_url = gather_user_preferences(BASE_URL)
    print("\n📡 Fetching results...\n")
    movie_titles = fetch_movie_titles(final_url)

    if not movie_titles:
        print("❌ No movies found. Try adjusting your filters.")
        return

    print("🎥 Here are some movies you might enjoy:\n")
    for title in movie_titles:
        print(title.text.strip())


if __name__ == "__main__":
    main()
