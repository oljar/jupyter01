import datetime

aaa = '25:10:10'
print( datetime.datetime.strptime(aaa, '%H:%M:%S'))


def is_time_format(input_string):
    try:
        datetime.datetime.strptime(input_string, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False