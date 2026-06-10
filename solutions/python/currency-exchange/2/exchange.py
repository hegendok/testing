"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    """Calculate the amount of money after exchanging currency.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return budget / exchange_rate



def get_change(budget, exchanging_value):
    """Calculate the amount of change after exchanging currency

    :param budget: float - amount of money you own
    :param exchanging_value: float - the amount of money user is exchanging now
    :return: float - the amount of money left from the starting currency after the exchage
    """
    return budget - exchanging_value



def get_value_of_bills(denomination, number_of_bills):
    """Calculate the number of currency within the amount

    :param denomination: int - the value of a single unit
    :param number_of_bills: int - the total number of units
    :return: int - calculated the value of the units
    """
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """Calculating amount of currency units withing the amount

    :param amount: float - the total starting value
    :param denomination: int - the value of the single unit
    :return: int - the number of unit that can be obtained withing the amount
    """
    return amount // denomination



def get_leftover_of_bills(amount, denomination):
    """Calculate leftover amount after exchanging into bills

    :param amount: float - the total starting value
    :param denomination: int - the valur of a single unit
    :return: float - the 'amount' that counts as a leftover after the denomination
    """
    return amount % denomination



def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Calculate the maximum value of the current currency

    :param budget: float - the amount of money planned to be exchanged
    :param denomination: int - the value of a single unit
    :param exchange_rate: float - the unit value of the foreign currency
    :param spread: int - the percentage that is taken as an exchange fee
    :return: int - the maximum value available from the new currency
    """
    percentile = spread / 100
    new_exchage_rate = exchange_rate + (exchange_rate * percentile)
    total = budget / new_exchage_rate
    return int(total / denomination) * denomination

