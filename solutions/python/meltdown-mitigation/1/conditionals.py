"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced
    :param temperature: float or int - the temperature value in kelvin
    :param neutrons_emited: float or int - the number of neutrons emitted per second
    :return: bool - Is the criticality ballanced?
    :note: conditions - for the reactor to be balanced in the criticality.
                -> the temp is less than 800K
                -> neutrons emitted per second is greater than 500
                -> the product of temp and neutrons emitted per second is less than 500000.
    """
    product_of_temp_and_neutrons_emitted = temperature * neutrons_emitted
    if temperature < 800 and neutrons_emitted > 500 and product_of_temp_and_neutrons_emitted < 500000:
        return True
    else:
        return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone
    :param voltage: int or float - Voltage value
    :param current: float or int - Current value
    :param theoretical_max_power: int or float - the power level that corresponds to 100% effciency
    :return: str - either ('Green', 'Orange', 'Red', or 'Black')
    :note: conditions - Efficiency can be grouped to 4 criteria.
            -> green - 80% or more efficiency
            -> orange - less than 80%, more than 60% efficiency
            -> red - its below 60%, but above 30%
            -> black - less than 30% efficiency
           The pecentage are calculated with (generated power/ theoretical max power) * 100
           where generated power = voltage * current
    """
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100
    if efficiency >= 80:
        return "green"
    elif efficiency >= 60:
        return "orange"
    elif efficiency >= 30:
        return "red"
    else:
        return "black"




def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Asses and return status code for the reactor
    :param temperature: int or float - the value of temperature in kelvin
    :param neutrons_produced_per_second: int or float - the neutron flux
    :param threshold: int or float - the threshold of the category
    :return: str - either ('LOW', 'NORMAL', or 'DANGER')
    :note: conditions -
            -> 'LOW': temperature * neutrons_produced_per_second < 90% of the treshold
            -> 'NORMAL': temperature * neutrons_produced_per_second +/- 10% threshold
            -> 'DANGER': temperature * neutrons_produced_per_second is not in the above-stated ranges
    """
    product_of_temp_and_npps = temperature * neutrons_produced_per_second
    ninety_percent = threshold * 0.9
    ten_percent = threshold * 1.1

    if product_of_temp_and_npps <= ninety_percent:
        return "LOW"
    elif (
        product_of_temp_and_npps <= ten_percent
        or product_of_temp_and_npps == ten_percent
    ):
        return "NORMAL"
    elif product_of_temp_and_npps > ten_percent:
        return "DANGER"