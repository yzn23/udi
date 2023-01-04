import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

CITY_DATA = {'1': 'chicago.csv',
             '2': 'new_york_city.csv',
             '3': 'washington.csv'}

#here we create check input 

def check_in(input_str, input_ty):
    """
    check the validity of user input.
    input_str: is the input of the user
    input_ty: the type of input: 1 = city, 2 = month, 3 = day
    """
    while True:
        input_r = input(input_str).lower()
        try:
            if input_r in CITY_DATA and input_ty == 1:
                break
            elif input_r in ['january', 'february', 'march', 'april', 'may', 'june', 'all'] and input_ty == 2:
                break
            elif input_r in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
                             'all'] and input_ty == 3:
                break
            else:
                if input_ty == 1:
                    print("Sorry, your input should be: (1) for chicago (2) for new york city or (3) for washington")
                if input_ty == 2:
                    print("Sorry, your input should be: month name or all")
                if input_ty == 3:
                    print("Sorry, your input should be: day name  or all")
        except ValueError:
            print("Sorry, your input is not correct")
    return input_r


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


    city = check_in('Which city you want: (1) chicago, (2) new york city, (3) washington', 1)

# TO DO: get user input for month (all, january, february, ... , june)
    month = check_in("Which Month (all or month name)?", 2)

# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = check_in("Which day? (all or day name)", 3)
    print('-' * 40)
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


# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

# convert the Start Time column to datetime
    df['Start Time'] =pd.to_datetime(df['Start Time'])

# extract month, days, hour from Start Time
    df['month']= df['Start Time'].dt.month
    df['dayweek']= df['Start Time'].dt.day_name()
    df['hour']=df['Start Time'].dt.time
# filter by month if applicable
    if month != 'all':
# use the index of the months list to get the corresponding int
     months= ['january', 'february', 'march', 'april', 'may', 'june']
     month = months.index(month) + 1

    # filter by month to create the new dataframe
     df = df[df['month'] == month]

# filter by day of week if applicable
    if day != 'all':
 # filter by day of week to create the new dataframe
     df = df[df['days'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

# TO DO: display the most common month
    pop_mon=df['month'].mode() [0]
    print('the most common month is: ',pop_mon)
# TO DO: display the most common day of week
    pop_dw=df['dayweek'].mode() [0]
    print('the most common day of week is: ', pop_dw)
# TO DO: display the most common start hour
    pop_hu = df['hour'].mode()[0]
    print('the most common start hour is: ', pop_hu)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_sts = df['Start Station'].mode()[0]

    print('The Most commonly Start Station: ', pop_sts)


# TO DO: display most commonly used end station
    pop_end = df['End Station'].mode()[0]

    print('The Most commonly End Station:', pop_end)

# TO DO: display most frequent combination of start station and end station trip
    gou_fi = df.groupby(['Start Station', 'End Station'])
    pop_cost = gou_fi.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of Start Station and End Station trip:\n', pop_cost)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_tr = df['Trip Duration'].sum()

    print('Total Travel Time:', tot_tr)
    # TO DO: display mean travel time
    trav= df['Trip Duration'].mean()

    print('Mean Travel Time:', trav)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    if city != 'washington':
    # TO DO: Display counts of gender
     print('Gender Stats:')
     print(df['Gender'].value_counts())
    # TO DO: Display earliest, most recent, and most common year of birth
     print('Birth Year Stats is:')
     most_year = df['Birth Year'].mode()[0]
     print('Most Common Year is:', most_year)
     mo_year = df['Birth Year'].max()
     print('Most Recent Year:', mo_year)
     er_year = df['Birth Year'].min()
     print('Earliest Year is:', er_year)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
#clean data
def cleen(df):
    ch_col = input("do you want filter the columns (YES or NO): ").lower()
    if ch_col != 'no':
        col = int(input('How many columns do you want to display (YES or NO): '))
        print(df.head(col))
    else:
        if ch_col != 'yes' or 'no':
            print('enter (yes) or (no)')
    dro = input("do you want drop NaN value (YES or NO): ").lower()
    if dro != "no":
        red = int(input("enter the condition for drop NaN value (how many Nan value in the row): "))
        df.dropna(thresh=red)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        clen=input('do you want cleen data?: ').lower()
        if clen!='no':
         cleen(df)
        print(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
    main()
