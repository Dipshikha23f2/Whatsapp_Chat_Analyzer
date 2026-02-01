# def preprocess(data):
#             # 1. regex pattern for WhatsApp date-time
#     pattern = r'(\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s?(?:am|pm)?)\s[-–]\s'
#
#     # 2. split data into parts
#     parts = re.split(pattern, data)
#
#     # 3. extract dates and raw messages
#     dates = parts[1::2]
#     raw_messages = parts[2::2]
#
#     # 4. create dataframe
#     df = pd.DataFrame({
#         'date': pd.to_datetime(dates, format="%d/%m/%y, %I:%M %p", errors='coerce'),
#         'raw_message': raw_messages
#     })
#
#     # 5. separate users and messages
#     users = []
#     messages = []
#
#     for msg in df['raw_message']:
#         entry = re.split(r'^(.+?):\s', msg, maxsplit=1)
#
#         if len(entry) > 1:
#             users.append(entry[1].strip())
#             messages.append(entry[2])
#         else:
#             users.append('group_notification')
#             messages.append(msg)
#
#     df['user'] = users
#     df['message'] = messages
#     df.drop(columns=['raw_message'], inplace=True)
#
#     # 6. add date features
#     df['year'] = df['date'].dt.year
#     df['month'] = df['date'].dt.month
#     df['day'] = df['date'].dt.day
#     df['hour'] = df['date'].dt.hour
#
#     # 7. remove group notifications (optional but recommended)
#     df = df[df['user'] != 'group_notification']
#
#     return df
#
#
#
#


import re
import pandas as pd

def preprocess(data):
    pattern = r'(\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s?(?:am|pm)?)\s[-–]\s'
    parts = re.split(pattern, data)

    dates = parts[1::2]
    messages = parts[2::2]

    df = pd.DataFrame({
        'date': pd.to_datetime(dates, format="%d/%m/%y, %I:%M %p", errors='coerce'),
        'raw_message': messages
    })

    users = []
    texts = []

    for msg in df['raw_message']:
        entry = re.split(r'^(.+?):\s', msg, maxsplit=1)
        if len(entry) > 1:
            users.append(entry[1])
            texts.append(entry[2])
        else:
            users.append('group_notification')
            texts.append(msg)

    df['user'] = users
    df['message'] = texts
    df.drop(columns=['raw_message'], inplace=True)
    df['only_date'] = df['date'].dt.date
    df['day_name']=df['date'].dt.day_name()
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour

    df = df[df['user'] != 'group_notification']

    return df
