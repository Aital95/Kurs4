import json
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
            Загружает список вакансий из файла JSON.
                """
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                for item in data:
                    listing = JobListing(item["title"], item["link"], item["salary"], item["description"])
                    self.listings.append(listing)
        except FileNotFoundError:
            print(f"Файл {self.filename} не найден.")

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
