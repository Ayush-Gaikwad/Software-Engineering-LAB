
import pytest

from weather_alert import (
    wind_alert,
    rain_alert,
    heat_alert,
    overall_alert
)


# WIND ALERT: True and False branches

@pytest.mark.parametrize("speed, expected", [
    (20, "none"),
    (38, "none"),
    (39, "advisory"),
    (61, "advisory"),
    (62, "watch"),
    (88, "watch"),
    (89, "warning"),
    (100, "warning"),
])
def test_wind_branches(speed, expected):
    assert wind_alert(speed) == expected


# RAIN ALERT: All nested branches

@pytest.mark.parametrize("rain, saturated, expected", [
    (5, False, "none"),
    (10, False, "advisory"),
    (10, True, "watch"),
    (49, False, "advisory"),
    (49, True, "watch"),
    (50, False, "watch"),
    (50, True, "warning"),
    (80, False, "watch"),
    (80, True, "warning"),
])
def test_rain_branches(rain, saturated, expected):
    assert rain_alert(rain, saturated) == expected


# HEAT ALERT: All decision branches

@pytest.mark.parametrize("temp, humidity, expected", [
    (20, 30, "none"),
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
def test_heat_branches(temp, humidity, expected):
    assert heat_alert(temp, humidity) == expected


# OVERALL ALERT: Loop and conditional branches

def test_overall_empty():
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
def test_overall_branches(alerts, expected):
    assert overall_alert(alerts) == expected


def test_overall_invalid_alert():
    with pytest.raises(ValueError, match="unknown alert"):
        overall_alert(["invalid"])
