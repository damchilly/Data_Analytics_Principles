
# coding: utf-8

# # Data Analysis Example Using Pandas to create data sets
# 
# Question: How much more women like a movie than men do? 
# 
# Using Pandas for data consolidation, aggregation and grouping

# In[1]:

import pandas as pd


# In[2]:

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']


# In[3]:

users = pd.read_table('~/Documents/PYTHON/ml-1m/users.dat', sep = '::', header = None, names = unames, engine = "python")


# In[4]:

users[:5]


# In[5]:

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('~/Documents/PYTHON/ml-1m/ratings.dat', sep = '::', header = None, names = rnames, engine = "python")


# In[6]:

ratings[:5]


# In[8]:

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('~/Documents/PYTHON/ml-1m/movies.dat', sep = "::", header = None, names = mnames, engine = "python")


# In[10]:

movies[:5]


# Note that ages and occupations are coded as integers indicating groups described in the data set README file.
# We need to aggregate the ratings. In order to do that we need to reformat the original data. Consolidate all the data to have a single table using pandas' merge function
# First merge ratings with users then merging the result with the movies data Pandas infers which columns to use to join the files. It uses the common fields as keys.

# In[11]:

data = pd.merge(pd.merge(ratings, users), movies)


# In[12]:

data[:5]


# Getting the mean movie ratings for each film. Aggregating the ratings grouped by one or more user or movie atributes

# In[13]:

mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')


# In[14]:

mean_ratings[:5]


# FILTERING: Filter down movies that received at least 250 ratings. We are grouping the data by title and use size() to get a series of group sizes for each title.

# In[15]:

ratings_by_title = data.groupby('title').size()


# In[16]:

ratings_by_title[:10]


# In[17]:

active_titles = ratings_by_title.index[ratings_by_title >=250]


# In[18]:

active_titles


# The index of titles receiving at least 250 ratings can be then used to select rows from mean_ratings above.

# In[19]:

mean_ratings = mean_ratings.ix[active_titles]


# In[26]:

mean_ratings[:10]


# To extract the top films among female viewers, we sort by the F column in descending order

# In[22]:

top_female_ratings = mean_ratings.sort_values(by = 'F', ascending = False)


# In[23]:

top_female_ratings[:10]


# # Measuring Disagreement
# 
# Find the movies that are most divisive between male and female viewers.
# Add a column to mean_ratings containing the difference in means, then sort them.

# In[24]:

mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']


# In[25]:

sorted_by_diff = mean_ratings.sort_values(by = 'diff') 


# In[30]:

sorted_by_diff[:-5] 


# Reversing the order of the rows and again slicing off the top 15 rows, we get the movies preferred by men that women didn't rate as highly.

# In[31]:

sorted_by_diff[::-1][:15] 


# In[ ]:

sorted_by_diff.plot()


# Calculate the standard deviation of rating grouped by title

# In[32]:

rating_std_by_title = data.groupby('title')['rating'].std() 


# Filter down to active titles

# In[33]:

rating_std_by_title = rating_std_by_title.ix[active_titles] 


# Order Series by value in descending order

# In[36]:

rating_std_by_title.sort_values(ascending=False)[:10] 


# In[37]:

graph = rating_std_by_title.sort_values(ascending=False) 


# In[38]:

graph[:5] 


# In[40]:

import matplotlib.pyplot as plt


# In[61]:

get_ipython().magic('pylab')


# In[45]:

graph[:5].plot(kind='barh', rot=0, ) 


# In[58]:

import numpy as np 


# In[62]:

graph[:30].plot(kind='bar'); plt.axhline(0, color='k')


# In[ ]:



