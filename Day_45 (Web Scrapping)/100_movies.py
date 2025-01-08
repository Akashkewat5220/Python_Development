import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
movie_title = soup.find_all(name="h3", class_="title")

all_movie = [movie.get_text() for movie in movie_title]
all_movie = all_movie[::-1]


with open("all_movie.txt", mode="w", encoding="utf-8") as file:
    for movie in all_movie:
        file.write(f"{movie}\n")

