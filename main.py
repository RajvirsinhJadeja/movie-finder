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

    while True:
        score_input = input("\nEnter the minimum IMDb rating you're okay with (0-10): ")

        try:
            score = float(score_input)
            if 0 <= score <= 10:
                break
            else:
                print("⚠️ Please enter a number between 0 and 10.")
        except ValueError:
            print("⚠️ Invalid input. Please enter a number, not letters or symbols.")

    url += "&user_rating=" + score_input + ","

    print(
        "\nIf you don't want to set a minimum or maximum release year, just press Enter to skip it."
    )

    min_date_input = input("\nEnter the earliest release year: ")
    if not min_date_input:
        min_date = ""
    else:
        while True:
            try:
                min_date = int(min_date_input)
                if min_date < 1700:
                    min_date = 1700
                    break
                elif min_date > 1700 and min_date <= 2025:
                    break
                else:
                    min_date = 2025
                    break
            except ValueError:
                print("⚠️ Invalid input. Please enter a number, not letters or symbols.")

            min_date_input = input("\nRe-enter the earliest release year: ")

    max_date_input = input("Enter the latest release year: ")
    if not max_date_input:
        max_date = ""
    else:
        while True:
            try:
                max_date = int(max_date_input)
                if max_date >= 2025:
                    max_date = 2075
                    break
                elif min_date != "" and max_date < min_date:
                    print(
                        "\nLatest release year must me more than earliest release year"
                    )
                else:
                    break
            except ValueError:
                print("⚠️ Invalid input. Please enter a number, not letters or symbols.")

            max_date_input = input("\nRe-enter the latest release year: ")

    url += "&release_date=" + str(min_date) + "," + str(max_date)

    return url


url = gather_info(base_url)

headers = {"User-Agent": "Chrome (Windows 10.0; Win64; x64)"}


page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, "html.parser")

name_cells = soup.find_all("h3", class_="ipc-title__text ipc-title__text--reduced")

name_cells.pop(len(name_cells) - 1)


for cell in name_cells:
    print(cell.text.strip())
