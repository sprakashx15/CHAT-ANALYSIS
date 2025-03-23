import streamlit as st
import matplotlib.pyplot as plt
import preprocessor
import helperfns
import seaborn as sns

st.sidebar.title("WHATSAPP CHAT ANALYZER")


# uploading the file
uploaded_file = st.sidebar.file_uploader("Choose a txt file")
if uploaded_file:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    # st.dataframe(df)

    # get the list of in list
    user_list=df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Overall")
    selected_user = st.sidebar.selectbox("Show Analysis of :",user_list)

    if st.sidebar.button("Analyze"):

        num_mess,words,num_media_files,num_links=helperfns.fetch_stats(selected_user,df)
        st.title("Top Statistics")
        col1,col2,col3,col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_mess)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Media Shared")
            st.title(num_media_files)
        with col4:
            st.header("Links Shared")
            st.title(num_links)

        #  monthly timeline

        st.title("Monthly Timeline")

        timeline=helperfns.monthly_timeline(selected_user,df)
        fig,ax=plt.subplots()
        ax.plot(timeline['time'],timeline['message'],color='green')
        plt.xticks(rotation=90)
        st.pyplot(fig)

        # daily timeline

        st.title("Daily Timeline")
        daily_timeline=helperfns.daily_timeline(selected_user,df)
        fig,ax=plt.subplots()
        plt.figure(figsize=(18, 10))
        ax.plot(daily_timeline['only_date'], daily_timeline['message'],color='black')
        st.pyplot(fig)

        # activity map
        st.title("Activity Map")
        col1,col2=st.columns(2)
        with col1:
            st.header("Most Busy Day")
            busy_day=helperfns.day_activity(selected_user,df)
            fig,ax=plt.subplots()
            ax.bar(busy_day.index,busy_day.values,color='purple')
            plt.xticks(rotation=90)
            st.pyplot(fig)

        with col2:
            st.header("Most Busy Month")
            busy_month = helperfns.month_activity(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='blue')
            plt.xticks(rotation=90)
            st.pyplot(fig)

        # busy hours

        st.header("Most Busy Hours")
        time_heatmap=helperfns.busy_hours(selected_user,df)
        fig,ax=plt.subplots()
        ax=sns.heatmap(time_heatmap)
        st.pyplot(fig)


        # finding the busiest person
        if selected_user == "Overall":
            st.title("Overall Statistics")
            st.header("Most Busy Users")
            x,new_df=helperfns.most_busy_users(df)
            fig, ax = plt.subplots()

            col1,col2=st.columns(2)

            with col1:
                ax.bar(x.index, x.values,color=['red', 'orange', 'yellow', 'green', 'blue'])
                plt.xticks(rotation=90)
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df,height=420,width=500)

        # creating WordCloud
        st.title("Word Cloud")
        df_wc=helperfns.create_wordcloud(selected_user,df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # most common words
        st.title("Most Common Words")
        most_common_df=helperfns.most_common_words(selected_user,df)

        fig, ax = plt.subplots()
        ax.barh(most_common_df[0],most_common_df[1],color='orange')
        plt.xticks(rotation=90)
        st.pyplot(fig)

        # emojis analysis
        st.title("Emojis_Uses")
        emojis_df=helperfns.emojis_analysis(selected_user,df)
        col1,col2=st.columns(2)
        with col1:
            st.dataframe(emojis_df,height=420,width=500)
        with col2:
            fig, ax = plt.subplots()
            ax.pie(emojis_df[1].head(10),labels=emojis_df[0].head(10),autopct='%1.0f%%')
            st.pyplot(fig)