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
    while True:
        min_rating = input("\nEnter the minimum IMDb rating you're okay with (0-10): ")
        try:
            rating = float(min_rating)

            if rating >= 0 and rating <= 10:
                return rating
        except ValueError:
            print("\n⚠️ Invalid input. Please enter a number, not letters or symbols.")


def gather_user_preferences(base_url: str) -> str:
    print("\n🎬 Welcome to Movie Finder!")
    print("\nI'm excited to help you discover great movies based on your preferences.")

    genre = get_genre()
    if genre != "":
        base_url += f"&genres={genre}"

    min_rating = get_min_rating()
    base_url += f"&user_rating={min_rating},"

    return base_url


def fetch_movie_titles(final_url: str) -> list:
    page = requests.get(final_url, headers=HEADERS)
    soup = BeautifulSoup(page.text, "html.parser")

    name_list = soup.find_all("h3", class_="ipc-title__text ipc-title__text--reduced")

    name_list.pop(len(name_list) - 1)

    return name_list


def main():
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
