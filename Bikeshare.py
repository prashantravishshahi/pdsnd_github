import time
import pandas as pd
import User_Input as ui

CITY_DATA = { 'chi': 'chicago.csv',
              'new': 'new_york_city.csv',
              'was': 'washington.csv' }


#definition of load data function :- This function is used to load data once the user confirms the month and city
def load_data(city, month, day):
    # Step to load the data file in the dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime using panda function
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    # filter the data by month (if applicable)
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        # filter by month to create a new dataframe
        df = df[df['month'] == month]
    # filter the data by day of week (if applicable)
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]
    return df

#definition of most common month function
def most_common_month(df):
    df['month'] = df['Start Time'].dt.month_name()
    popular_month=df['month'].mode()[0]
    print('Most Popular Start Month:',popular_month)

#definition of most common day function
def most_common_day(df):
    df['day'] = df['Start Time'].dt.day_name()
    popular_day=df['day'].mode()[0]
    print('Most Popular Day:',popular_day)

#definition of most common start hour function
def most_common_start_hour(df):
    df['hour'] = df['Start Time'].dt.hour
    popular_hour=df['hour'].mode()[0]
    print('Most Popular Start Hour:',popular_hour)

#definition of most frequent times of travel function
def time_stats(df, month, day):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    if(month=='all' and day=='all'):
        most_common_month(df)
        most_common_day(df)
        most_common_start_hour(df)
    elif(month!='all' and day=='all'):
        most_common_day(df)
        most_common_start_hour(df)

    elif(month=='all' and day!='all'):
        most_common_start_hour(df)
        most_common_month(df)
    elif(month!='all'and day!='all'):
        most_common_start_hour(df)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)

#definition of the most popular stations and trip function
def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print('Most Popular Start Station:',popular_start_station)
    # display most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    print('Most Popular End Station:',popular_end_station)
    # display most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station'].map(str) + '&' + df['End Station']
    popular_start_end = df['Start End'].value_counts().idxmax()
    print('Most Popular most frequent combination of start station and end station: ',popular_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)
#definition of trip duration stats function
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('Total Travel Time:',total_travel_time)
    # display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('Mean Travel Time:',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)
#definition of the statistics on bikeshare users function : This function takes the most of the time to execute.
def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    # print value counts for each user type
    user_types = df['User Type'].value_counts()
    print('User Type:\n',user_types)
    if city=='new' or city=='chi':
          # Display counts of gender
          gender_types = df['Gender'].value_counts()
          print('Gender:\n',gender_types)
          # Display earliest, most recent, and most common year of birth
          earliest_year_birth = int(df['Birth Year'].min())
          print('Earliest Birth Year: ',earliest_year_birth)
          most_recent_year_birth =int(df['Birth Year'].max())
          print('Most Recent Birth Year: ',most_recent_year_birth)
          most_common_year_birth = int(df['Birth Year'].mode()[0])
          print('Most Common Birth year: ',most_common_year_birth)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)
def statistics():
    while True:
        city, month, day = ui.get_filters()
        load_data(city, month, day)
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        check='y'
        start=0
        end=10
        check=input('\nWould you like to have a look on each trip details? \nType y or n \ny:yes\nn:no\n')
        while((check != 'y') and (check!='n')):
             check=input('\nPlease enter y or n: ')
        if check == 'y':
             print(df.iloc[start:end])
             start+=10
             end+=10
             while(check =='y'):
                 check=input('\nWould you like look next 10 records? \nType y or n \ny:yes\nn:no\n')
                 while((check != 'y') and (check!='n')):
                    check=input('\nPlease enter y or n: ')
                 if check == 'y':
                     print(df.iloc[start:end])
                 start+=10
                 end+=10

        restart = input('\nWould you like to restart? Enter y or n.\n')
        restart = restart.lower()
        restart = restart[:1]
        while((restart != 'y') and (restart !='n')):
            restart=input('\nPlease enter y or n: ')
        if restart == 'n':
            break
        elif restart =='y':
            continue


if __name__ == "__main__":
	statistics()