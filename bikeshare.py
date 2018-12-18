import time
import pandas as pd


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
    city = input("Please enter \"chicago\", \"new york city\" or \"washington\" to view Bike Share Data: ")
    city = city.lower()
    while city not in CITY_DATA.keys():
        print("Sorry, {} is not valid city selection.".format(city))
        city = input("Please enter \"chicago\", \"new york city\" or \"washington\" to view Bike Share Data: ")
        city = city.lower()



    # TO DO: get user input for month (all, january, february, ... , june)
    month_list =["all", "january", "february", "march", "april", "may", "june"]
    month = input("Please select the month\'s data that you would like to view (january, february, march, april, may, june, or all): ")
    month = month.lower()
    while month not in month_list:
        print("Sorry, {} is not a valid selection. Please select from january, february, march, april, may, june, or all".format(month))
        month = input("Please select the month\'s data that you would like to view (january, february, march, april, may, june, or all): ")
        month = month.lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days_of_week = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day = input("Please select the day of the week whose data you would like to view (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday): ")
    day = day.lower()
    while day not in days_of_week:
        print("Sorry, {} is not a valid day of the week selection".format(day))
        day = input("Please select the day of the week whose data you would like to view (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday): ")
        day = day.lower()


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

    # convert the Start Time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # extract month and day of week from Start Time to create new columns
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name

    # filter by month if applicable
    if month != "all":
        # use the index of the months list to get the corresponding int
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df["month"] == month]

    # filter by day of week if applicable
    if day != "all":
        # filter by day of week to create the new dataframe
        df = df[df["day_of_week"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df["month"].mode()[0]
    print("The most common month was {}.\n".format(common_month))

    # TO DO: display the most common day of week
    common_day = df["day_of_week"].mode()[0]
    print("The most common day of the week in was {}.\n".format(common_day))
    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    common_hour = df["hour"].mode()[0]
    print("The most common hour  in was {}.\n".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df["Start Station"].mode()[0]
    print("The most commonly used  start station is {}.\n".format(start_station))
    # TO DO: display most commonly used end station
    end_station = df["End Station"].mode()[0]
    print("The most commonly used  end station is {}.\n".format(end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df["Start End Station Combo"] = df["Start Station"] + " and " + df["End Station"]
    station_combo = df["Start End Station Combo"].mode()[0]
    print("The most common Start and End Station combination is {}.\n".format(station_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("The total travel time was {}.\n".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("The mean travel time was {}.\n".format(total_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    print("User Type Totals: \n{}\n".format(user_types))
    # TO DO: Display counts of gender
    try:
        genders = df['Gender'].value_counts()
        print("Gender:")
        print(genders)
        print()
    #Create exception in the event CSV file doesn't have any gender data
    except KeyError:
        print("There isn't a [Gender] column in this spreedsheet!\n")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df["Birth Year"].min()
        most_recent_year = df["Birth Year"].max()
        common_year = df["Birth Year"].mode()[0]
        print("\nThe earliest year of birth was {}.\nThe most recent year of birth was {}.\nThe most common year of birth was {}.".format(earliest_year,most_recent_year,common_year))
    #Create exception in the event CSV file doesn't have any birthdate data
    except KeyError:
        print("There isn't a [Birth Year] column in this spreedsheet!")


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


        yes_count = 0
        see_more = input("Would you like to see 5 lines of raw data?\n")
        if see_more == "yes":
            yes_count += 1
            print(df.head())
            see_more = input("Would you like to see 5 more lines of data?\n")
            while see_more == "yes":
                yes_count += 1
                display_rows = 5 * yes_count
                print(yes_count)
                print("Displaying {} lines of data:\n".format(display_rows))
                print(df.head(display_rows))
                see_more = input("Would you like to see 5 more lines of data? ")




        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
