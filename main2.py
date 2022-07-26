import datetime
from datetime import datetime, timedelta

message = input("Введите напоминание ")

words = {'через': 1}

words3 = {'  ': 1}

words2 = {' в ': 1,}

hour2 = {'10 часов': 10, '11 часов': 11, '12 часов': 12,
'13 часов': 13, '14 часов': 14, '15 часов': 15, '16 часов': 16, '17 часов': 17, '18 часов': 18,
'19 часов': 19, '20 часов': 20, '21 час': 21, '22 часа': 22, '23 часа': 23, '1 час': 1, '2 часа': 2, '3 часа': 3, '4 часа': 4, '5 часов': 5, '6 часов': 6,
'7 часов': 7, '8 часов': 8, '9 часов': 9, 'час': 1,}

minute2 = {'10 минут': 10, '11 минут': 11, '12 минут': 12, '13 минут': 13,
           '14 минут': 14, '15 минут': 15, '16 минут': 16, '17 минут': 17,
'18 минут': 18, '19 минут': 19, '20 минут': 20, '21 минуту': 21, '22 минуты': 22,
'23 минуты': 23, '24 минуты': 24, '25 минут': 25, '26 минут': 26, '27 минут': 27, '28 минут': 28,
'29 минут': 29, '30 минут': 30, '31 минуту': 31, '32 минуты': 32, '33 минуты': 33,
'34 минуты': 34, '35 минут': 35, '36 минут': 36, '37 минут': 37, '38 минут': 38, '39 минут': 39,
'40 минут': 40, '41 минуту': 41, '42 минуты': 42, '43 минуты': 43, '44 минуты': 44,
'45 минут': 45, '46 минут': 46, '47 минут': 47, '48 минут': 48, '49 минут': 49, '50 минут': 50,
'51 минуту': 51, '52 минуты': 52, '53 минуты': 53, '54 минуты': 54, '55 минут': 55, '56 минут': 56,
'57 минут': 57, '58 минут': 58, '59 минут': 59,'60 минут': 60, '61 минуту': 61,
'62 минуты': 62,'63 минуты': 63, '64 минуты': 64, '65 минут': 65, '66 минут': 66, '67 минут': 67,
'68 минут': 68, '69 минут': 69, '70 минут': 70, '71 минуту': 71, '72 минуты': 72,
'73 минуты': 73, '74 минуты': 74, '75 минут': 75, '76 минут': 76, '77 минут': 77, '78 минут': 78,
'79 минут': 79, '80 минут': 80, '81 минуту': 81, '82 минуты': 82, '83 минуты': 83,
'84 минуты': 34, '85 минут': 85, '86 минут': 86, '87 минут': 87, '88 минут': 88, '89 минут': 89,
'90 минут': 90, '91 минуту': 91, '92 минуты': 92, '93 минуты': 93, '94 минуты': 94,
'95 минут': 95, '96 минут': 96, '97 минут': 97, '98 минут': 98, '99 минут': 99, '100 минут': 100,
'минуту': 1, '1 минуту': 1, '2 минуты': 2, '3 минуты': 3, '4 минуты': 4, '5 минут': 5, '6 минут': 6, '7 минут': 7,
'8 минут': 8, '9 минут': 9, }

day = {'10 ': 10,
'11 ': 11, '12 ': 12, '13 ': 13, '14 ': 14, '15 ': 15, '16 ': 16, '17 ': 17, '18 ': 18, '19 ': 19,
'20 ': 20, '21 ': 21, ' 22 ': 22, '23 ': 23, '24 ': 24, '25 ': 25, '26 ': 26, '27 ': 27,
'28 ': 28, '29 ': 29, '30 ': 30, '31 ': 31, ' 1 ': 1, ' 2 ': 2, ' 3 ': 3, ' 4 ': 4, ' 5 ': 5, '6 ': 6, '7 ': 7, '8 ': 8, '9 ': 9, }

month = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6,
'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}

year = {'2019 года': 2019, '2020 года': 2020, '2021 года': 2021, '2022 года': 2022, '2023 года': 2023}

hour = { '10:': 10, '11:': 11, '12:': 12, '13:': 13, '14:': 14, '15:': 15, '16:': 16, '17:': 17,
'18:': 18, '19:': 19, '20:': 20, '21:': 21, '22:': 22,'23:': 23, '01:': 1, '02:': 2, '03:': 3, '04:': 4, '05:': 5, '06:': 6, '07:': 7, '08:': 8, '09:': 9,
'1:': 1, '2:': 2, '3:': 3, '4:': 4, '5:': 5, '6:': 6, '7:': 7, '8:': 8, '9:': 9, '0:': 0}

