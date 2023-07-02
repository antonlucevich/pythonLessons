import requests

class New_Joke():
# Класс шуток

    def __init__(self):
        pass

    def create_new_random_joke(self):
        # Создание шутки

        category = "https://api.chucknorris.io/jokes/categories"
        result_category = requests.get(category)
        result_category_for_taken = result_category.json()
        print("Список категорий " + str(result_category_for_taken))

        i = 0
        while i < len(list(result_category_for_taken)):
            # Перебор категорий шуток

            url = "https://api.chucknorris.io/jokes/random?category=" + str(result_category_for_taken[i])
            print("Ссылка внутри перебора: " + str(url))
            i += 1

            result = requests.get(url)
            print("Код ответа: " + str(result.status_code))
            print("Шутка: " + str(result.json()["value"]))

            # Проверка кода ответа
            assert 200 == result.status_code
            if result.status_code == 200:
                print("Успешная операция \n")
            else:
                print("Ошибка операции")
                result.encoding = "utf-8"
                print(result.text)

# Выводим результат
joke = New_Joke()
joke.create_new_random_joke()