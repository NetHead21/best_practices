import datetime

def get_monday_friday_dates(year: int) -> list[datetime.date]:
    monday_friday_dates = []
    for month in range(1, 13):
        for day in range(1, 32):
            try:
                date_obj = datetime.date(year, month, day)
                weekday = date_obj.weekday()
                if weekday == 0 or weekday == 4:  # 0 represents Monday, 4 represents Friday
                    monday_friday_dates.append(date_obj)
            except ValueError:
                # Skip invalid dates (e.g., February 30)
                pass
    return monday_friday_dates



print(get_monday_friday_dates(2022))