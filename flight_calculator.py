def calculate_flight_time(weight_grams):
    if weight_grams < 0:
        raise ValueError("weight_grams must be non-negative (got a negative value).")

    flight_time = 180 - 0.1 * weight_grams

    if flight_time < 0:
        return 0

    return flight_time