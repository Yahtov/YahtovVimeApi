# Импортируем библиотеку 'requests' для выполнения HTTP-запросов
import requests

response = requests.get("https://api.vimeworld.com/online") # Выполняем GET-запрос к API-URL и сохраняем ответ в переменной
data = response.json() # Извлекаем данные в формате JSON из ответа и сохраняем их в переменной словаря


total_players = data["total"] # Пытаемся получить значение ключа "total" из словаря и сохраняем его в переменной
print(f"На сервере играют: {total_players} игроков") # Выводим количество игроков в общем онлайне в терминал
