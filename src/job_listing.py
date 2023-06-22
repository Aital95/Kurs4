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

    def __str__(self):
        """
                Возвращает строковое представление объекта JobListing.

                Returns:
                    str: Строковое представление вакансии.
                """
        return f"{self.title}\nSalary: {self.salary}\nDescription: {self.description}\nLink: {self.link}"