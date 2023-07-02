import requests

def send_post_request():
    # Задаем параметры запроса
    base_url = "https://rahulshettyacademy.com"
    post_resource = "/maps/api/place/add/json"
    api_key = "?key=qaclick123"

    # Формируем URL
    post_url = base_url + post_resource + api_key
    print(post_url)

    # Формируем тело запроса
    payload_json = {
        "location": {
            "lat": -38.383494,
            "lng": 33.427362
        },
        "accuracy": 50,
        "name": "Frontline house",
        "phone_number": "(+91) 983 893 3937",
        "address": "29, side layout, cohen 09",
        "types": [
            "shoe park",
            "shop"
        ],
        "website": "http://google.com",
        "language": "French-IN"
    }

    # Отправляем POST-запрос
    response = requests.post(post_url, json=payload_json)
    print(response.text)

    # Проверяем статус-код ответа
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Проверяем ответ
    response_data = response.json()
    assert response_data["status"] == "OK", f"Expected status 'OK', but got {response_data['status']}"

    return response_data["place_id"]

def save_place_ids_to_file(place_ids):
    # Сохранение place_ids
    with open("place_ids.txt", "w") as file:
        for place_id in place_ids:
            file.write(f"{place_id}\n")

def read_place_ids_from_file():
    # Чтение place_ids
    with open("place_ids.txt", "r") as file:
        return [line.strip() for line in file.readlines()]

def send_get_request(place_id):
    base_url = "https://rahulshettyacademy.com"
    get_resource = "/maps/api/place/get/json"
    api_key = "?key=qaclick123"

    # Формируем URL
    get_url = base_url + get_resource + api_key + "&place_id=" + place_id

    # Отправляем GET-запрос
    response = requests.get(get_url)

    # Проверяем статус-код ответа
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Проверяем ответ
    response_data = response.json()
    assert response_data["status"] == "OK", f"Expected status 'OK', but got {response_data['status']}"

# Отправляем POST-запрос 5 раз и сохраняем place_id в список
place_ids = [send_post_request() for _ in range(5)]

# Сохраняем place_id в текстовый файл
save_place_ids_to_file(place_ids)

# Читаем place_id из текстового файла
place_ids_from_file = read_place_ids_from_file()

# Отправляем GET-запрос для каждого place_id из файла и проверяем их существование
for place_id in place_ids_from_file:
    send_get_request(place_id)