minute = {'10': 10, '11': 11, '12': 12, '13': 13, '14': 14, '15': 15,
'16': 16, '17': 17, '18': 18, '19': 19, '20': 20, '21': 21, '22': 22, '23': 23, '24': 24, '25': 25,
'26': 26, '27': 27, '28': 28, '29': 29, '30': 30,
'31': 31, '32': 32, '33': 33, '34': 34, '35': 35, '36': 36, '37': 37, '38': 38, '39': 39, '40': 40,
'41': 41, '42': 42, '43': 43, '44': 44, '45': 45,
'46': 45, '47': 47, '48': 48, '49': 49, '50': 50, '51': 51, '52': 52, '53': 53, '54': 54, '55': 55, '56': 56,
'57': 57, '58': 58, '59': 59, '00': 0, '01': 1, '02': 2, '03': 3, '04': 4, '05': 5, '06': 6, '07': 6, '08': 8, '09': 9,}

day2 = {'1 день': 1, ' день': 1, ' 2 дня': 2, ' 3 дня': 3, ' 4 дня': 4, ' 5 дней': 5, '6 дней': 6, '7 дней': 7, '8 дней': 8, '9 дней': 9, '10 дней': 10,
'11 дней': 11, '12 дней': 12, '13 дней': 13, '14 дней': 14, '15 дней ': 15, '16 дней ': 16, '17 дней ': 17, '18 дней': 18, '19 дней': 19,
'20 дней': 20, '21 день': 21, ' 22 дня': 22, '23 дня': 23, '24 дня': 24, '25 дней': 25, '26 дней': 26, '27 дней': 27,
'28 дней': 28, '29 дней': 29, '30 дней': 30, '31 день': 31}


def through(mess):
    message = mess
    words3_list = list(words3.keys())
    words_list = list(words.keys())
    hour2_list = list(hour2.keys())
    minute2_list = list(minute2.keys())
    day2_list = list(day2.keys())
    res_list = hour2_list + words_list + minute2_list

    for k, v in day2.items():
        exist = k in mess
        if exist == 1:
            day3 = day2[k]
            message = mess.replace(k, '')
            break
        else:
            day3 = 0

    for k, v in hour2.items():
        exist = k in message
        if exist == 1:
            hour1 = hour2[k]
            message = message.replace(k, '')
            break
        else:
            hour1 = 0

    for k, v in minute2.items():
        exist = k in message
        if exist == 1:
            minute1 = minute2[k]
            message = message.replace(k, '')
            break
        else:
            minute1 = 0

    for word in res_list:
        if word in message:
            message = message.replace(word, '')

    for word in words3_list:
        if word in message:
            message = message.replace(word, '')

    curr = datetime.now()
    td = timedelta( days=day3, hours=hour1, minutes=minute1)
    b = curr + td

    print({'STATUS': 'SUCCESS','DATE': {'year': b.strftime('%Y'), 'month': b.strftime('%m'), 'day': b.strftime('%d'),
                                        'hour': b.strftime('%H'), 'minute': b.strftime('%M')},'TEXT': {message}})

def specdata(mess):
    message = mess
    words3_list = list(words3.keys())
    words2_list = list(words2.keys())
    year_list = list(year.keys())
    month_list = list(month.keys())
    day_list = list(day.keys())
    hour_list = list(hour.keys())
    minute_list = list(minute.keys())
    time_now = datetime.now()

    for k, v in year.items():
        exist = k in mess
        if exist == 1:
            year1 = year[k]
            message = message.replace(k, '')
            break
        else:
            year1 = time_now.year

    for k, v in month.items():
        exist = k in mess
        if exist == 1:
            month1 = month[k]
            message = message.replace(k, '')
            break
        else:
            month1 = time_now.month


    for k, v in day.items():
        exist = k in mess
        if exist == 1:
            day1 = day[k]
            message = message.replace(k, '')
            break
        else:
            day1 = time_now.day

    for k, v in hour.items():
        exist = k in message
        if exist == 1:
            hour1 = hour[k]
            message = message.replace(k, '')
            break
        else:
            hour1 = time_now.hour

    for k, v in minute.items():
        exist = k in message
        if exist == 1:
            minute1 = minute[k]
            message = message.replace(k, '')
            break
        else:
            minute1 = time_now.minute

    for word in words2_list:
        if word in message:
            message = message.replace(word, '')

    for word in words3_list:
        if word in message:
            message = message.replace(word, '')

    print({'STATUS': 'SUCCESS', 'DATE': {'year': {year1}, 'month': {month1}, 'day': {day1}, 'hour': {hour1}, 'minute': {minute1}}, 'TEXT': {message}})

def test(mess):
    for k, v in words.items():
        qwe = k in mess
        if qwe == 1:
            through(mess)
        else:
            specdata(mess)

try:
    test(message)
except Exception:
    print({'STATUS': 'ERROR!'})
