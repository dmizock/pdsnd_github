import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

city_names = ['chicago', 'new york city', 'washington']
month_names = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
day_names = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

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
  while True:
    city = input('Please select one of the following cities: Chicago, New York City or Washington.\n').lower()
    if city not in city_names:
        print('Invalid entry, please enter a valid city.')
    else:
        break
    # TO DO: get user input for month (all, january, february, ... , june)
while True:
    month = input('Please select one month from the following or all months: January, February, March, April, May, June, all.\n').lower()
    if month not in month_names:
        print('Invalid month entered, please enter a valid month')
    else:
        break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
while True:
    day = input('Please select a day of the week or all days: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, all.\n').lower()
    if day not in day_names:
        print('Invalid day entered, please enter a valid day')
    else:
        break
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

    # Load data into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract all of month, day and hour from Start Time to make new columns
    df['month_names'] = df['Start Time'].dt.month
    df['day_names'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour

    # filter by month / day of week and create new dataframe using filters
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        day_name = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        day = day_name.index(day) + 1
        df = df[df['day_names'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('Most common month:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_names'].mode()[0]
    print('Most common day of the week:', common_day)


    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most common hour of the day:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_staion = df['Start Station'].mode().values[0]
    print('Most popular used start station is:', start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode().values[0]
    print('Most popular used end station is:', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_roundtrip = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('The most frequent start to end trip is     \n{}'.format(start_station, end_station, popular_roundtrip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    print('Total travel duration in seconds is:', total_duration)

    # TO DO: display mean travel time
    avg_trip_duration = df['Trip Duration'].mean()
    print('Average trip duration in seconds is:', avg_trip_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Number of user types:', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
    print('Number of users of each gender (if applicable):', gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        oldest = df['Birth Year'].min()
        youngest = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
    print('The oldest birth year is:', oldest)
    print('The youngest birth year is:', youngest)
    print('The most common birth year is:', most_common)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
