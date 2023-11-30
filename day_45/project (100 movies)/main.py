from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

response = response.text

soup = BeautifulSoup(response, 'html.parser')

titles = soup.select("h3.title")
titles_names = []
for title in titles:
    titles_names.append(title.text.encode("utf-8"))

titles_names.reverse()

with open("project (100 movies)/movies.txt", "w", encoding="utf-8") as file:
    for title in titles_names:
        file.write(f'{title.decode("utf-8")}\n')