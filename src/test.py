import requests
from abc import ABC, abstractmethod
class AbstractJobAPI(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями."""
    @abstractmethod
    def get_jobs(self, query):
        pass


class HhJobAPI(AbstractJobAPI):
    """Класс для работы с API hh.ru."""

    def __init__(self, api_url):
        self.api_url = api_url

    def get_jobs(self, query):
        """Получает вакансии с помощью API hh.ru.
               Args:
                   query: Поисковый запрос для вакансий.
               Returns:
                   Список словарей, представляющих информацию о вакансиях."""
        url = f"https://api.hh.ru/vacancies?text={query}&area=113&per_page=10"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get("items", [])
        else:
            print("Ошибка доступа HH.ru API.")
            return []


class SuperJobAPI(AbstractJobAPI):
    """Класс для работы с API superjob.ru."""
    def __init__(self, token):
        self.token = token

    def get_jobs(self, query):
        """Получает вакансии с помощью API superjob.ru.
                Args:
                    query: Поисковый запрос для вакансий.
                Returns:
                    Список словарей, представляющих информацию о вакансиях."""
        url = f"https://api.superjob.ru/2.0/vacancies?keyword={query}"
        headers = {"X-Api-App-Id": self.token}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get("objects", [])
        else:
            print("Ошибка доступа SuperJob.ru API.")
            return []
def interact_with_user(manager, api1, api2):
    """
    Взаимодействие с пользователем через консоль.

    Args:
        manager: Менеджер вакансий.
        api1: Объект для работы с API hh.ru.
        api2: Объект для работы с API superjob.ru.
    """
    while True:
        print("\nПараметры:")
        print("1. Поиск работы")
        print("2. Фильтровать вакансии по ключевому слову")
        print("3. Удалить список вакансий")
        print("4. Выход")
        option = input("Выберите вариант: ")
        if option == "1":
            query = input("Введите запрос для поиска работы: ")
            jobs1 = api1.get_jobs(query)
            jobs2 = api2.get_jobs(query)
            jobs = jobs1 + jobs2
            listings = []

for job in jobs:
    if "title" in job:
        print("Ключ 'title' присутствует в данных")

    if "description" in job:
        print("Ключ 'description' присутствует в данных")
    else:
        print("Ключ 'description' отсутствует в данных")


