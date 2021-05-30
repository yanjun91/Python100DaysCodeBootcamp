from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.timeout.com/newyork/movies/best-movies-of-all-time")

soup = BeautifulSoup(response.text, "html.parser")
movies = soup.find_all(name="h3", class_="card-title")
movie_rankings = [(item.getText()) for item in movies]

file_content = ""

for movie in movie_rankings:
    movies = movie.strip()
    if movies[0] != "C":
        file_content += movies
        file_content += "\n"

print(file_content)

with open("top100Movies.txt", "w", encoding="utf-8") as file:
    file.write(file_content)