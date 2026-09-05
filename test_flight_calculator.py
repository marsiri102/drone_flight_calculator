import pytest

from flight_calculator import calculate_flight_time


def test_zero_payload_returns_maximum_flight_time():
    """A zero-gram payload should produce the maximum flight time."""
    assert calculate_flight_time(0) == 180


def test_typical_payload_uses_linear_calculation():
    """A typical payload should reduce flight time by 0.1 minute per gram."""
    assert calculate_flight_time(500) == 130


def test_fractional_payload_returns_fractional_flight_time():
    """Decimal payload weights should be calculated accurately."""
    assert calculate_flight_time(125.5) == pytest.approx(167.45)


def test_payload_at_zero_flight_time_boundary_returns_zero():
    """A payload of 1,800 grams should result in exactly zero minutes."""
    assert calculate_flight_time(1800) == 0


def test_payload_above_boundary_is_floored_at_zero():
    """Payloads producing negative times should return zero."""
    assert calculate_flight_time(2000) == 0


def test_negative_payload_raises_value_error():
    """Negative payload weights are invalid."""
    with pytest.raises(
        ValueError,
        match=r"weight_grams must be non-negative",
    ):
        calculate_flight_time(-1)


@pytest.mark.parametrize(
    ("weight_grams", "expected_minutes"),
    [
        (1, 179.9),
        (100, 170),
        (750, 105),
        (1799, 0.1),
    ],
)
def test_calculate_flight_time_for_multiple_valid_payloads(
    weight_grams,
    expected_minutes,
):
    """The function should calculate expected values across valid inputs."""
    assert calculate_flight_time(weight_grams) == pytest.approx(expected_minutes)