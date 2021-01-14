from typing import List, Union
import random

from DNB_psd2 import AISP
from database_connecter import StoreInDatabase


class Transaction:
    """
    This class will only estimate if one single transaction is 'good' or 'bad' and will
    not take into consideration that user is doing many small transactions
    """
    default_positive = "Good job on following budget!"
    default_negative = "You are going over the budget,\n" \
                       "you should spend 25% or less of the budget per week!"

    tips = [
        "Plan your week before purchasing groceries!",
        "When visiting Oslo for a day, buy a 24 hours ticket.\nThis will save "
        "you 37kr every time you take public transportation after 3 rides",
        "You can now save 27 500kr on your BSU account.\nThis means that you can save 5 500kr on "
        "your taxes!",
        "If you earn less than 60 000kr this year\nyou will not need to pay taxes!"
    ]
    want_to_pay_debt = False

    def __init__(self, transaction_type: str):

        if transaction_type == "Payments":
            self.want_to_pay_debt = True
            self.placement_in_database = 4
        elif transaction_type == "Food":
            self.placement_in_database = 1
        elif transaction_type == "Travel":
            self.placement_in_database = 3
        else:
            NameError(f"Name {transaction_type} is not in database")

    def do_transaction(self) -> List[str]:
        """
        Uses dnb_transaction and the chosen categories from gui to estimate
        how it's going with the budget
        Need to get information on how much money have been spent (dnb_transaction), get
        information about what it is spent on (self.transaction_type), relate
        money spent to users budget (calculate_week_ratio) and need to give a message if
        user is doing well or not and/or tips for further spendings.
        :return:
        Returns a a list with two strings that contains a positive/negative message
        """
        ratio = self.calculate_week_ratio()
        tips = random.choice(self.tips)
        if self.want_to_pay_debt == True:
            if ratio[0] == False:
                return [self.default_positive, tips, ratio[1], ratio[2]]
            else:
                return ["You must pay more to your debt!", tips, ratio[1], ratio[2]]

        else:
            if ratio[0] == True:
                return [self.default_positive, tips, ratio[1], ratio[2]]
            else:
                return [self.default_negative, tips, ratio[1], ratio[2]]

    def calculate_week_ratio(self) -> List[Union[bool, float, int]]:
        """
        Here I want to calculate to see if the user have gone beyond
        25% (one week) of it's budget
        :return:
        True if this is the amount spent in one week is under 25% of budget, false else
        """
        data = StoreInDatabase()
        budget = data.get_data()
        budget_type = budget[self.placement_in_database]

        used_money = self.dnb_transaction()

        ratio = used_money / budget_type
        print(f"Budget type: {budget_type}\nUsed money: {used_money}\nRatio: {ratio}")

        return [ratio < 0.25, budget_type, used_money]

    @staticmethod
    def dnb_transaction() -> Union[int, float]:
        """
        here I want to find information about what transactions a user have been using
        and relate it to transaction_type in database, ge
        :return:
        """
        AISP_client = AISP(PSU_ID="31125458052", pem_path="../../certificate/certificate.pem",
                           key_path="../../certificate/private.key",
                           webdriver_path="../../chromedriver_win32/chromedriver.exe")
        accounts = AISP_client.accounts()
        transaction_history = AISP_client.get_bank_transactions(bban=f"{accounts[0]}")
        transactions = transaction_history["transactions"]
        booked = transactions["booked"]
        amount = 0
        for trans in booked:
            transaction_amount = trans["transactionAmount"]
            amount += float(transaction_amount["amount"])

        return amount


if __name__ == "__main__":
    k = Transaction("Food")
    k.do_transaction()
