import matplotlib
import requests 
from bs4 import BeautifulSoup   
import csv 
from itertools import zip_longest

#libraries for plotting and visualization of data 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

result = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")

src = result.content 
#print(src) to verify the content

soup = BeautifulSoup(src, "lxml")

#title, date, rating of the movies 
movie_titles = soup.find_all("td", {"class": "titleColumn"})
movie_date = soup.find_all("span", {"class": "secondaryInfo"})
movie_rating = soup.find_all("td", {"class": "ratingColumn imdbRating"})

#print(movie_titles[0].text) test to verify the content

#extract needed info 
for i in range (len(movie_titles)):
    movie_titles[i] = movie_titles[i].text
    movie_titles[i] = movie_titles[i].replace("\n", "")
    movie_titles[i] = movie_titles[i].strip()

for i in range (len(movie_date)):
    movie_date[i] = movie_date[i].text
    movie_date[i] = movie_date[i].replace("(", "")
    movie_date[i] = movie_date[i].replace(")", "")
    movie_date[i] = movie_date[i].strip()

for i in range (len(movie_rating)):
    movie_rating[i] = movie_rating[i].text
    movie_rating[i] = movie_rating[i].replace("\n", "")
    movie_rating[i] = movie_rating[i].strip()


data = [movie_titles, movie_date, movie_rating]
export_data = zip_longest(*data, fillvalue = '')


#opening the csv file 

with open (r"C:\\Users\\microbox\Desktop\\python programming\web scraping\\file1.csv", "w", encoding="ISO-8859-1", newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(("Movie Title", "Release Date", "Rating"))
    wr.writerows(export_data)


#visualize the rating of movies 

#import data from csv file 
df = pd.read_csv(r"C:\\Users\\microbox\Desktop\\python programming\web scraping\\file1.csv", encoding="latin-1")
df.head()

df.shape 
#plotting the data
plt.figure(figsize=(10,10))
plt.bar(df['Movie Title'].head(20), df['Rating'].head(20), color='b')
plt.xticks(rotation=90)
plt.xlabel('Movie Title')
plt.ylabel('Rating')
plt.title('Top 20 Movies')
plt.show()






