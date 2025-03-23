from urlextract import URLExtract
extractor = URLExtract()
from wordcloud import WordCloud, STOPWORDS
import pandas as pd
import seaborn as sns
import emoji
from collections import Counter

def fetch_stats(selected_user,df):

    # Restructuring the df according to use
    if selected_user !='Overall':
        df=df[df['user']==selected_user]

    # 1. Number of messages
    num_mess = df.shape[0]

    #2.Number of words
    words=[]
    for message in df['message']:
        words.extend(message.split())

    # 3.Number of media files
    num_media_files=df[df['message']=='<Media omitted>\n'].shape[0]

    # links shared
    links=[]
    for message in df['message']:
        links.extend(extractor.find_urls(message))
    num_links=len(links)
    return num_mess, len(words), num_media_files, num_links

def most_busy_users(df):
    x=df['user'].value_counts().head()
    new_df=round((df['user'].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={'index':'Name','user':'Percentage'})
    return x,new_df

def create_wordcloud(selected_user,df):
    # Restructuring the df according to use
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # removing the unnecessary word that are not part of the chat
    custom_stopwords = set(STOPWORDS)
    unwanted_words={"<Media omitted>\n","Media","omitted",'Bhai','hai','tha','ho','h','hmm','kya','aur','nhi','ke','kya','hi','to','bhi','nahi','toh','se','ka','ki','are','raha','aa','kar','koi','main','na','hu','m','ye','ko','k','rha','pe','gya','sab'}
    custom_stopwords.update(unwanted_words)

    wc=WordCloud(width=520, height=400, min_font_size=10,background_color='white',stopwords=custom_stopwords)
    df_wc=wc.generate(df['message'].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']
    stop_words = ['Bhai', 'hai', 'tha', 'ho', 'h', 'hmm', 'kya', 'aur', 'nhi', 'ke', 'kya', 'hi', 'to', 'bhi', 'nahi',
                  'toh', 'se', 'ka', 'ki', 'are', 'raha', 'aa', 'kar', 'koi', 'main', 'na', 'hu', 'm', 'ye', 'ko', 'k',
                  'rha', 'pe', 'gya', 'sab']

    words = []
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    df=pd.DataFrame(Counter(words).most_common(20))
    return df

def emojis_analysis(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.UNICODE_EMOJI['en']])

    df=pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
    return df

def monthly_timeline(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    timeline=df.groupby(['year','month']).count()['message'].reset_index()
    time=[]
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))
    timeline['time']=time

    return timeline

def daily_timeline(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    df['only_date'] = df['date'].dt.date
    daily_timeline=df.groupby('only_date').count()['message'].reset_index()
    return daily_timeline


def day_activity(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()

def month_activity(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()

def busy_hours(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))
    df['period'] = period
    df_new = df.groupby(['period', 'day_name'])['message'].count().reset_index()
    df_new = df_new.sort_values(by=['period'])
    time_heatmap=df_new.pivot_table(index='day_name', columns='period', values='message', aggfunc='sum')

    return time_heatmap