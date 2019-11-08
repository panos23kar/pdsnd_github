import time
import pandas as pd
import numpy as np
import datetime as dt

# dictionary through which we access the data files
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def city_message():
    """'Forms and returns the message that prompts the user to type the city's name"""

    msg = "\nPlease type the city that you are interested in:\n" \
          "1)Chicago\n2)New York city\n3)Washington\nType the city name here:"
    return msg


def filter_city(city_input):
    """"
    Retrieves the user's input for the city and checks
    if he/she has typed the name of the city correctly

        Args:
        (str) city_input - user's input for city
        Returns:
        (str) city_input - name of the city to analyze
    """
    while (city_input.lower() != 'chicago' and city_input.lower() != 'new york city'
           and city_input.lower() != 'washington'):
        print('\nYou have typed -->', city_input, '<-- which is not a valid city name')
        city_input = input(city_message()).strip()
    return city_input


def month_message():
    """'Forms and returns the message that prompts the user to type the month's name"""

    msg = "\nPlease type the month that you are interested in:\n" \
          "1)January\n2)February\n3)March\n4)April\n5)May\n6)June\n7)July\n8)August\n9)September" \
          "\n10)October\n11)November\n12)December\n13)All (to apply no month filter)" \
          "\nType the month's name here: "
    return msg


def filter_month(month_input):
    """"
    Retrieves the user's input for the month and checks
    if he/she has typed the name of the month correctly

        Args:
        (str) month_input - user's input for month
        Returns:
        (str) month_input - name of the month to analyze
    """
    while (month_input.lower() != 'january' and month_input.lower() != 'february'
           and month_input.lower() != 'march' and month_input.lower() != 'april'
           and month_input.lower() != 'may' and month_input.lower() != 'june'
           and month_input.lower() != 'july' and month_input.lower() != 'august'
           and month_input.lower() != 'september' and month_input.lower() != 'october'
           and month_input.lower() != 'november' and month_input.lower() != 'december'
           and month_input.lower() != 'all'):
        print('\nYou have typed -->', month_input, '<-- which is not a valid month name')
        month_input = input(month_message()).strip()
    return month_input


def day_message():
    """'Forms and returns the message that prompts the user to type the day's name"""

    msg = "\nPlease type the day that you are interested in:\n" \
          "1)Monday\n2)Tuesday\n3)Wednesday\n4)Thursday\n5)Friday\n" \
          "6)Saturday\n7)Sunday\n8)All (to apply no day filter)\nType the day name here:"
    return msg


def filter_day(day_input):
    """"
    Retrieves the user's input for the day and checks
    if he/she has typed it correctly

        Args:
        (str) day_input - user's input for day
        Returns:
        (str) day_input - name of the day to analyze
    """
    while (day_input.lower() != 'monday' and day_input.lower() != 'tuesday'
           and day_input.lower() != 'wednesday' and day_input.lower() != 'thursday'
           and day_input.lower() != 'friday' and day_input.lower() != 'saturday'
           and day_input.lower() != 'sunday' and day_input.lower() != 'all'):
        print('\nYou have typed -->', day_input, '<-- which is not a valid day name')
        day_input = input(day_message()).strip()
    return day_input


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = filter_city(input(city_message()).strip())

    # get user input for month (all, january, february, ... , june)
    month = filter_month(input(month_message()).strip())

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = filter_day(input(day_message()).strip())

    print('-' * 40)
    return city, month, day


def month_day_hour_column(df):
    """"
    Transforms the 'Start Time' column into datetime column type.
    Creates a column which hosts the month
    Creates a column which hosts the day
    Creates a column which hosts the hour

    Args:
        (Pandas DataFrame) df - name of the dataframe which was created by loading the corresponding .csv file
    Returns:
        (Pandas DataFrame) df - contains city the received data frame enriched with month, day, hour columns
    """
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from the Start Time column to create an month column
    # The month as January=1, December=12
    df['month'] = df['Start Time'].dt.month

    # extract hour from the Start Time column to create an day column
    # The day of the week with Monday=0, Sunday=6
    df['day'] = df['Start Time'].dt.weekday

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    return df


