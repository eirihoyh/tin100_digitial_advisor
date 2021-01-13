from typing import Union, Dict
"""HEI"""

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
                 avrg_income: Union[int, float],
                 monthly_debt: Union[int, float]) -> None:

        self.nr_people = nr_people
        self.avrg_income = avrg_income
        self.monthly_debt = monthly_debt

    def check_budget(self):
        """
        maybe check if budget follows avrg_income and save it to a database
        :return:
        """
        pass

    def check_if_salary_ok(self) -> bool:
        amount = 0
        for item in self.budget_setup.values():
            amount += item

        return amount <= self.avrg_income


class Student(Person):

    status_constant = 1

    def __init__(self, nr_people: int,
                 avrg_income: Union[str, float],
                 monthly_debt: Union[str, float]) -> None:

        super().__init__(nr_people=nr_people,
                         avrg_income=avrg_income,
                         monthly_debt=monthly_debt)

    def calculate_budget(self) -> Dict:
        self.budget_setup["Food/drinks"] = 3000 * self.status_constant * self.nr_people
        self.budget_setup["Payments"] = self.monthly_debt
        self.budget_setup["Clothing"] = 500 * self.status_constant * (1 + (self.nr_people/2))
        self.budget_setup["Travel"] = 500 * self.status_constant * (1 + (self.nr_people/2))
        self.budget_setup["Freetime"] = 500 * self.status_constant * (1 + (self.nr_people/2))
        self.budget_setup["Buffer account"] = 500 * self.status_constant * (1 + (self.nr_people/2))

        return self.budget_setup


class Family(Person):

    status_constant = 1.5

    def __init__(self, nr_people: int,
                 avrg_income: Union[int, float],
                 monthly_debt: Union[int, float]) -> None:

        super().__init__(nr_people=nr_people,
                         avrg_income=avrg_income,
                         monthly_debt=monthly_debt)

    def calculate_budget(self) -> None:
        self.budget_setup["Food/drinks"] = 3000 * self.status_constant * self.nr_people
        self.budget_setup["Payments"] = self.monthly_debt
        self.budget_setup["Clothing"] = 500 * self.status_constant * (1 + (self.nr_people / 2))
        self.budget_setup["Travel"] = 500 * self.status_constant * (1 + (self.nr_people / 2))
        self.budget_setup["Freetime"] = 500 * self.status_constant * (1 + (self.nr_people / 2))
        self.budget_setup["Buffer account"] = 500 * self.status_constant * (
                    1 + (self.nr_people / 2))

        return self.budget_setup


class Retired(Person):

    status_constant = 0.75

    def __init__(self, nr_people: Union[int, float],
                 avrg_income: Union[int, float],
                 monthly_debt: Union[int, float]) -> None:

        super().__init__(nr_people=nr_people,
                         avrg_income=avrg_income,
                         monthly_debt=monthly_debt)

    def calculate_budget(self) -> None:
        self.budget_setup["Food/drinks"] = 3000 * self.status_constant * self.nr_people
        self.budget_setup["Payments"] = self.monthly_debt
        self.budget_setup["Clothing"] = 500 * self.status_constant * (1 + (self.nr_people / 2))
        self.budget_setup["Travel"] = 500 * self.status_constant * (1 + (self.nr_people / 2))
        self.budget_setup["Freetime"] = 500 * self.status_constant * (1 + (self.nr_people / 2))
        self.budget_setup["Buffer account"] = 500 * self.status_constant * (
                1 + (self.nr_people / 2))

        return self.budget_setup
