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

    #copilot sugggested: raise ValueError("weight_grams must be non-negative (got a negative value).") ACCEPTED.

        raise ValueError("weight_grams must be non-negative (got a negative value).")

    flight_time = 180 - 0.1 * weight_grams

    #copilot suggested: if flight_time < 0: ACCEPTED.

    if flight_time < 0:
        return 0

    return flight_time

    #copilot sugggested: 
    #def flight_time_table(max_weight_grams, step_grams):

	#if max_weight_grams < 0:
	#raise ValueError("max_weight_grams must be non-negative")
	#if step_grams <= 0:
	#raise ValueError("step_grams must be greater than zero")

	#return list(range(0, max_weight_grams + 1, step_grams))
    #REJECTED.
    

def flight_time_table(max_weight_grams, step_grams):
    """
        Build a table of (weight, flight_time) pairs across a payload range.
    
        Parameters:
            max_weight_grams (int or float): Largest payload weight, in grams.
            step_grams (int or float): Increment, in grams, between rows.
    
        Returns:
            list[tuple[float, float]]: (weight, flight_time) pairs, lightest to heaviest.
    """
    if step_grams <= 0:

    #copilot sugggested: raise ValueError("step_grams must be greater than 0.") ACCEPTED.

        raise ValueError("step_grams must be greater than 0.")

    table = []
    weight = 0

    while weight <= max_weight_grams:

    #copilot suggested: while weight > 0: print("Current weight:", weight) weight -= 1 EDITED.
        
        table.append((weight, calculate_flight_time(weight)))
        weight += step_grams

    return table

    