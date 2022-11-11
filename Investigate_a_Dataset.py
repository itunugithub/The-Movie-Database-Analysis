#!/usr/bin/env python
# coding: utf-8

# 
# 
# # Project: The Movie Database Analysis
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# ### Dataset Description 
# 
# In this project, I will be analyzing the movie database which contains information on over 10,000 movies as well as other information on revenue, runtime, popularity, production companies etc. The objective of this project is to analyse the various trends in the data set and examine the correlation between the differnt variables.
# 
# ### Questions for Analysis
# 1. Which production company produced the highest movie
# 2. Which production company generated the highest revenue
# 3. Which movie generated the highest revenue and what year was it released
# 4. List the top 5 genres with the higest rating
# 5. Examine the correlation between the variables in the data.
# 

# **Loading the libraries required for the analysis**

# In[62]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# In this segment I will be inspecting the data frame to understand it's structure then filter out information that is not important for this analysis.

# **Read and name data frame**

# In[56]:


movies_df = pd.read_csv('tmdb-movies.csv')


# The data set was imported and named movies_df

# **Find out how many sample is the dataframe**

# In[29]:


movies_df.info()
movies_df.shape


# The Analysis reveals that there are 10,866 rows and 21 columns in the movies_df

# **View the first five of the movies_df**

# In[30]:


movies_df.head()

The above provides information on the first five columns of the movies_df
# **Viewing null values in the movies_df**

# In[31]:


movies_df.isnull().sum()


# _Some of the parameters have missing values in them such as cast, homepage, director, tagline, keywords, overview, genres, production companies_

# **Checking for duplicates**

# In[32]:


movies_df.duplicated().sum()


# One duplicate record was found in the movies_df

# **Checking for unique rows in the movies_df**

# In[33]:


movies_df.nunique()


# **List of some movie titles in the data frame**

# In[34]:


movies_df['original_title'].unique()


# _The above shows the unique values in the data set, there are 10,571 unique movie titles in the data frame and some of the movie_titles are as seen in the analysis.

# **Summary Statistics**

# In[35]:


movies_df.describe()


# 
# ### Data Cleaning
# 1. In this segment, I will be eliminating some of the columns that are not relevant for this analysis such as imdb_id,homepage,overview and keyword.
# 2. Drop rows with null values
# 3. Drop rows with duplicate values
#  

# **Elimination of irrelevant columns**

# In[36]:


movies_df.drop(['imdb_id', 'homepage', 'overview', 'keywords'], axis =1, inplace = True)
movies_df.info()


# In[37]:


movies_df.drop(['id'], axis =1, inplace = True)
movies_df.info()


# **Drop rows with null values**

# In[38]:


movies_df.dropna(inplace = True)


# In[40]:


movies_df.isnull().sum()


# In[41]:


movies_df.shape


# **Drop rows with duplicate records**

# In[42]:


movies_df.drop_duplicates(inplace = True)
movies_df.shape


# In[43]:


movies_df.describe()


# _At the end of the data cleaning, the rows and columns have been reduced to 7635 and 16 respectively and has also impacted the summary statistics of the data frame._

# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# In this segment I will be addressing the research questions as stated at the beginning of the project and creating visual representations as appropriate.
# 
# 
# ### Research Question 1 - Which production company produced the highest number of movies

# In[16]:


Top_production_company = movies_df.groupby('production_companies').original_title.count().sort_values(ascending = False)[0:10]
Top_production_company


# _The analysis above shows that Paramount pictures production company produced the highest number of movies (141)._

# **Creating a function for bar plots**

# In[17]:


def plots(heading, xlabel, ylabel, title):
    plt.figure(figsize=(10,8))
    heading.plot(kind='bar')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    
    return plots


# **Visual representation of the Top 10 production companies**

# In[19]:


heading = movies_df.groupby('production_companies').original_title.count().sort_values(ascending = False)[0:10]


# In[ ]:


plots(heading, 'PRODUCTION COMPANIES', 'MOVIE COUNT', 'TREND OF THE TOP 10 PRODUCTION COMPANIES');


#     Fig. 1:Trend of the top 10 production companies

# _The chart above shows the top 10 production companies with paramount pictures being the highest production company in the data frame._

# ### Research Question 2 - Which production company generated the highest revenue

# In[65]:


get_ipython().system(' pip install --upgrade pandas==0.25.0')


# In[66]:


genres_data = movies_df.assign(genres_ = movies_df['genres'].str.split('|')).explode('genres_')
genres_data['genres_'].value_counts().head(5)


# In[63]:


production_companies_data = movies_df.assign(production_companies_ = movies_df['production_companies'].str.split('|')).explode('production_companies_')
production_companies_data['production_companies_'].value_counts().head(5)


# In[21]:


Production_company_with_highest_revenue = movies_df.groupby('production_companies').revenue.sum().sort_values(ascending = False).head(5)
Production_company_with_highest_revenue


# In[22]:


heading = movies_df.groupby('production_companies').revenue.sum().sort_values(ascending = False).head(5)


# In[23]:


plots(heading, 'production_companies', 'revenue_generated', 'TOP 5 PRODUCTION COMPANIES WITH HIGHEST REVENUE');


# Fig. 2:Top 5 production Companies with the highest Revenue

