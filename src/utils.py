# Функция для создания периодов
from calendar import monthrange


def get_period(month: int, year: int):
    first_day = f"00:01:00 01.{month:02d}.{year}"
    last_day = f"23:59:00 {monthrange(year, month)[1]:02d}.{month:02d}.{year}"
    return first_day, last_day
