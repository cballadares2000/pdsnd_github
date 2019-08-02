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
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['Chicago', 'New York', 'Washington']
    city = " "
    while city not in (cities) :
        print('Please choose one of the following cities \n')
        city = input(' Chicago \n New York \n Washington \n\n').title()
    print ('You have chosen ' + city)


    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['All', 'January', 'February', 'March', 'April', 'May', 'June']
    month = " "
    while month not in (months):
        print('Please choose one of the following months \n')
        month = input(' All \n January \n February \n March \n April \n May \n June \n\n').title()
        print ('You have chosen ' + month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['All','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    day = " "
    while day not in (days):
        print('Please choose one of the following days \n')
        day = input(' All \n Monday \n Tuesday \n Wednesday \n Thursday \n Friday \n Saturday \n Sunday \n\n').title()
        print ('You have chosen ' + day)

    print('-'*40)
    return city, month, day


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
    # Filter  Names of cities, months and days
    if city == 'Chicago':
        city = 'chicago'
    elif city == 'New York':
        city = 'new york city'
    else:
        city = 'washington'

    month = month.lower()
    day = day.lower()

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def cities(city):
    #Display cities data
    if city == 'Chicago':
        print('Chicago with a population of  2,705,594 is the third most populous city in the United States.')
    elif city == 'New York':
        print('New York with a population of  8,398,748 is the  most populous city in the United States.')
    else:
        print('Washington or D.C is the capital of the United States, more than 20 millions tourists visit the city annualy')

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    common_months =['January','February','March','Abril','May','June']
    print('Most common month:', common_months[common_month-1])

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day:', common_day)

    # TO DO: display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour
    common_hour = df['hour'].mode()[0]
    print('Most common hour:', common_hour,' hours')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_start_station = df['Start Station'].mode()[0]
    print('Most commonly Start Station:', commonly_start_station)

    # TO DO: display most commonly used end station
    commonly_end_station = df['End Station'].mode()[0]
    print('Most commonly End Station:', commonly_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    # Create new column Stations ='Start Station'+'End Station'
    df['Stations'] = df['Start Station'] + " to " + df['End Station']
    commonly_combination_of_stations = df['Stations'].mode()[0]
    print('Most commonly combination of stations:', commonly_combination_of_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time is:', round (total_travel_time/3600),' hours')

    # TO DO: display mean travel time
    median_travel_time = df['Trip Duration'].median()
    print('Median Travel Time is:', round (median_travel_time/60),' minutes')

    # TO DO: display shortest travel time
    shortest_travel_time = df['Trip Duration'].min()
    print('Shortest Travel Time is:', round (shortest_travel_time/60),' minutes')

    # TO DO: display longuest travel time
    longuest_travel_time = df['Trip Duration'].max()
    print('Longuest Travel Time is:', round (longuest_travel_time/3600),' hours')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types.to_string())

    # TO DO: Display counts of gender
    if city == 'Washington':
        print(' We do not have "Gender" information for this city')
    else:
        user_types = df['Gender'].value_counts()
        print(user_types.to_string())

    # TO DO: Display earliest, most recent, and most common year of birth
    if city == 'Washington':
        print(' We do not have "Year of birth" information for this city')
    else:
        # display Earliest Birth year
        earlier_birth_year = df['Birth Year'].min()
        print('Earliest Birth year is:', int(earlier_birth_year))

        # display Most Recent Birth year
        most_recent_birth_year = df['Birth Year'].max()
        print('Most Recent Birth year is:', int(most_recent_birth_year))

        # display the most common Birth year
        most_common_birth_year = df['Birth Year'].median()
        print('Most common Birth year is:', int(most_common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    answer = 'yes'
    x = 0
    while answer == 'yes':
        answer = input('\nWould you like to see 5 lines of Raw Data? Enter yes or no.\n').lower()
        if answer == 'yes':
            x= (x + 5)
            print (df.iloc[x-5:x])

    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        cities(city)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print (' Thanks for using this program, Good bye')
            break


if __name__ == "__main__":
    main()
