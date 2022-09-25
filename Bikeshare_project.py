import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "none" to apply no month filter
        (str) day - name of the day of week to filter by, or "none" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')

    while True:
        try:
            # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
            city = str(input("\nWould you like to see data for Chicago, New York City or Washington? \n" ).lower())
            if city in ['chicago', 'new york city', 'washington']:
                break
            else:
                print("That\'s not a vallid input!")
        except:
            print("That\'s not a vallid input!")

    while True:
        try:
            #check if the user want to filter or not
            filter = str(input("\nWould you like to filter the data by month, day, both or not at all? Please type \"not at all\" for no filter. \n" ).lower())
            if filter in ['month', 'day', 'both', 'not at all']:
                break
            else:
                print("That\'s not a vallid input!")
        except:
            print("That\'s not a vallid input!")

    #test user input to check if they chose to filter or not
    if filter == 'not at all':
        month = 'none'
        day = 'none'

    elif filter == 'month':
        while True:
            try:
                # TO DO: get user input for month (january, february, ... june)
                month = str(input("\nWhich month? January, February, March, April, May or June? Please type full month name. \n" ).lower())
                day = 'none'
                if month in ['january', 'february', 'march', 'april', 'may', 'june', 'july']:
                    break
                else:
                    print("That\'s not a vallid input!")
            except:
                print("That\'s not a vallid input!")

    elif filter == 'day':
        while True:
            try:
                # TO DO: get user input for day of week (monday, tuesday, ... sunday)
                day = str(input("\nWhich day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? Please type full day name. \n" ).lower())
                month = 'none'
                if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                    break
                else:
                    print("That\'s not a vallid input!")
            except:
                print("That\'s not a vallid input!")

    elif filter == 'both':
        while True:
            try:
                # TO DO: get user input for month (january, february, ... june)
                month = str(input("\nWhich month? January, February, March, April, May or June? Please type full month name. \n" ).lower())
                if month in ['january', 'february', 'march', 'april', 'may', 'june', 'july']:
                    break
                else:
                    print("That\'s not a vallid input!")
            except:
                print("That\'s not a vallid input!")

        while True:
            try:
                # TO DO: get user input for day of week (monday, tuesday, ... sunday)
                day = str(input("\nWhich day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? Please type full day name. \n" ).lower())
                if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                    break
                else:
                    print("That\'s not a vallid input!")
            except:
                print("That\'s not a vallid input!")

    print('-'*100)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "none" to apply no month filter
        (str) day - name of the day of week to filter by, or "none" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'none':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'none':
        day = day.title()
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].value_counts().idxmax()
    print('Most Popular Month:', popular_month,'\n')

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].value_counts().idxmax()
    print('Most Popular Day Of Week:', popular_day,'\n')

    # TO DO: display the most common start hour
    popular_hour = df['hour'].value_counts().idxmax()
    print('Most Popular Start Hour:', popular_hour,'\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('Most Common Used Start Station:', common_start_station,'\n')

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print('Most Common Used End Station:', common_end_station,'\n')

    # TO DO: display most frequent combination of start station and end station trip
    cmn_start = df[df['Start Station']==df['Start Station'].mode()[0]]
    cmn_end = cmn_start[cmn_start['End Station']==cmn_start['End Station'].mode()[0]]
    x = cmn_end['Start Station'].mode()[0]
    y = cmn_end['End Station'].mode()[0]
    print('Most Common Trip Starts At \"{}\", And Ends At \"{}\".'.format(x, y),'\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Trip Duration:', total_travel_time,'seconds\n')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Average Trip Duration:', mean_travel_time,'seconds\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def user_stats_types(df):
    """Displays statistics about bikeshare user types."""

    print('\nCalculating User Types...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('There Are Two Types Of Users:\n', user_types, '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of gender
    gender_count = df['Gender'].value_counts()
    print('Those Users Break Down To:\n', gender_count, '\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest = df['Birth Year'].min()
    most_recent = df['Birth Year'].max()
    most_common_birth_year = df['Birth Year'].mode()[0]
    print('Earliest Birth Year Is: ', earliest, '\nMost Recent Birth Year Is: ',most_recent, '\nMost Recent Birth Year Is: ', most_common_birth_year,'\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def display_data(df):
    while True:
        try:
            q1 = input('Would you like to display the first 5 rows of data?: (y/n)\n')
            if q1 in ['y', 'n']:
                break
            else:
                print("\nPlease Enter valid value, y for yes , n for no!\n")
        except:
            print("\nPlease Enter valid value, y for yes , n for no!\n")
    if q1 == 'y':
        start_row = 0
        end_row = 5

        while True and end_row <= df['Start Time'].count():
            print(df.iloc[start_row:end_row])
            while True:
                try:
                    q2 = input('\nWould you like to display 5 more rows?: (y/n)\n')
                    if q2 in ['y', 'n']:
                        break
                    else:
                        print("\nPlease Enter valid value, y for yes , n for no!\n")
                except:
                    print("\nPlease Enter valid value, y for yes , n for no!\n")

            if q2 == 'n':
                break
            else:
                start_row += 5
                end_row += 5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats_types(df)

        if city != 'washington':
            user_stats(df)
        else:
            print('There Are No Available Age And Gender Data On Washington!\n')

        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
