# def fetch_stats(selected_user, df):
#     if selected_user == 'Overall':
#         # fetch all msg
#         return df.shape[0]
#         # no of words
#         words = []
#         for message in df['message']:
#             words.extend(message.split())
#         return num_message, len(words)
#     else:
#         new_df = df[df['user'] == selected_user]
#         num_message=new_df.shape[0]
#         words = []
#         for message in df['message']:
#             words.extend(message.split())
#         return num_message, len(words)
#
from urlextract import URLExtract
extract = URLExtract()
from wordcloud import WordCloud
import emoji
from collections import Counter


def fetch_stats(selected_user, df):

    # filter dataframe
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # number of messages
    num_messages = df.shape[0]

    # number of words
    words = []
    for message in df['message']:
        words.extend(message.split())

    # fetch no of media messages
    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    # fetch no of media msg
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))
    return num_messages, len(words), num_media_messages, len(links)


def most_busy_users(df):
    x=df['user'].value_counts().head()
    df=round(df['user'].value_counts()/df.shape[0]*100, 2)

    return x,df



# def create_wordcloud (selected_user, df):
#     if selected_user != 'Overall':
#         df = df[df['user'] == selected_user]
#     wc= WordCloud (width=600,height=500,min_font_size=10,background_color='white')
#     df_wc=wc.generate(df['message'].str.cat(sep=" "))
#     return df_wc
def create_wordcloud(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    text = " ".join(df['message'])

    wc = WordCloud(
        width=500,
        height=300,
        min_font_size=10,
        background_color='white',
        collocations=False
    )

    return wc.generate(text)


# def emoji_helper(selected_user, df):
#     if selected_user != 'Overall':
#         df = df[df['user'] == selected_user]
#
#     emojis = []
#
#     for message in df['message']:
#         emojis.extend([c for c in message if c in emoji.EMOJI_DATA])
#     emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
#     return emoji_df

# from collections import Counter
import pandas as pd
# import emoji

def emoji_helper(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []

    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])

    emoji_df = pd.DataFrame(
        Counter(emojis).most_common(),
        columns=['emoji', 'count']
    )

    return emoji_df

# def monthly_timeline(selected_user, df):
#
#     if selected_user != 'Overall':
#         df = df[df['user'] == selected_user]
#     timeline = (df.groupby(['year','month_num','month']).count()['message'].reset_index().sort_values(['year','month_num']))
#     time=[]
#     for i in range(timeline.shape[0]):
#         time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))
#     timeline['time']= time
#     return timeline

def monthly_timeline(selected_user, df):

    # filter user
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # 🔴 VERY IMPORTANT: create columns here
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()

    timeline = (
        df.groupby(['year','month_num','month'])
          .count()['message']
          .reset_index()
          .sort_values(['year','month_num'])
    )

    timeline['time'] = timeline['month'] + "-" + timeline['year'].astype(str)

    return timeline

def daily_timeline(selected_user, df):

    # filter user
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    daily_timeline=df.groupby("only_date").count()['message'].reset_index()
    return daily_timeline

def week_activity_map(selected_user, df):

    # filter user
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    return df['day_name'].value_counts()

def month_activity_map(selected_user, df):

    # filter user
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    return df['month'].value_counts()
