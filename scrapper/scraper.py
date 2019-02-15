import requests
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import multiprocessing

path = './250links.csv'
df_links = pd.read_csv(f'{path}')

imdb_links = []
for link in df_links['links']:
    imdb_links.append(link)
url = f'https://www.imdb.com/title/{imdb_links[1]}/'
all_movie_title = []
all_movie_year = []
all_movie_time = []

all_genres = []

all_movie_rating = []
all_movie_thumb = []
all_movie_plot = []
all_movie_dir = []

all_movie_stars = []

def title():
  for link in tqdm(imdb_links):
    url = f'https://www.imdb.com/title/tt0{link}/'
    response = requests.get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    title = html_soup.find('div', class_='title_wrapper')
    try:
      movie_title = title.h1.text
    except:
      continue
    
    try:
      movie_year = title.find('a').text
    except:
      continue
    
    try:
      movie_time = title.find('div', class_='subtext').time.text
    except:
      continue
    
    try:
      a_genres = title.find_all('a')
      genres = []
      for i in range(1, len(a_genres)-1):
          genres.append(a_genres[i].text)
    except:
      continue
        
    all_movie_title.append(movie_title)
    all_movie_year.append(movie_year)
    all_movie_time.append(movie_time)

    all_genres.append(genres)
    print('done_title')
    sleep(randint(1,4))

def stars(count):
      for link in imdb_links:
        url = f'https://www.imdb.com/title/{link}/'
        response = requests.get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        info = html_soup.find_all('div', class_='credit_summary_item')

        try:
              movie_dir = info[0].a.text
        except:
              continue

        try:
              tot_stars = info[2].find_all('a')
        except:
              continue

        movie_stars = []
        for i in range(len(tot_stars)-1):
            movie_stars.append(tot_stars[i].text)

        all_movie_dir.append(movie_dir)
        all_movie_stars.append(movie_stars)
        print('done_stars:',count)
        sleep(randint(1,4))
        count += 1

def rating(i):
      for link in imdb_links:
        url = f'https://www.imdb.com/title/{link}/'
        response = requests.get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        rating = html_soup.find('div', class_='ratingValue')
        poster = html_soup.find('div', class_='poster')
        plot = html_soup.find('div', class_='summary_text')
        try:
              movie_rating = rating.span.text
        except:
              continue

        try:
              movie_thumb = poster.img['src']
        except:
              continue

        try:
              movie_plot = plot.text
        except:
              continue

        all_movie_rating.append(movie_rating)
        all_movie_thumb.append(movie_thumb)
        all_movie_plot.append(movie_plot)
        print('done_rating:',i)
        sleep(randint(1,4))
        i += 1

p1 = multiprocessing.Process(target = title)
p2 = multiprocessing.Process(target = rating)
p3 = multiprocessing.Process(target = stars)

p1.start() 
p2.start()
p3.start()

# process IDs 
print("ID of process p1: {}".format(p1.pid)) 
print("ID of process p2: {}".format(p2.pid))
print("ID of process p2: {}".format(p3.pid))

# wait until processes are finished 
p1.join() 
p2.join()
p3.join()

# both processes finished 
print("Both processes finished execution!") 
