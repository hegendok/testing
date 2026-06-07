EXPECTED_BAKE_TIME = 40
print(EXPECTED_BAKE_TIME)

def bake_time_remaining(bake_time):
    """Calculate remaining baking time
    
    Parameters:
        bake_time(int):the time baking the lasagna

    Returns:
        int: the time remaining after baking.

    This function takes one integer representing the time to bake.
        It calculates the time left from the EXPECTED_BAKE_TIME after baking.

    """
    return EXPECTED_BAKE_TIME - bake_time

print(bake_time_remaining(30))

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time per layer.

    Parameters:
        number_of_layers(int): the amount of layers used.
    
    Returns:
        int: the time needed to prep the layers.

    This function takes one integer representing
the layers taht's going to be prepared, before
then it calculates how long it has passed after
prepping the layers.
    """
    time_per_layer = 2
    return time_per_layer * number_of_layers

print(preparation_time_in_minutes(1))

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the combined time.

    Parameters:
        number_of_layers(int): the amount of layers used.
        elapsed_bake_time(int): time that has past after baking.

    Returns:
        int: the time the has passed after prepping the layers and baking.

    This function takes two integer one representing the amount of lasagna
layers used and the other representing the time the has passed from baking.
It then calculates how long time has passed after all of it.
    """
    preparation_time_in_minutes(number_of_layers)
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

print(elapsed_time_in_minutes(3, 20))
