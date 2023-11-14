from datetime import date, timedelta

def get_birthdays_per_week(users):
    result = {}

    if len(users) == 0:
        return result

    current_date = date.today()
    current_date_plus_week = current_date + timedelta(days=7)
    
    current_year = current_date.year

    for user in users:
        new_date = user['birthday'].replace(year=current_year)
        if  current_date <= new_date < current_date_plus_week:
            day_of_the_week = new_date.strftime('%A')
            if day_of_the_week == 'Saturday' or day_of_the_week == 'Sunday':
                day_of_the_week = 'Monday'
            if day_of_the_week in result:
                result[day_of_the_week].append(user['name'].split(' ')[0])
            else:
                result[day_of_the_week] = [user['name'].split(' ')[0]]

    return result
    