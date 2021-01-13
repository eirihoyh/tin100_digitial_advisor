from typing import List


class Transaction:
    """
    This class will only estimate if one single transaction is 'good' or 'bad' and will
    not take into consideration that user is doing many small transactions
    """
    default_positive = "Good job on following budget!"
    default_negative = "You are going over the budget!"

    tips = [
        "Plan your week before purchasing groceries!",
        "When visiting Oslo for a day, buy a 24 hours ticket. This will save "
        "you 37kr every time you take public transportation after 3 rides",
        "You can now save 27 500kr on your BSU account. This means that you can save 5 500kr on "
        "your taxes!",
        "If you earn less than 60 000kr this year you will not need to pay taxes!"
    ]
    def __init__(self, transaction_type):

        if transaction_type == "Payments":
            self.want_to_pay_debt = True
        else:
            self.want_to_pay_debt = False

        self.transaction_type = transaction_type

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
        pass

    def calculate_week_ratio(self) -> bool:
        """
        Here I want to calculate to see if the user have gone beyond
        25% (one week) of it's budget
        :return:
        """
        pass

    def dnb_transaction(self):
        """
        here I want to find information about what transactions a user have been using
        and relate it to transaction_type in database, ge
        :return:
        """
        pass
