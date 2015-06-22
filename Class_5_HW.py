# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 21:51:57 2015

@author: FrankC
"""

cd
cd desktop/DAT7/data

import pandas as pd

movies = pd.read_csv('imdb_1000.csv')

type(movies.star_rating[0])
type(movies.title[0])
type(movies.content_rating[0])
type(movies.genre[0])
type(movies.duration[0])
type(movies.actors_list[0])

movies.duration.mean()

movies.sort('duration').head(5)
movies.sort('duration').tail(5)

movies.duration.plot(kind='hist',bins=10)
movies.duration.plot(kind='box')

movies.content_rating.value_counts()

movies.groupby('content_rating').content_rating.count().plot(kind='bar')

movies.content_rating.replace(['NOT RATED','APPROVED','PASSED','GP'],'UNRATED',inplace=True)
movies.content_rating.replace(['X','TV-MA'],'NC-17',inplace=True)

movies.content_rating.value_counts()

movies.isnull().sum()

movies[movies.content_rating.isnull()==True]

movies.content_rating[187] = 'PG'
movies.content_rating[649] = 'PG'
movies.content_rating[936] = 'PG'

movies[movies.duration>=120].star_rating.mean()
movies[movies.duration<120].star_rating.mean()

movies.plot(kind='scatter',x='duration',y='star_rating')

movies.groupby('genre').duration.mean()

