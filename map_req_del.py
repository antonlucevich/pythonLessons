import requests

base_url = "https://rahulshettyacademy.com" # базовый урл
key = "?key=qaclick123" # ключ для запросов

post_resource = "/maps/api/place/add/json"  # метод Post
delete_resource = "/maps/api/place/delete/json" # метод Del
get_resource = "/maps/api/place/get/json" # метод Get

class Chek_Location():

    def __init__(self):
        pass

    def test_post_new_location(self):
        # Создание новой локации

        quantity = int(5) # цикл на 5 place_id

        for i in range(quantity):
            post_url = base_url + post_resource + key
            print("Post url: " + str(post_url))
            json_new_location = {
                "location": {
                    "lat": -38.383494,
                    "lng": 33.427362
                }, "accuracy": 50,
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
            result_post = requests.post(post_url, json=json_new_location)
            print(result_post.text)
            print("Статус код : " + str(result_post.status_code))
            assert 200 == result_post.status_code
            print("Создана новая локация")

            check_post = result_post.json() # в переменную json ответа
            check_info_post = check_post.get("status") # в переменную значение status
            print("Статус код ответа : " + check_info_post)
            assert check_info_post == "OK"

            place_id = check_post.get("place_id") # id локации в переменную
            print("Place_id : " + place_id)
            print("\n")

            f = open("place_ids.txt", "a") # сохраняем id в файл
            f.write(place_id + "\n")
            f.close()

    def test_delete_new_location(self):
        # Удаление новых локаций

        with open("place_ids.txt", "r") as file:
            place_ids = file.readlines()

            # обрабатываем выборочные локации place_id
            for place_id in place_ids[1:3]:
                # Удаляем лишние символы
                place_id = place_id.strip()
                delete_url = base_url + delete_resource + key
                json_delete_location = {
                    "place_id": place_id
                }
                print("Place_id" + delete_url)

                result_delete = requests.delete(delete_url, json = json_delete_location)
                print("Статус код : " + str(result_delete.status_code))
                assert 200 == result_delete.status_code
                print("Удаление локации успешно")


    def test_get_delete_location(self):
        # Проверка существования локации

        with open("place_ids.txt", "r") as file:
            place_ids = file.readlines()
            # Обрабатываем каждый place_id
            for place_id in place_ids:
                # Удаляем лшишние символы
                place_id = place_id.strip()
                get_url = base_url + get_resource + key + "&place_id=" + place_id
                print(get_url)

                result_get = requests.get(get_url)
                print(result_get.text)
                print("Статус код : " + str(result_get.status_code))
                if result_get.status_code == 200:
                    # Записываем place_id в новый файл, если код 200
                    with open("place_ids_exist.txt", "a") as f:
                        f.write(place_id + "\n")


# выводим результат операций
new_location = Chek_Location()
new_location.test_post_new_location()
new_location.test_delete_new_location()
new_location.test_get_delete_location()