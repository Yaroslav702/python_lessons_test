from bs4 import BeautifulSoup

with open('films.html') as file:
    soup = BeautifulSoup(file, "html.parser")


container = '.container'
data = soup.select()
