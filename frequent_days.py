import datetime
import operator
from calendar import day_name

# my solution
def most_frequent_days(year):
    day_mapper = {0:'Monday',
                  1:'Tuesday',
                  2:'Wednesday',
                  3:'Thursday',
                  4:'Friday',
                  5:'Saturday',
                  6:'Sunday'}

    count = dict()
    first_day = datetime.date(year,1,1)
    last_day = datetime.date(year,12,31)
    current_day = first_day
    while current_day <= last_day:
        num_day = current_day.weekday()
        count[day_mapper[num_day]] = count.get(day_mapper[num_day],0) + 1
        current_day += datetime.timedelta(days=1)

    max_value = max(count.iteritems(), key=operator.itemgetter(1))[1]
    return [key for key in count.keys()
            if count[key] == max_value]

# best solution
def most_frequent_days2(year):
    first = set(range(datetime.datetime(year, 1, 1).weekday(), 7))
    last = set(range(datetime.datetime(year, 12, 31).isoweekday()))
    return [day_name[day] for day in sorted((first & last) or (first | last))]

print most_frequent_days2(2188)
