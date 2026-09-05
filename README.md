## AI Use Disclosure

I used GitHub Copilot's inline suggestions while writing flight_calculator.py.
Accepted suggestions for the input-validation checks in both functions,
edited a suggested loop that would have printed values instead of building
the table, and rejected a suggested version of flight_time_table() that
returned a flat list of weights instead of (weight, flight_time) pairs.

I also used GitHub Copilot Chat (/tests) to generate the initial unit
test suite for calculate_flight_time(). Reviewed all 10 generated
tests line by line and verified the linear calculation, fractional
input, zero-flight-time boundary, and negative-weight ValueError
cases were all covered correctly. Verified all 10 tests pass with
pytest.