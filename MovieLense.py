import numpy as np
import pandas as pd

#C:\Users\jangs\PycharmProjects\untitled\venv\Scripts


ratings = pd.read_csv("./ml-latest-small/ratings.csv")
movies = pd.read_csv("./ml-latest-small/movies.csv")
data   =  pd.merge(ratings, movies, on = 'movieId')


ratings_rank = ratings.pivot_table(
    index='userId', values='rating',
    aggfunc=np.mean
)

ratings_rank_max2 = ratings_rank.groupby("userId").filter(lambda x: x["rating"] == ratings_rank["rating"].max())

strTmp = ''
intTmp =  1
for userTmp in ratings_rank_max2.index:
    strTmp += str(userTmp)
    if intTmp <len(ratings_rank_max2.index):
        strTmp += ','
        intTmp += 1
print('1-1. 최고평점 : '  + strTmp)

#----------------------------

ratings_rank_min2 = ratings_rank.groupby("userId").filter(lambda x: x["rating"] == ratings_rank["rating"].min())
strTmp = ''
intTmp =  1
for userTmp in ratings_rank_min2.index:
    strTmp += str(userTmp)
    if intTmp < len(ratings_rank_min2.index):
        strTmp += ','
        intTmp += 1
print('1-2. 최저평점  : ' + strTmp)

#----------------------------

moveis_rank = data.pivot_table(
    index='title', values='rating',
    aggfunc=np.mean
)
moveis_rank_max2 = moveis_rank.groupby("title").filter(lambda x: x["rating"] == moveis_rank["rating"].max())
moveis_rank_min2 = moveis_rank.groupby("title").filter(lambda x: x["rating"] == moveis_rank["rating"].min())

strTmp = ''
intTmp = 1
for userTmp in moveis_rank_max2.index:
    strTmp += str(userTmp)
    if intTmp < len(moveis_rank_max2.index):
        strTmp += ','
        intTmp += 1

print('2-1. 최고평점 : ' + strTmp)
strTmp = ''
intTmp = 1
for userTmp in moveis_rank_min2.index:
    strTmp += str(userTmp)
    if intTmp < len(moveis_rank_min2.index):
        strTmp += ','
        intTmp += 1
print('2-2. 최저평점  : ' + strTmp)

#----------------------------

movies2 = movies.loc[movies["genres"].str.contains("Crime") & movies["genres"].str.contains("Thriller")]
data2   =  pd.merge(ratings,movies2, on = 'movieId')

genres_rank = data2.pivot_table(
    index='title', values='rating',
    aggfunc=np.mean
)
genres_rank_max2 = genres_rank.groupby("title").filter(lambda x: x["rating"] == genres_rank["rating"].max())

strTmp = ''
intTmp = 1
for userTmp in genres_rank_max2.index:
    strTmp += str(userTmp)
    if intTmp < len(genres_rank_max2.index):
        strTmp += ','
        intTmp += 1

print('3. 범죄스릴러 장르 최고평점  : ' + strTmp)
