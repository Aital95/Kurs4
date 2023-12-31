from src.job_api import HhJobAPI, SuperJobAPI
from src.job_listing import JobListing
from src.job_listing_manager import JSONJobListingManager
import os
import re


def get_job_listings(query, api1, api2):
    """
    Получение списка вакансий из двух API.

    Args:
        query: Запрос для поиска работы.
        api1: Объект для работы с API hh.ru.
        api2: Объект для работы с API superjob.ru.

    Returns:
        Список объектов JobListing.
    """
    jobs1 = api1.get_jobs(query)
    jobs2 = api2.get_jobs(query)
    jobs = jobs1 + jobs2
    listings = []

    for job in jobs:
        if "name" in job:
            title = job["name"]
        elif "profession" in job:
            title = job["profession"]
        else:
            title = "Нет названия"

        if "url" in job:
            link = job["url"]
        elif "link" in job:
            link = job["link"]
        else:
            link = "Нет ссылки"

        if "salary" in job and job["salary"] is not None and "from" in job["salary"]:
            salary = job["salary"]["from"]
        elif "payment_from" in job:
            salary = job["payment_from"]
        else:
            salary = "Не указано"

        if "snippet" in job:
            snippet = job["snippet"]
            if "responsibility" in snippet:
                description = snippet["responsibility"]
            else:
                description = "Нет описания"
        elif "candidat" in job:
            candidat_text = job["candidat"]
            match = re.search(r"Обязанности:\s+(.+)", candidat_text)
            if match:
                description = match.group(1)
            else:
                description = "Нет описания"
        else:
            description = "Нет описания"

        listing = JobListing(title, link, salary, description)
        listings.append(listing)

    return listings


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
        print("2. Выход")
        option = input("Выберите вариант: ")

        if option == "1":
            query = input("Введите запрос для поиска работы: ")
            listings = get_job_listings(query, api1, api2)

            for i, listing in enumerate(listings):
                print(f"\nРабота {i + 1}:")
                print(listing)

            if listings:
                choice = input("\nВведите номер списка вакансий для сохранения (или «0», чтобы пропустить): ")
                if choice.isdigit():
                    index = int(choice) - 1
                    if index >= 0 and index < len(listings):
                        manager.add_listing(listings[index])
                        print("Список вакансий сохранен.")
                    elif index == -1:
                        print("Список вакансий пропущен.")
                    else:
                        print("Неверный выбор.")
                else:
                    print("Неверный выбор.")
        elif option == "2":
            break

        else:
            print("Неверный выбор. Попробуйте еще раз.")

            # После сохранения списка вакансий добавляем опции 2 и 3
        while True:
            print("\nПараметры:")
            print("1. Поиск работы")
            print("2. Фильтровать вакансии по ключевому слову")
            print("3. Удалить список вакансий")
            print("4. Выход")
            option = input("Выберите вариант: ")

            if option == "1":
                query = input("Введите запрос для поиска работы: ")
                listings = get_job_listings(query, api1, api2)

                for i, listing in enumerate(listings):
                    print(f"\nРабота {i + 1}:")
                    print(listing)

                if listings:
                    choice = input("\nВведите номер списка вакансий для сохранения (или «0», чтобы пропустить): ")
                    if choice.isdigit():
                        index = int(choice) - 1
                        if index >= 0 and index < len(listings):
                            manager.add_listing(listings[index])
                            print("Список вакансий сохранен.")
                        elif index == -1:
                            print("Список вакансий пропущен.")
                        else:
                            print("Неверный выбор.")
                    else:
                        print("Неверный выбор.")

            elif option == "2":
                keyword = input("Введите ключевое слово для фильтрации списков вакансий: ")
                filtered_listings = manager.filter_listings(keyword)
                if filtered_listings:
                    for i, listing in enumerate(filtered_listings):
                        print(f"\nJob {i + 1}:")
                        print(listing)
                else:
                    print("По данному ключевому слову не найдено списков вакансий.")

            elif option == "3":
                print("\nВаши сохраненные списки вакансий:")
                for i, listing in enumerate(manager.listings):
                    print(f"\nJob {i + 1}:")
                    print(listing)
                choice = input("\nВведите номер списка вакансий для удаления: ")
                if choice.isdigit():
                    index = int(choice) - 1
                    if index >= 0 and index < len(manager.listings):
                        listing = manager.listings[index]
                        manager.delete_listing(listing)
                        print("Список вакансий удален.")
                    else:
                        print("Неверный выбор.")
                else:
                    print("Неверный выбор.")

            elif option == "4":
                break

            else:
                print("Неверный выбор. Попробуйте еще раз.")




def main():
    hh_api_url = os.getenv('HH_API_URL')
    hh_api = HhJobAPI(hh_api_url)

    superjob_token = os.getenv('SJ_API_KEY')
    superjob_api = SuperJobAPI(superjob_token)

    manager = JSONJobListingManager("job_listings.json")

    interact_with_user(manager, hh_api, superjob_api)


if __name__ == "__main__":
    main()
