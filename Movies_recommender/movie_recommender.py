# -*- coding: utf-8 -*-
"""Movie_recommender.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zWbslXz90JbzDMvQ0XpXIu-_qRIHdKf8
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import ast
import sklearn
import nltk

"""#Data"""

credits=pd.read_csv('/content/drive/MyDrive/Movie_data/tmdb_5000_credits.csv')
movies=pd.read_csv('/content/drive/MyDrive/Movie_data/tmdb_5000_movies.csv')

print('Dimension of movies ',movies.shape)
print('Dimension of credits ',credits.shape)
print(movies.info())
print(credits.info())

"""##merging both dataframes"""

movies=movies.merge(credits,on='title')

"""##checking null values"""

sns.heatmap(movies.isnull(),cbar=False,cmap='viridis')
plt.show()

"""## keeping only required features"""

movies=movies[['id','title','overview','genres','keywords','cast','crew']]
movies.head()

movies.dropna(inplace=True)
movies.head()

"""## Extraction of tags and new dataset

### Extraction of Genres and keywords.
"""

def convert(obj):
  l=[];
  for i in ast.literal_eval(obj):
    l.append(i['name'])
  return l;
movies['genres']= movies['genres'].apply(convert)
movies['keywords']= movies['keywords'].apply(convert)

"""###Extraction of cast"""

def cast(obj):
  l=[]
  a=ast.literal_eval(obj)
  for i in range(4):
    l.append(a[i]['name'])
  return l
movies['cast']= movies['cast'].apply(convert)

"""###Extraction of Director"""

def director(obj):
  l=[]
  for i in ast.literal_eval(obj):
    if i['job']=='Director':
      l.append(i['name'])
      break;
  return l
movies['crew']=movies['crew'].apply(director)

"""###Extracting Overview"""

movies['overview']=movies['overview'].apply(lambda x:x.split())

movies['overview']=movies['overview'].apply(lambda x:[i.replace(" ","") for i in x])
movies['cast']=movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies['crew']=movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])
movies['genres']=movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
movies['keywords']=movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
movies.head()

"""###combining these to make tag"""

movies['tags']=movies['genres']+movies['overview']+movies['cast']+movies['crew']+movies['keywords']

"""###New dataset new_df"""

new_df=movies[['id','title','tags']]
new_df['tags']=new_df['tags'].apply(lambda x: " ".join(x))
new_df['tags']=new_df['tags'].apply(lambda x: x.lower())
new_df.head()

from nltk.stem.porter import PorterStemmer as PS
ps=PS()

def stem(text):
  y=[]
  for i in text.split():
    y.append(ps.stem(i))
  return " ".join(y)
  new_df['tags']=new_df['tags'].apply(stem)

"""##Vectorization"""

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=6000,stop_words='english')
vector=cv.fit_transform(new_df['tags']).toarray()
vector

print(cv.get_feature_names_out().size)

"""#Main function

##Similarity
"""

from sklearn.metrics.pairwise import cosine_similarity as cos
similarity_matrix=cos(vector)

similarity_matrix

similarity_matrix.shape

"""## judging"""

def recommend(movie):
  index=new_df[new_df['title']==movie].index[0]
  L=sorted(list(enumerate(similarity_matrix[index])),reverse=True,key=lambda x: x[1])[1:6:1]
  recommendations=[]
  for i in L:
    recommendations.append(new_df['title'][i[0]])
  print(recommendations)
  return

movie = input("Enter your current movie: ")
recommend(movie)

recommend('The Dark Knight Rises')

import pickle

# Assuming new_df is your dataframe
pickle.dump(new_df, open('movies.pkl', 'wb'))

new_df['title'].values

pickle.dump(similarity_matrix,open('similarity.pkl','wb'))

