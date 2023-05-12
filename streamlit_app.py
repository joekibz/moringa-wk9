#!/usr/bin/env python
# coding: utf-8

# In[1]: Project - Visualizing data with streamlit


import praw
from datetime import datetime, timedelta
from praw.models import Submission

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from textblob import TextBlob
from wordcloud import WordCloud
import streamlit as st


# In[2]:


# Reddit API credentials
client_id = '4P3XofOI1xtQ_mQQ-NKqdA'
client_secret = 'Zydw7_cOkfXrfg104AxEXf0HIXobKw'
user_agent = 'kibz_app'


# In[3]:


# Connect to Reddit API
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
)


# In[4]:


# Load the icon image
icon_image = 'https://www.freeiconspng.com/thumbs/reddit-icon/red-reddit-icon-7.png'
# Insert the icon image above the sidebar text
st.sidebar.image(icon_image, use_column_width=True)

# Create sidebar element for subreddit selection
selected_subreddits = st.sidebar.text_input('Enter Subreddits (comma-separated)', 'all')

# Convert the comma-separated input into a list of subreddit values
subreddits = [sub.strip() for sub in selected_subreddits.split(',')]

# If no subreddits are selected, default to 'all'
if not subreddits:
    subreddits = ['all']


# In[5]:


# Create sidebar elements
default_keywords = ['telecom fraud','telecoms scam', 'phone fraud', 'billing fraud', 'identity theft', 'sim fraud', 'digital crime', 'identity theft']

custom_keywords = st.sidebar.text_input('Enter Custom Keywords (separated by comma)', '').split(',')
keywords = st.sidebar.multiselect('Select Keywords', default_keywords + custom_keywords, default=default_keywords)
dayz = st.sidebar.slider('Select Time Delta (in days)', 1, 50, 10,1)


# In[6]:


#Load page header intro at the top
st.title('Visual reddit-ing with Streamlit')
st.markdown("<h3 style='color:blue;'>How to use the dashboard </h3>", unsafe_allow_html=True)
st.markdown('On the left sidebar there are several widgets that can be used to modify reddit chart analysis below')
st.markdown('1_ "<b>Enter Subreddits(comma separated)</b>" - Enter a list of subreddits to search in separated by commas. Default is \
"all" subreddits.', unsafe_allow_html=True)
st.markdown('2_ "<b>Enter Custom Keywords(separated by comma)</b>" - Enter list of keywords to search for in all the subreddits listed in [1_]. On pressing enter the keywords are \
added to the listbox below [3_] from where multiples can be selected', unsafe_allow_html=True)
st.markdown('3_ "<b>Select Keywords</b>" - Select desired keywords from the listbox to add them to the subreddit search string',unsafe_allow_html=True)
st.markdown('4_ "<b>Select Time Delta(in days)</b>" - Use the slider to determine how many days back in time to search the subreddits specified in [1_]. Default is 10 days ',unsafe_allow_html=True)


# In[7]:


