import json
import os
from abc import ABC, abstractmethod

from src.job_listing import JobListing


class JobListingManager(ABC):
    @abstractmethod
    def add_listing(self, listing):
        pass

    @abstractmethod
    def filter_listings(self, keyword):
        pass

    @abstractmethod
    def delete_listing(self, listing):
        pass


class JSONJobListingManager(JobListingManager):
    """Класс для управления списком вакансий в формате JSON."""

    def __init__(self, filename):
        """
        Инициализирует экземпляр класса JSONJobListingManager.

        Args:
            filename (str): Имя файла для сохранения списка вакансий.
        """
        self.filename = filename
        self.listings = []
        self.load_listings()

    def load_listings(self):
        """
        Загружает список вакансий из файла JSON, создает пустой список, если файл не существует,
        или загружает пустой список, если файл существует, но является пустым.
        """
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    if isinstance(data, list):
                        for item in data:
                            listing = JobListing(
                                item.get("title"),
                                item.get("link"),
                                item.get("salary"),
                                item.get("description")
                            )
                            self.listings.append(listing)
                        print(f"Загружено {len(self.listings)} вакансий из файла {self.filename}.")
                    else:
                        print(f"Файл {self.filename} не содержит список вакансий.")
            except FileNotFoundError:
                print(f"Файл {self.filename} не найден.")
        else:
            print(f"Файл {self.filename} не существует. Создаю новый файл.")

    def save_listings(self):
        """
            Сохраняет список вакансий в файл JSON.
                """
        data = []
        for listing in self.listings:
            item = {
                "title": listing.title,
                "link": listing.link,
                "salary": listing.salary,
                "description": listing.description
            }
            data.append(item)

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def add_listing(self, listing):
        """
            Добавляет вакансию в список и сохраняет его.

            Args:
                listing (JobListing): Вакансия для добавления.
                """
        self.listings.append(listing)
        self.save_listings()

    def filter_listings(self, keyword):
        """
            Фильтрует список вакансий по ключевому слову.

            Args:
                keyword (str): Ключевое слово для фильтрации.

            Returns:
                list: Отфильтрованный список вакансий.
            """
        return [listing for listing in self.listings if keyword in listing.title or keyword in listing.description]

    def delete_listing(self, listing):
        """
            Удаляет вакансию из списка и сохраняет его.

            Args:
                listing (JobListing): Вакансия для удаления.
            """
        if listing in self.listings:
            self.listings.remove(listing)
            self.save_listings()
