#definition of input month function.
def get_month():
    '''Asks the user for a month and returns the specified month.
    Args:
        none.
    Returns:
        (tuple) Lower limit, upper limit of month for the bikeshare data.
    '''
    months=['january','february','march','april','may','june']
    while True:
        month =input('\nWhich month of year? Choose january, february, march, april, may or june\n')
        month=month.lower()
        if(month in months):
            break
        print("\nI'm sorry, The month you have entered is incorrect. Please try again.")
    return month

#definition of input day function.
def get_day():
    '''Asks the user for a day and returns the specified day.
    Args:
        none.
    Returns:
        (tuple) Lower limit, upper limit of date for the bikeshare data.
    '''
    days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    while True:
        day =input('\nWhich day of week? Choose sunday, monday, tuesday, wednesday, thursday, friday or saturday\n')
        day=day.lower()
        if(day in days):
            break
        print("\nI'm sorry, The month you have entered is incorrect. Please try again.")
    return day

#definition of filters function
def get_filters():
    print('Hello! There Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, New York City, Washingon). 
    citys=['chi','new','was']
    while True:
        city =input('\nPlease choose one of the cities (chicago, new york city, washington)\n You can give first 3 letters:- ')
        city=city.lower()
        city = city[:3]
        if(city in citys):
            break
        print("\nI'm sorry, The city you have entered is incorrect. Please try again.")
    # get user input for filters (Month, Day, Both or not at all)
    while True:
        filters=['m','d','b','n']
        filter =input('\nDo you want to filter using\m:Month\nd:Day\nb:Both\nn:No filters\nType m, d, b, or n\n')
        if(filter in filters):
            break
    if(filter=='m'):
        # get filter criteria of month from user
        month=get_month()
        day='all'
    elif(filter=='d'):
        # get filter criteria of day from user
        day=get_day()
        month='all'
    elif(filter=='b'):
        # get filter criteria of month and day from user
        month=get_month()
        day=get_day()
    elif(filter=='n'):
        day='all'
        month='all'
    
    print('-'*100)
    return city, month, day