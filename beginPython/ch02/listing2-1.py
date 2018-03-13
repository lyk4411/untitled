# Print out a date, given year, month, and day as numbers
from pip._vendor.distlib.compat import raw_input

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

# A list with one ending for each number from 1 to 31
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
        + ['st', 'nd', 'rd'] +  7 * ['th'] \
        + ['st']

year    = raw_input('Year: ')
month   = raw_input('Month (1-12): ')
day     = raw_input('Day (1-31): ')

month_number = int(month)
day_number = int(day)

# Remember to subtract 1 from month and day to get a correct index
month_name = months[month_number-1]
ordinal = day + endings[day_number-1]

print (month_name + ' ' + ordinal + ', ' + year)

# for i in range(5):
#     if i == 5:
#         print ('found it! i = %s' % i)
#         break
# else:
#     print ('not found it ...')

# girls=['a','b','c','c']
# boys =['1','2','3','4']
# print(list(b + g for b in boys for g in girls))

dict = {'runoob': '菜鸟教程', 'google': 'Google 搜索'}

print("Value : %s" % dict.setdefault('runoob', None))
print("Value : %s" % dict.setdefault('Taobao', '淘宝'))
print(dict)