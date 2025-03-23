import re
import pandas as pd
def preprocess(data):
    pattern = r'\d{1,2}/\d{1,2}/\d{2},\s\d{1,2}:\d{2}\s?(?:am|pm)\s-\s'

    messages = re.split(pattern, data)[1:]  # Extract messages after splitting by pattern
    dates = re.findall(pattern, data)  # Extract all date-time stamps

    from datetime import datetime  # Import the datetime module

    timestamps_24hr = []
    for ts in dates:
        # Extract the date and time parts
        dt_part, time_part = ts.split(", ")
        # Remove trailing separator and any narrow no-break spaces
        time_part = time_part.replace(" - ", "").replace("\u202f", "")

        # Convert to 24-hour format
        dt_obj = datetime.strptime(f"{dt_part} {time_part}", "%d/%m/%y %I:%M%p")
        timestamps_24hr.append(dt_obj.strftime("%d/%m/%y, %H:%M -"))

    df = pd.DataFrame({'user_message': messages, 'message_date': timestamps_24hr})
    # convert message date date_type
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %H:%M -')
    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    messages_list = []  # Renamed to avoid conflict with loop variable

    for message in df['user_message']:  # Renamed loop variable
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            messages_list.append(entry[2])  # Append to the list
        else:
            users.append('group_notification')
            messages_list.append(entry[0])  # Append to the list

    df['user'] = users
    df['message'] = messages_list  # Assign the list to the DataFrame column

    # splitting the date itself in seprate columns each for yera,month,day
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['month_num'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    return df