# import streamlit as st
# st.sidebar.title("Whatsapp-chat-analysis")
import streamlit as st
import helper
import matplotlib.pyplot as plt
from preprocessor import preprocess
import streamlit as st
import matplotlib.pyplot as plt
import helper
import preprocessor
import pandas as pd


st.sidebar.title("WhatsApp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Upload WhatsApp chat (.txt) file")

if uploaded_file is not None:
    data = uploaded_file.getvalue().decode("utf-8")
    df = preprocess(data)

    # st.title("Chat Overview")
    # st.dataframe(df)

    # fetch unique user

    user_list = df['user'].unique().tolist()
    user_list.insert(0, 'Overall')

    selected_user = st.sidebar.selectbox(
        "Show analysis for",
        user_list
    )

    if st.sidebar.button("Show Analysis"):
        # Stat Area
        num_messages, words, num_media_messages, no_links = helper.fetch_stats(selected_user, df)
        st.title("Top Statistics")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            # st.metric("Total Messages", num_messages)
            st.header("Total Msg")
            st.title(num_messages)
        with col2:
            st.header("Total words")
            st.title(words)
        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)
        with col4:
            st.header("Shared Links")
            st.title(no_links)

        # monthly timeline
        st.title("Monthly Timeline")
        timeline=helper.monthly_timeline(selected_user, df)
        fig, ax =plt.subplots()
        ax.plot(timeline['time'], timeline['message'])
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # daily timeline
        st.title("Daily Timeline")
        daily_timeline=helper.daily_timeline(selected_user, df)
        fig, ax =plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # Activity map
        st.title("Activity Map")
        col1,col2=st.columns(2)

        with col1:
            st.header("Most busy day")
            busy_day= helper.week_activity_map(selected_user,df)
            fig, ax =plt.subplots()
            ax.bar(busy_day.index,busy_day.values)
            st.pyplot(fig)

        with col2:
            st.header("Most busy month")
            busy_month= helper.month_activity_map(selected_user,df)
            fig, ax =plt.subplots()
            ax.bar(busy_month.index,busy_month.values,color='orange')
            st.pyplot(fig)


        # finding the busiest users in the group (Group level)
        if selected_user == 'Overall':
            st.title('Most Busy user')
            x, new_df= helper.most_busy_users(df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)
            with col1:
                ax.bar(x.index, x.values ,color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)
        # Wordcloud
        st.title("WordCloud")
        df_wc=helper.create_wordcloud(selected_user,df)
        fig,ax=plt.subplots()
        plt.imshow(df_wc)
        st.pyplot(fig)

        #emoji analysis

        # # emoji_df=helper.emoji_helper(selected_user,df)
        # emoji_df = helper.emoji_helper(selected_user, df)
        #
        # st.dataframe(emoji_df)
        #
        # st.subheader("Emoji Distribution")
        #
        # if not emoji_df.empty:
        #
        #     top_emojis = emoji_df.head(10)   # top 10 emojis
        #
        #     fig, ax = plt.subplots()
        #     ax.pie(
        #         top_emojis['count'],
        #         labels=top_emojis['emoji'],
        #         autopct='%1.1f%%',
        #         startangle=90
        #     )
        #     ax.axis('equal')  # makes pie circle
        #
        #     st.pyplot(fig)
        #
        # else:
        #     st.write("No emojis found.")
        emoji_df = helper.emoji_helper(selected_user, df)

        st.subheader("Emoji Analysis")

        if not emoji_df.empty:

            # create two columns
            col1, col2 = st.columns(2)

            # 🔹 LEFT SIDE → TABLE
            with col1:
                st.subheader("Emoji Table")
                st.dataframe(emoji_df)

            # 🔹 RIGHT SIDE → PIE CHART
            with col2:
                st.subheader("Emoji Distribution")

                top_emojis = emoji_df.head(10)

                fig, ax = plt.subplots(figsize=(5, 5))
                ax.pie(
                    top_emojis['count'],
                    labels=top_emojis['emoji'],
                    autopct='%1.1f%%',
                    startangle=90
                )
                ax.axis('equal')

                st.pyplot(fig)

        else:
            st.write("❌ No emojis found.")