#Load CSS for use in display of charts
st.markdown(
    """
    <style>
    /* Add spacing between charts */
    .chart-container {
        margin-bottom: 20px;
    }

    /* Increase chart title font size */
    .chart-title {
        font-size: 24px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# In[8]:


#Fetch the data from reddit ...
# Initialize a list to store the data
data = []

# Search for posts matching multiple keywords in the specified time delta
for subreddit_name in subreddits:
    subreddit = reddit.subreddit(subreddit_name)
    for submission in subreddit.search(query=' '.join(keywords), sort='new', time_filter='week'):
        # Filter posts from the specified time delta
        if datetime.fromtimestamp(submission.created_utc) > datetime.now() - timedelta(days=dayz):

            post_data = {
                'Title': submission.title,
                'Author': submission.author.name,
                'Subreddit': submission.subreddit.display_name,
                'Date/Time': datetime.fromtimestamp(submission.created_utc),
                'Post Text': submission.selftext,
                'Score': submission.score,
                'URL': submission.url
            }
            data.append(post_data)

# Create a DataFrame from the collected data
df = pd.DataFrame(data)

# Print the DataFrame
#len(df)


# In[9]:


#Load the bar plot of mean scores 
if not df.empty:

    mean_scores = df.groupby('Subreddit')['Score'].mean()
    num_posts = df['Subreddit'].value_counts()

    fig,ax = plt.subplots(figsize=(14, 8))
    sns.barplot(x=mean_scores.index, y=mean_scores.values)
    plt.xticks(rotation=90)
    plt.xlabel('Subreddit')
    plt.ylabel('Mean Score')
    plt.title('Mean Score per Subreddit')
    plt.tight_layout()
    #plt.show()
    st.subheader("Reddit chart analytics")

    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="chart-title">Mean Scores</h2>', unsafe_allow_html=True)
    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)



else:
    st.write("No posts found matching the search criteria.")


# In[10]:


#Load histogram of number of posts per subreddit

if not df.empty:

    fig,ax = plt.subplots(figsize=(14, 8))
    sns.histplot(data=df, x='Subreddit', binwidth=1)
    plt.xticks(rotation=90)
    plt.xlabel('Subreddit')
    plt.ylabel('Number of Posts')
    plt.title('Number of Posts per Subreddit')
    plt.tight_layout()
    #plt.show()
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="chart-title">Posts per subreddit</h2>', unsafe_allow_html=True)
    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.write("No posts found matching the search criteria.")


# In[11]:


#Using TextBlob carry out sentiment analysis
#Then plot the distribution of sentiments

if not df.empty:
    
    # Perform sentiment analysis on each post text
    df['sentiment'] = df['Post Text'].apply(lambda x: TextBlob(x).sentiment.polarity)
    # Categorize sentiments as positive, negative, or neutral
    df['sentiment_category'] = pd.cut(df['sentiment'], bins=[-np.inf, -0.1, 0.1, np.inf], labels=['Negative', 'Neutral', 'Positive'])
    # Calculate the count of each sentiment category
    sentiment_counts = df['sentiment_category'].value_counts()


    #left_column.pyplot(sns.barplot(x=mean_scores.index, y=mean_scores.values))
    fig,ax =plt.subplots(figsize=(14, 8))
    sentiment_counts.plot(kind='bar', color=['red', 'gray', 'green'])
    plt.title('Sentiment Analysis - Fraud Posts')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    #plt.show()
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="chart-title">Sentiment Analysis</h2>', unsafe_allow_html=True)
    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.write("No posts found matching the search criteria.")


# In[12]:


# Concatenate the post titles or text into a single string
# Plot the WORD cloud

if not df.empty:
    
    text = ' '.join(df['Title'])

    # Create a WordCloud object
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    
    fig,ax = plt.subplots(figsize=(14, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud - Fraud Keywords')
    #plt.show()
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="chart-title">WORD cloud</h2>', unsafe_allow_html=True)
    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.write("No posts found matching the search criteria.")




# In[13]:


# Convert the 'created_utc' column to datetime
# Plot the frequency of fraud mentions over time on a line chart

if not df.empty:
    
    df['Convert_UTC'] = pd.to_datetime(df['Date/Time'], unit='s')
    # Group the data by date and count the number of mentions
    mention_counts = df['Convert_UTC'].dt.date.value_counts().sort_index()

    fig,ax = plt.subplots(figsize=(14, 8))
    mention_counts.plot(kind='line')
    plt.title('Frequency of Fraud Mentions over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Mentions')
    plt.xticks(rotation=45)
    #plt.show()
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="chart-title">Line chart of fraud mentions</h2>', unsafe_allow_html=True)
    st.pyplot(fig)
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.write("No posts found matching the search criteria.")



# In[14]:


# Display raw data fetched from reddit in a compact table
if not df.empty:
    st.subheader('Reddit Feed Summary')
    st.table(df[['Title', 'Author', 'Subreddit', 'Date/Time', 'URL']])

else:
    st.write("No posts found matching the search criteria.")


# In[ ]:




