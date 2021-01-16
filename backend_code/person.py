from typing import Union, Dict


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
        self.use_money = float(avrg_income) - float(monthly_debt)

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
    status_constant = 1.4

    def __init__(self, nr_people: int,
                 avrg_income: Union[str, float],
                 monthly_debt: Union[str, float]) -> None:
        super().__init__(nr_people=nr_people,
                         avrg_income=avrg_income,
                         monthly_debt=monthly_debt)

    def calculate_budget(self) -> Dict:
        self.budget_setup["Food/drinks"] = self.use_money * 0.4
        self.budget_setup["Payments"] = self.monthly_debt
        self.budget_setup["Clothing"] = self.use_money * 0.2
        self.budget_setup["Travel"] = self.use_money * 0.1
        self.budget_setup["Freetime"] = self.use_money * 0.2
        self.budget_setup["Buffer account"] = self.use_money * 0.1

        return self.budget_setup


class Family(Person):
    status_constant = 1.5

    def __init__(self, nr_people: int,
                 avrg_income: Union[int, float],
                 monthly_debt: Union[int, float]) -> None:
        super().__init__(nr_people=nr_people,
                         avrg_income=avrg_income,
                         monthly_debt=monthly_debt)

    def calculate_budget(self) -> Dict:
        self.budget_setup["Food/drinks"] = self.use_money * 0.2
        self.budget_setup["Payments"] = self.monthly_debt
        self.budget_setup["Clothing"] = self.use_money * 0.2
        self.budget_setup["Travel"] = self.use_money * 0.2
        self.budget_setup["Freetime"] = self.use_money * 0.3
        self.budget_setup["Buffer account"] = self.use_money * 0.1

        return self.budget_setup


class Retired(Person):
    status_constant = 0.75

    def __init__(self, nr_people: Union[int, float],
                 avrg_income: Union[int, float],
                 monthly_debt: Union[int, float]) -> None:
        super().__init__(nr_people=nr_people,
                         avrg_income=avrg_income,
                         monthly_debt=monthly_debt)

    def calculate_budget(self) -> Dict:
        self.budget_setup["Food/drinks"] = self.use_money * 0.2
        self.budget_setup["Payments"] = self.monthly_debt
        self.budget_setup["Clothing"] = self.use_money * 0.2
        self.budget_setup["Travel"] = self.use_money * 0.3
        self.budget_setup["Freetime"] = self.use_money * 0.2
        self.budget_setup["Buffer account"] = self.use_money * 0.1

        return self.budget_setup
