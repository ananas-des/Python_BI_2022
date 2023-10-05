import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
import time
import datetime
import io
from dotenv import load_dotenv


# Task1
response = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mp_mv250")
soup = BeautifulSoup(response.content, "lxml")

films_dict = {}
# tags list with title name, year, and director
rating_list = soup.find_all("td", attrs={"class": "titleColumn"})

# extracting title names
titles = [title.find('a').get_text() for title in rating_list]
films_dict.update({"name": titles})

# extracting ranks
ranks = [int(i.a.previous_element.strip()[:-1]) for i in rating_list]
films_dict.update({"rank": ranks})

# extracting years
years_pattern = re.compile(r'\d{4}')
years = [re.search(years_pattern, title.find('span').get_text())[0] for title in rating_list]
films_dict.update({"year": years})

# extracting ratings and n_reviews
rate_reviews_list = soup.find_all("td", attrs={"class": "ratingColumn imdbRating"})
rate_reviews_pattern = re.compile(r'(\d+([,\.]{1}\d+)+)')
films_dict.update({"rating": [], "n_reviews": []})
for i in rate_reviews_list:
    (mark, _), (n_votes, _) = re.findall(rate_reviews_pattern, i.strong.attrs["title"])
    films_dict["rating"].append(float(mark))
    films_dict["n_reviews"].append(int(n_votes.replace(",", "")))

# extracting directors    
directors = [direc.a.attrs["title"].split(" (")[0] for direc in rating_list]
films_dict.update({"directors": directors})
films_df = pd.DataFrame(films_dict)

# Subtask1
top_reviewed = films_df[["name", "n_reviews"]].sort_values(by="n_reviews", ascending=False).head(4)
top_reviewed

# Subtask2
top_years = films_df.groupby("year")["rating"].mean().sort_values(ascending=False).head(4)
top_years

# Subtask3
directors_count  = films_df["directors"].value_counts()
directors_count = directors_count[directors_count > 2]

fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
sns.barplot(x=directors_count.index, y=directors_count.values, palette="twilight", ax=ax)
ax.set_title("Films number for directors from Top 250 IMDb", fontsize=14, fontweight='bold')
ax.set_xlabel("director", fontweight='bold')
ax.set_xticklabels(directors_count.index, rotation=45, ha="right")
ax.set_ylabel("count", fontweight='bold');

# Subtask4
films_df.groupby("directors")["n_reviews"].sum().sort_values(ascending=False).head(4)

# Subtask5
print(films_df.shape)
films_df.head()

# Task2
load_dotenv()
TG_API_TOKEN = os.getenv("TG_API_TOKEN")
chat_id = os.getenv("TG_CHAT_ID")

def telegram_logger(chat_id):
    '''A decorator for calculating function exacution time, 
    creating .log file, and sending it to telegram bot
    
    Parameters:
        chat_id (str): chat id for sending messages by bot
    '''
    
    
    def wrapper(func):
        def inner_func(*args, **kwargs):
            url = f'https://api.telegram.org/bot{TG_API_TOKEN}/'
            text_buffer = io.StringIO()
            sys.stdout = sys.stderr = text_buffer
            
            try:
                start = time.time()
                if func.__name__ == 'long_lasting_function':
                    longtime = 200000000
                    result = None
                else:
                    result = func(*args, **kwargs)
                    longtime = 0
                run_time = time.time() - start + longtime
                
                if run_time > 24*60*60:
                    run_time = round(run_time)
                run_time = datetime.timedelta(seconds=run_time)
                
                text = f'Function `{func.__name__}` is done.\nRuntime: `{run_time}`'
            except Exception as error:
                text = f'Function `{func.__name__}` failed.\n`{type(error).__name__}: {error}`'
            sys.stdout, sys.stderr = sys.__stdout__, sys.__stderr__
            data = {'chat_id': chat_id, 'text':text, 'caption':text, 'parse_mode':'Markdown'}
            file = text_buffer.getvalue()
            if file:
                requests.post(url + 'sendDocument', data=data, files={'document':(f'{func.__name__}.log',file)})
            else:
                requests.post(url + 'sendMessage', data=data)
            return result
        return inner_func
    return wrapper


@telegram_logger(chat_id)
def good_function():
    print("This goes to stdout")
    print("And this goes to stderr", file=sys.stderr)
    time.sleep(2)
    print("Wake up, Neo")

@telegram_logger(chat_id)
def bad_function():
    print("Some text to stdout")
    time.sleep(2)
    print("Some text to stderr", file=sys.stderr)
    raise RuntimeError("Ooops, exception here!")
    print("This text follows exception and should not appear in logs")
    
@telegram_logger(chat_id)
def long_lasting_function():
    time.sleep(200000000)


good_function()

try:
    bad_function()
except Exception:
    pass

long_lasting_function()