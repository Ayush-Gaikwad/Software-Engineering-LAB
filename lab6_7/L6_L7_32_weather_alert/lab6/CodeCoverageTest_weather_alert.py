
import pytest

from weather_alert import (
    wind_alert,
    rain_alert,
    heat_alert,
    overall_alert
)


# WIND ALERT TESTS

@pytest.mark.parametrize("speed, expected", [
    (0, "none"),
    (38, "none"),
    (39, "advisory"),
    (61, "advisory"),
    (62, "watch"),
    (88, "watch"),
    (89, "warning"),
    (120, "warning"),
])
def test_wind_alert(speed, expected):
    assert wind_alert(speed) == expected


# RAIN ALERT TESTS

@pytest.mark.parametrize("rain, saturated, expected", [
    (0, False, "none"),
    (9, False, "none"),
    (10, False, "advisory"),
    (10, True, "watch"),
    (49, False, "advisory"),
    (49, True, "watch"),
    (50, False, "watch"),
    (50, True, "warning"),
    (80, False, "watch"),
    (80, True, "warning"),
])
def test_rain_alert(rain, saturated, expected):
    assert rain_alert(rain, saturated) == expected


# HEAT ALERT TESTS

@pytest.mark.parametrize("temp, humidity, expected", [
    (20, 40, "none"),
    (34, 40, "none"),
    (35, 40, "advisory"),
    (39, 40, "advisory"),
    (40, 40, "watch"),
    (44, 40, "watch"),
    (45, 40, "warning"),
    (30, 60, "none"),
    (34, 60, "advisory"),
    (39, 60, "watch"),
    (44, 60, "warning"),
])
def test_heat_alert(temp, humidity, expected):
    assert heat_alert(temp, humidity) == expected


# OVERALL ALERT TESTS

def test_overall_alert_empty():
    assert overall_alert([]) == "none"


@pytest.mark.parametrize("alerts, expected", [
    (["none"], "none"),
    (["advisory"], "advisory"),
    (["watch"], "watch"),
    (["warning"], "warning"),
    (["none", "advisory"], "advisory"),
    (["advisory", "watch"], "watch"),
    (["watch", "warning"], "warning"),
    (["warning", "none"], "warning"),
    (["advisory", "none", "watch"], "watch"),
])
def test_overall_alert(alerts, expected):
    assert overall_alert(alerts) == expected


def test_overall_alert_invalid():
    with pytest.raises(ValueError, match="unknown alert"):
        overall_alert(["invalid"])
