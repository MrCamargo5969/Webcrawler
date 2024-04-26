from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument('window-size=800,800')

chrome_driver = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service = chrome_driver, options = chrome_options)

url = 'https://www.rottentomatoes.com/browse/movies_at_home/genres:action~sort:popular?page=2'
driver.get(url)
time.sleep(2)

film_titles = driver.find_elements(By.CLASS_NAME, 'p--small')
film_posts = driver.find_elements(By.CLASS_NAME, 'smaller')
film_scores = driver.find_elements(By.TAG_NAME, 'score-pairs-deprecated')

films_title = []
films_post = []
films_critic = []
films_audience =[]


for film in film_titles[4:]:
    films_title.append(film.text)

for date in film_posts:
    films_post.append(date.text.replace(',', ';'))

for score in film_scores:
    per = score.text.split('\n')
    films_critic.append(per[0])
    films_audience.append(per[1])

list_films = []
n = 0
for i, e in enumerate(films_title):
    list_films.append(f'{films_title[n]}, {films_post[n]}, {films_critic[n]}, {films_audience[n]}')
    n += 1

with open('filmes.csv', 'w', encoding='utf-8') as file:
            file.write('FILM, POSTING, CRITIC, AUDIENCE \n')
            for film in list_films:
                  file.write(film + '\n')

driver.quit()
