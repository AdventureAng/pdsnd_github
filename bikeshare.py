import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv', 'Chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv', 'New York City': 'new_york_city.csv', 'New York': 'new_york_city.csv', 'new york': 'new_york_city.csv',
              'washington': 'washington.csv', 'Washington': 'washington.csv' }

def get_input(input_str,input_type):
    """
    get the validity of user input.
    input_str: is the input of the user
    input_type: is the type of input: 1 = city, 2 = month, 3 = day
    """
    while True:
        input_read=input(input_str)
        try:
            if input_read in ['chicago','new york city','washington','Chicago','New York','New York City','new york','Washington'] and input_type == 1:
                break
            elif input_read in ['january', 'february', 'march', 'april', 'may', 'june','all','January', 'February', 'March', 'April', 'May', 'June','All'] and input_type == 2:
                break
            elif input_read in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','All'] and input_type == 3:
                break
            else:
                if input_type == 1:
                    print("Sorry, your input should be: chicago, new york city, or washington. Please try again")
                if input_type == 2:
                    print("Sorry, your input should be: january, february, march, april, may, june or all. Please try again.")
                if input_type == 3:
                    print("Sorry, your input should be: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all. Please try again.")
        except ValueError:
            print("Sorry, your input is wrong")
    return input_read

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = get_input('Please enter which city you would like to explore. chicago, new york city, or washington? ',1)
    # get user input for month (all, january, february, ... , june)
    month = get_input('Next, which month would you like to look at? Please enter a month from january to june or type all to see all months. \n(e.g. all, january, february, march, april, may, june) ',2) 
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = get_input('And finally, what day of the week would you like to look at?  Please enter a day from monday to sunday or you can type \'all\' to see all days. \n(e.g. all, monday, tuesday, wednesday, thursday, friday, saturday, sunday) \n>  ',3) 
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month is :", most_common_month)

    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("The most common day is :", most_common_day)

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is :", most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    
    print('The most commonly used start station is:', most_common_start_station)


    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    
    print('The most commonly used end station is:', most_common_end_station)

    # display most frequent combination of start station and end station trip
    df['combination']=df['Start Station']+" "+"to"+" "+ df ['End Station']
    frequent_combination= df['combination'].mode()[0]
    
    print('The most commonly used combination of start and end station is:', frequent_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    
    print('Total travel time:', total_travel_time)                                    


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    
    print('Mean travel time:', mean_travel_time)                                     

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of user types:')
    print(df['User Type'].value_counts())                                        
    

    # Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('Count of gender is:', gender)
    else:
        print('There is no gender information.')


    # Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest_birth = df['Birth_Year'].min()
        print('The ealiest year of birth is:', earliest_birth)
        most_recent_birth = df['Birth_Year'].max()
        print('The most recent birth year is:', most_recent_birth)
        most_common_birth = df['Birth Year'].mode()[0]
        print('The most common birth year is:', most_common_birth)
    else:
        print('There is no birth year information.')

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
    
