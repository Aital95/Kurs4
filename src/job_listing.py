class JobListing:
    """Класс для представления информации о вакансии."""
    def __init__(self, title, link, salary, description):
        """
                Инициализирует экземпляр класса JobListing.

                Args:
                    title (str): Заголовок вакансии.
                    link (str): Ссылка на вакансию.
                    salary (str): Зарплата.
                    description (str): Описание вакансии.
                """
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

    def __gt__(self, other):
        """Определяет оператор > для сравнения по зарплате."""
        return self.salary > other.salary

    def __lt__(self, other):
        """Определяет оператор < для сравнения по зарплате."""
        return self.salary < other.salary

    def sorted_listings(listings):
        """Сортирует список объявлений по зарплате."""
        return sorted(listings)

    #def gt и lt (сравнивают по зарплате) (метод сортирует sorted(зависит от gt и lt))

    def __str__(self):
        """
                Возвращает строковое представление объекта JobListing.

                Returns:
                    str: Строковое представление вакансии.
                """
        return f"{self.title}\nЗарплата: {self.salary}\nОписание: {self.description}\nСсылка: {self.link}"