def month_matcher(month):
    """"
    Matches the input of the user with a month

    Args:
        (str) month - input of the user for month
    Returns:
        (tuple) Returns the index of a month and mont's name (capitalized first letter)
    """
    if month.lower() == 'january' or month == '1':
        return 1, 'January'
    elif month.lower() == 'february' or month == '2''':
        return 2, 'February'
    elif month.lower() == 'march' or month == '3':
        return 3, 'March'
    elif month.lower() == 'april' or month == '4':
        return 4, 'April'
    elif month.lower() == 'may' or month == '5':
        return 5, 'May'
    elif month.lower() == 'june' or month == '6':
        return 6, 'June'
    elif month.lower() == 'july' or month == '7':
        return 7, 'July'
    elif month.lower() == 'august' or month == '8':
        return 8, 'August'
    elif month.lower() == 'september' or month == '9':
        return 9, 'September'
    elif month.lower() == 'october' or month == '10':
        return 10, 'October'
    elif month.lower() == 'november' or month == '11':
        return 11, 'November'
    elif month.lower() == 'december' or month == '12':
        return 12, 'December'


def day_matcher(day):
    if day.lower() == 'monday' or day == '0':
        return 0, 'Monday'
    elif day.lower() == 'tuesday' or day == '1':
        return 1, 'Tuesday'
    elif day.lower() == 'wednesday' or day == '2':
        return 2, 'Wednesday'
    elif day.lower() == 'thursday' or day == '3':
        return 3, 'Thursday'
    elif day.lower() == 'friday' or day == '4':
        return 4, 'Friday'
    elif day.lower() == 'saturday' or day == '5':
        return 5, 'Saturday'
    elif day.lower() == 'sunday' or day == '6':
        return 6, 'Sunday'


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city.lower()])
    df = month_day_hour_column(df)
    if month.lower() == 'all' and day.lower() == 'all':
        return df
    else:
        # same data frame enriched with moth, day, hour columns
        if month.lower() != 'all' and day.lower() != 'all':
            # obtain only the rows of the specified month and day
            month = month_matcher(month)[0]
            day = day_matcher(day)[0]
            df = df[df['month'] == month]
            df = df[df['day'] == day]
        elif month.lower() != 'all':
            # obtain only the rows of the specified day
            month = month_matcher(month)[0]
            df = df[df['month'] == month]
        else:
            # obtain only the rows of the specified month
            day = day_matcher(day)[0]
            df = df[df['day'] == day]

        return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month

    # group dataframe by month and count how many rows correspond to each of them.
    # Then I sort them in descending order and assign them in a new data frame
    month_df = df.groupby('month').count().sort_values('Unnamed: 0', ascending=False)

    # extract the 'index' of the month and transform it back to something human readable
    # extract the number of rows that correspond to this month
    month, number_of_rows = month_matcher(str(month_df.index[0]))[1], month_df.iloc[0][0]

    print('The most common month is', month, 'with', number_of_rows, 'rentings.')

    # display the most common day of week
    day_df = df.groupby('day').count().sort_values('Unnamed: 0', ascending=False)
    day, number_of_rows = day_matcher(str(day_df.index[0]))[1], day_df.iloc[0][0]
    print('The most common day is', day, 'with', number_of_rows, 'rentings.')

    # display the most common start hour
    hour_df = df.groupby('hour').count().sort_values('Unnamed: 0', ascending=False)
    hour, number_of_rows = hour_df.index[0], hour_df.iloc[0][0]
    print('The most common start hour is', hour, 'with', number_of_rows, 'rentings.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station_df = df.groupby('Start Station').count().sort_values('Unnamed: 0', ascending=False)
    start_station, number_of_rows = start_station_df.index[0], start_station_df.iloc[0][0]
    print('The most commonly used start station is', start_station, 'with', number_of_rows, 'appearances')

    # display most commonly used end station
    end_station_df = df.groupby('End Station').count().sort_values('Unnamed: 0', ascending=False)
    end_station, number_of_rows = end_station_df.index[0], end_station_df.iloc[0][0]
    print('The most commonly used end station is', end_station, 'with', number_of_rows, 'appearances')

    # display most frequent combination of start station and end station trip
    start_end_station_df = df.groupby(['Start Station', 'End Station']).count() \
        .sort_values('Unnamed: 0', ascending=False)
    start_end_station = start_end_station_df.index[0][0] + ' - ' + start_end_station_df.index[0][1]
    number_of_rows = start_end_station_df.iloc[0][0]
    print('The most frequent combination of start station and end station trip is:', start_end_station,
          'with', number_of_rows, 'appearances')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # convert the End Time column to datetime
    df['End Time'] = pd.to_datetime(df['End Time'])
    # calculate the duration of each trip by subtracting the start time from the end time
    df['Trip Duration'] = df['End Time'] - df['Start Time']

    # display total travel time
    # calculate the total travel time using the sum() function from NumPy module
    total_travel_time = np.sum(df['Trip Duration'])
    print('The total travel time for the specified time period is ', total_travel_time)

    # display mean travel time
    # calculate the mean travel time using the mean() function from NumPy module
    mean_travel_time = np.mean(df['Trip Duration'])
    # datetime modules formats the time in a better way, no need for days to be displayed for average time of bike trips
    time_delta = dt.timedelta(seconds=mean_travel_time.seconds)
    print('The mean travel time for the specified time period is ', time_delta)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    # Checks if 'User Type' column is part of the dataframe
    if 'User Type' in df:
        user_type_df = df.groupby('User Type').count().sort_values('Unnamed: 0', ascending=False)
        # string which holds the 'array' to be presented to the users
        user_type_array = user_type_df['Unnamed: 0'].to_string()
        print(f'These are the types of users and the number of appearances:\n\n{user_type_array}')
    else:
        print('This dataset does not include information about the user types!')

    # Display counts of gender
    # Checks if 'Gender' column is part of the dataframe
    if 'Gender' in df:
        gender_df = df.groupby('Gender').count().sort_values('Unnamed: 0', ascending=False)
        # string which holds the 'array' to be presented to the users
        gender_array = gender_df['Unnamed: 0'].to_string()
        print(f'\nThese are the genders and the number of appearances:\n\n{gender_array}\n\n')
    else:
        print('\nThis dataset does not include information about genders!\n')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest = np.min(df['Birth Year'])
        print('The earliest year of birth is', int(earliest))

        most_recent = np.max(df['Birth Year'])
        print('The most recent year of birth is', int(most_recent))

        year_df = df.groupby('Birth Year').count().sort_values('Unnamed: 0', ascending=False)
        most_common_year, number_of_rows = year_df.index[0], year_df.iloc[0][0]
        print('The most common year of birth is', int(most_common_year), 'with', number_of_rows, 'appearances')
    else:
        print('This dataset does not include information about birth year!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def welcome_message():
    """"Displays a welcome message to the user"""
    print('\nHello Dear user!\nIt\'s time to obtain some cycling insights!\n'
          'You will experience an interactive python bike journey\nHave fun!!')


def expose_raw_rows(df):
    """"
    Exposes raw data to the user after it has asked him/her if he/she wants so
     Args:
            (Pandas DataFrame) df - name of the dataframe which was created by loading the corresponding .csv file
    """

    want_to_see = True
    rows_counter = 0
    while want_to_see:
        user_willing = input('\nWould you like to see 5 (more) rows of the dataset? (Type Yes/No)\n').strip()
        if user_willing.lower() == 'yes':
            print(df.iloc[rows_counter:rows_counter + 5].to_string())
            rows_counter += 5
        elif user_willing.lower() == 'no':
            want_to_see = False


def main():
    # welcomes the user
    welcome_message()

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        expose_raw_rows(df)

        restart = input('\nWould you like to restart? (Type Yes/No)\n').strip()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