# _The analysis above shows that paramount pictures generated the highest revenue_

# ### Research Question 3 - Which movie generated the highest revenue and what year was it released.

# In[25]:


movie_with_highest_revenue = movies_df.groupby(['original_title', 'release_year']).revenue.sum().sort_values(ascending = False).head(5)
movie_with_highest_revenue


# In[26]:


heading = movies_df.groupby(['original_title', 'release_year']).revenue.sum().sort_values(ascending = False).head(5)


# In[27]:


plots(heading, 'MOVIE TITLE', 'REVENUE', 'TOP 5 MOVIES WITH HIGHEST REVENUE');


# Fig. 3:Top 5 Movies with the Highest Revenue

# _The above shows that Avatar which was released in the year 2009 generated the highest revenue_

# ### Research Question 4 - List the top 5 genres with the highest rating

# In[28]:


Most_rated= movies_df.groupby('genres').vote_count.count().sort_values(ascending = False).head(5)
Most_rated


# In[29]:


heading = movies_df.groupby('genres').vote_count.count().sort_values(ascending = False).head(5)


# In[30]:


plots(heading, 'GENRES', 'VOTE COUNT', 'TOP 5 GENRES WITH HIGHEST RATING');


# Fig. 4:Top 5 genres with the higest Rating

# _The analysis shows that comedy, drama, Horror, Thriller and Romance are the top 5 rated genres, however comedy is the most preffered, this analysis will help to inform producers/directors on their focus areas while also improving on others._

# ##### Single variable analysis for some features of the dataset

# ###### 1. Distribution plot for budget

# In[6]:


sns.distplot(movies_df['budget'], hist = False).set(title = 'Distplot of Budget');


# Fig. 5:Displot of Budget

# The above plot is right or positively skewed. It informs us that all values in the budget column are positive.

# ###### 2. Distribution Plot for Revenue

# In[5]:


sns.distplot(movies_df['revenue'], hist = False).set(title = 'Distplot of Revenue');


# Fig. 6:Displot of Revenue

# The above plot is right or positively skewed. It informs us that all values in the revenue column are positive.

# ###### 3. Distribution plot for Vote Count

# In[8]:


sns.distplot(movies_df['vote_count'], hist = False).set(title = 'Vote Count');


# Fig. 7:Displot of Vote Count

# The above plot shows that the dataset in the vote count column is positively skewed and that it also contain outliers.

# ### Research Question 5 - Examine the correlation between variables in the data frame

# **Correlation Matrix**
# _The purpose of the correlation matrix is to check for relationship btw variables.

# In[31]:


corr = movies_df.corr()
plt.figure(figsize = (18,10))
sns.heatmap(corr, annot=True, cmap = 'BuPu');


# - In the The matrix above, the correlation between popularity and revenue is 0.66 depicting a positive relationship between the two variables
# - The correlation between vote count and revenue is 0.78, this shows that there is a strong postive relationship between the two variables
# - The correlation bbetween budget and revenue is 0.73 which also means that there is a strong relationship between the two variables

# ###### <a id='conclusions'></a>
# ## Conclusions
# **Results**
# 
# Following the analysis carried out on the movie database I was able to statiscally and visually represent the findings gotten from the data frame. Below are some of the  insights drawn from the analysis carried out 
# 
# - Which production company produced the highest movie: This ananlysis helps to understand the production capcity of each production companies over the year. The result shows that Paramount pictures production company produced the highest number of movies (141)
#   
#   We got the production companies with highest number of movies released by applying the groupby function to the production_companies and original title column, and thereafter plotted the bar chart.
#   
#     
# - Which production company generated the highest revenue:The analysis on production company with the higest shows that  Paramount pictures recorded the highest revenue which amounts to 7.8b, this helps to understand the financial strength of the production companies which can further support proper decision making.
#   
#   We obtained the production companies with highest revenue by applying the groupby function to the production companies and revenue column, and there after plotting the bar chart.
#   
#     
# - Which movie generated the highest revenue and what year was it released: This question is to help us evaluate the relationship btw release year and revenue generated. It will help us check if the release year has an impact on the revenue generated. Result shows that the movie titled Avatar was released in 2009 and it recorded the highest revenue amounting to 2.7b
#   
#   To obtain the movie which generated the highest revenue and its release year, we applied the groupby function to the columns original_title, release_year, and thereafter extracted the revenue from the resulting dataframe. Furthermore, we used the bar plot to obtain the top 5 movies.
#   
#     
# - List the top 5 genres with the highest rating:The analysis on top 5 genres with the highest rating shows that comedy, drama, Horror, Thriller and Romance are the top 5 rated genres, however comedy is the most preffered, this result will help to inform producers/directors on their focus areas and how to better suit their audience while also improving on others.
#   
#   To obtain the genres with highest rating, we applied the groupby function to the genres and vote count column. The plot of the top 5 genres was done using the bar chart.
#   
#     
# - Examine the correlation between the variables in the data:  The analysis also examine the correlation between the variables in the data frame and the finding shows a definite relationship between revenue and other variables like vote_count, popularity and budget.
#   
#   The correlation between the features was obtained using the correlation matrix plot.
#   
# 
# 
# **Limitation**
# - The data set had a large number of rows with null values and when dropped affected some of the values in the summary statistics
# 

# **Reference:**
# Google
