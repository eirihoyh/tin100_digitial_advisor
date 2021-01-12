from typing import Union


class Person:
    budget_setup = {
        "Food/drinks": 0,
        "Clothing": 0,
        "Travel": 0,
        "Payments": 0,
        "Buffer account": 0,
        "Freetime": 0
    }

    def __init__(self, nr_people: int,
                 avrg_income: Union[str, float],
                 monthly_debt: Union[str, float],
                 status_constant: Union[str, float]) -> None:

        self.nr_people = nr_people
        self.avrg_income = avrg_income
        self.monthly_debt = monthly_debt
        self.status_constant = status_constant

    def calculate_budget(self) -> None:
        self.budget_setup["Food/drinks"] = 3500 * self.status_constant * self.nr_people
        self.budget_setup["Clothing"] = 500* self.nr_people * self.status_constant
        self.budget_setup["Travel"]

    def check_budget(self):
        pass

    def check_if_beyond_salary(self) -> bool:
        amount = 0
        for key in self.budget_setup:
            amount += self.budget_setup[key]

        return amount <= self.avrg_income


class Student(Person):
    def __init__(self, nr_people: int,
                 avrg_income: Union[str, float],
                 monthly_debt: Union[str, float]) -> None:

        super().__init__(nr_people=nr_people,
                         avrg_income=avrg_income,
                         monthly_debt=monthly_debt,
                         status_constant=1)


class Family(Person):
    def __init__(self, nr_people: int,
                 avrg_income: Union[str, float],
                 monthly_debt: Union[str, float]) -> None:

        super().__init__(nr_people=nr_people,
                         avrg_income=avrg_income,
                         monthly_debt=monthly_debt,
                         status_constant=1.25)


class Retired(Person):
    def __init__(self, nr_people: int,
                 avrg_income: Union[str, float],
                 monthly_debt: Union[str, float]) -> None:

        super().__init__(nr_people=nr_people,
                         avrg_income=avrg_income,
                         monthly_debt=monthly_debt,
                         status_constant=0.75)
