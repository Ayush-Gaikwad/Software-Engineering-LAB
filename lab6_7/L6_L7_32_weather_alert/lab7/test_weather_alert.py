
import math
import pytest
from hypothesis import given, strategies as st

from weather_alert import parse_reading, wind_category, rainfall_spread


# FUZZ TEST 1: PARSE READING

@given(st.one_of(st.text(), st.none()))
def test_parse_reading_no_unexpected_crash(s):
    try:
        result = parse_reading(s)
        assert isinstance(result, tuple)
        assert math.isfinite(result[0])
        assert 0 <= result[1] <= 100
    except ValueError:
        pass


@given(
    st.floats(allow_nan=False, allow_infinity=False),
    st.integers(min_value=0, max_value=100)
)
def test_parse_reading_valid(temp, humidity):
    result = parse_reading(f"{temp}/{humidity}")
    assert result == (temp, humidity)


# FUZZ TEST 2: WIND CATEGORY

@given(st.one_of(st.text(), st.none()))
def test_wind_category_no_unexpected_crash(s):
    try:
        result = wind_category(s)
        assert result in ["none", "advisory", "warning"]
    except ValueError:
        pass


@given(st.integers(min_value=0))
def test_wind_category_valid(speed):
    result = wind_category(str(speed))

    if speed >= 89:
        assert result == "warning"
    elif speed >= 39:
        assert result == "advisory"
    else:
        assert result == "none"


# FUZZ TEST 3: RAINFALL SPREAD

@given(st.one_of(st.text(), st.none()))
def test_rainfall_spread_no_unexpected_crash(s):
    try:
        result = rainfall_spread(s)
        assert math.isfinite(result)
        assert result >= 0
    except ValueError:
        pass


@given(
    st.lists(
        st.floats(
            min_value=0,
            allow_nan=False,
            allow_infinity=False
        ),
        min_size=1
    )
)
def test_rainfall_spread_valid(readings):
    csv = ",".join(str(r) for r in readings)
    result = rainfall_spread(csv)

    assert result == max(readings) - min(readings)


# EXPLICIT INVALID INPUT TESTS

@pytest.mark.parametrize("value", [None, "", "abc", "20/30/40", "nan/50"])
def test_invalid_parse_reading(value):
    with pytest.raises(ValueError):
        parse_reading(value)


@pytest.mark.parametrize("value", [None, "", "abc", "-10", "45.5"])
def test_invalid_wind_category(value):
    with pytest.raises(ValueError):
        wind_category(value)


@pytest.mark.parametrize("value", [None, "", "abc", "-5,10", "nan,5", "1,,3"])
def test_invalid_rainfall_spread(value):
    with pytest.raises(ValueError):
        rainfall_spread(value)
