import requests

class New_Joke():
# Класс шуток

    def __init__(self):
        pass

    def create_new_random_joke(self):
        # Создание шутки

        category_joke = input(str("Введите категорию шутки: "))
        category = "https://api.chucknorris.io/jokes/categories"
        result_category = requests.get(category)
        result_category_for_taken = result_category.json()

        # Сравниваем слово юзера и категории
        if set(result_category_for_taken) & set(category_joke.split()):
            print("Такая категория шуток есть, генерируем шутку \n")
            url_taken = "https://api.chucknorris.io/jokes/random?category=" + str(category_joke)
            result = requests.get(url_taken)
            # print("Код ответа: " + str(result.status_code))
            print("Шутка: " + str(result.json()["value"]))

            # Проверка кода ответа
            assert 200 == result.status_code
            if result.status_code == 200:
                print("Успешная операция \n")
            else:
                print("Ошибка операции")
                result.encoding = "utf-8"
                print(result.text)
        else:
            print("Такой категории шуток нет")

# Выводим результат
joke = New_Joke()
joke.create_new_random_joke()