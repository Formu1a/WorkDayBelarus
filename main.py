from bs4 import BeautifulSoup
import requests
from funcForWork import split_into_groups,get_holiday_calendar,func_dict_data,change_values,serch_data
from settings import yearForHolidayCalendar,date_to_find


### Получаеем все значения с сайта с датами и значаниями даты
url = 'https://www.tws.by/tws/references/calendar-transition'
response = requests.get(url)
bs = BeautifulSoup(response.text)
temp = bs.find_all('td')

#### Делим на группы по 3 значкния в массиве
arr = split_into_groups(temp,3)


### делаем словарь из групп который мы сделаи выше
holDays = func_dict_data(arr)
print(holDays)

##### получаем все рабочие и выходные дни за год
adept = get_holiday_calendar(yearForHolidayCalendar)
print(adept)


### тут словарь с измененными значениями исходя из данных на сайте
dictFinData = change_values(holDays,adept)


# ищем дату и определяем рабочий день или нет
serch_data(dictFinData,date_to_find)