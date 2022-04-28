EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_time):
    """
    Return the remaining bake time.

    This function takes a number representing the time already spent baking and calculates the
    """
    return EXPECTED_BAKE_TIME - elapsed_time


def preparation_time_in_minutes(layers):
    """
    Return the total time it takes to prepare the lasagna layers.

    This function takes a number representing the number of layers and calculates the total time
    """
    return PREPARATION_TIME * layers


def elapsed_time_in_minutes(layers, elapsed_time):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return (layers * PREPARATION_TIME) + elapsed_time
