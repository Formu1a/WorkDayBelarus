import datetime
import holidays

def func_dict_data(arr):
    dictArr= []
    for x in arr:
        key = str(x[0])[4:][:-5]
        val = str(x[1])[4:][:-5]
        # отбираем по определенному году (который на данный момент)
        if str(datetime.date.today().year) in key:
            dictData = {key:val}
            dictArr.append(dictData)
        else:
            continue
    return dictArr


def split_into_groups(array, group_size):
    groups = []
    current_group = []

    for item in array:
        current_group.append(item)

        if len(current_group) == group_size:
            groups.append(current_group)
            current_group = []

    if current_group:
        groups.append(current_group)

    return groups


def get_holiday_calendar(year):
    calendar = []
    blr_holidays = holidays.BY(years=year)

    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, 12, 31)

    delta = datetime.timedelta(days=1)
    current_date = start_date

    while current_date <= end_date:
        is_working = current_date.weekday() < 5 and current_date not in blr_holidays
        formatted_date = current_date.strftime("%d")
        formatted_dateM = current_date.strftime("%m")
        calendar.append({f'{formatted_date}.{formatted_dateM}.{current_date.year}':"Рабочий" if is_working else "Выходной"})
        current_date += delta

    return calendar


def change_values(arr1, arr2):
    for obj1 in arr1:
        for obj2 in arr2:
            if obj1.keys() == obj2.keys():
                # Меняем значение текущего объекта во втором массиве на значение из первого массива
                obj2[list(obj1.keys())[0]] = obj1[list(obj1.keys())[0]]

    return arr2



def serch_data(data,date_to_find):
    for item in data:
        # Проверяем ключ (дату) каждого элемента с искомой датой
        if date_to_find in item:
            value = item[date_to_find]
            print(value)
            break
    else:
        print('Значение для указанной даты не найдено')


