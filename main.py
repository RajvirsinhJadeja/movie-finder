from bs4 import BeautifulSoup
import requests

genreSet = {
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

base_url = "https://www.imdb.com/search/title/?title_type=feature"


def gather_info(url):
    print("🎬 Welcome to Movie Finder!")
    print(
        "\nI'm excited to help you discover some great movies to watch based on your preferences."
    )
    genre = input(
        "\nWhat genre are you in the mood for? (e.g. action, sci-fi, horror): "
    )

    if genre.lower() in ["scifi", "sci fi", "sci-fi"]:
        url += "&genres=" + "sci-fi"
    elif genre.lower() in genreSet:
        url += "&genres=" + genre.lower()

    return url


url = gather_info(base_url)

headers = {"User-Agent": "Chrome (Windows 10.0; Win64; x64)"}


page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, "html.parser")

name_cells = soup.find_all("h3", class_="ipc-title__text ipc-title__text--reduced")

for cell in name_cells:
    print(cell.text.strip())
