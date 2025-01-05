import requests

from schemas import Point
from utils import get_period

# from src.schemas import Point

# Пример данных
cashier_id = "c817246fefe734d78092903ad29008ad9f927dbd44d77c6ce48466a8598c1559"
registrar_id = "4000777270"

# Создаем список объектов Points
points_list = [
    Point(name="Nicca", cashier_id=cashier_id, registrar_id=registrar_id),
    Point(name="SanTrope", cashier_id=cashier_id, registrar_id=registrar_id),
    Point(name="Soldat", cashier_id="c817246fefe734d78092903ad29008ad9f927dbd44d77c6ce48466a8598c1559", registrar_id="4000777270"),
    Point(name="Jamaika", cashier_id=cashier_id, registrar_id=registrar_id)
]

# URL и заголовки для запросов
url = "http://127.0.0.1:55551/command/getReportForPeriod"
headers = {
    "accept": "application/json;charset=utf-8",
    "Content-Type": "application/json;charset=utf-8"
}
year = 2024


# Выполнение запросов и сохранение результатов
for point in points_list:
    with open(f"{point.name}.txt", "w", encoding="utf-8") as file:
        for month in range(1, 13):  # Для каждого месяца
            start_period, end_period = get_period(month, year)
            payload = {
                "commandName": "getReportForPeriod",
                "cashierId": point.cashier_id,
                "registrarId": point.registrar_id,
                "from": start_period,
                "to": end_period
            }
            try:
                # Выполняем запрос
                response = requests.post(url, headers=headers, json=payload)
                response.raise_for_status()
                # Сохраняем ответ в файл
                file.write(f"Месяц: {month:02d}\n")
                file.write(response.text + "\n\n")
            except requests.RequestException as e:
                # Логируем ошибки
                file.write(f"Месяц: {month:02d}\n")
                file.write(f"Ошибка: {str(e)}\n\n")
