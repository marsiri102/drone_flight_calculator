def calculate_flight_time(weight_grams):
    """
    Calculate active flight time (minutes) for a given payload weight.

    Parameters:
        weight_grams (int or float): Payload weight in grams. Must be >= 0.

    Returns:
        float: Active flight time in minutes, floored at 0.

    Raises:
        ValueError: If weight_grams is negative.
    """
    if weight_grams < 0:
        raise ValueError("weight_grams must be non-negative (got a negative value).")

    flight_time = 180 - 0.1 * weight_grams

    if flight_time < 0:
        return 0

    return flight_time

def flight_time_table(max_weight_grams, step_grams):
    
    if step_grams <= 0:
        raise ValueError("step_grams must be greater than 0.")

    table = []
    weight = 0
    while weight <= max_weight_grams:
        table.append((weight, calculate_flight_time(weight)))
        weight += step_grams

    return table