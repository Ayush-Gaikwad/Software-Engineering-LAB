
import math


def parse_reading(text):
    if not isinstance(text, str):
        raise ValueError("Reading must be a string")

    parts = text.split('/')

    if len(parts) != 2:
        raise ValueError("Reading must contain temperature/humidity")

    try:
        temp = float(parts[0])
        humidity = int(parts[1])
    except ValueError:
        raise ValueError("Temperature and humidity must be numeric")

    if not math.isfinite(temp):
        raise ValueError("Temperature must be finite")

    if not 0 <= humidity <= 100:
        raise ValueError("Humidity must be between 0 and 100")

    return temp, humidity


def wind_category(speed_text):
    if not isinstance(speed_text, str) or not speed_text.strip():
        raise ValueError("Wind speed must be a valid string")

    try:
        speed = int(speed_text)
    except ValueError:
        raise ValueError("Wind speed must be an integer")

    if speed < 0:
        raise ValueError("Wind speed cannot be negative")

    if speed >= 89:
        return 'warning'
    if speed >= 39:
        return 'advisory'
    return 'none'


def rainfall_spread(readings_csv):
    if not isinstance(readings_csv, str) or not readings_csv.strip():
        raise ValueError("Rainfall readings must be a non-empty string")

    try:
        readings = [float(r.strip()) for r in readings_csv.split(',')]
    except ValueError:
        raise ValueError("Rainfall readings must contain valid numbers")

    if not readings:
        raise ValueError("At least one rainfall reading is required")

    if not all(math.isfinite(r) and r >= 0 for r in readings):
        raise ValueError("Rainfall values must be finite and non-negative")

    return max(readings) - min(readings)


def main():
    print("==== Running parse_reading ====")
    user_input = input("Enter temperature/humidity (e.g. 35.5/80): ")

    try:
        result = parse_reading(user_input)
        print("Temperature and Humidity:", result)
    except ValueError as e:
        print("Invalid reading:", e)

    print("\n==== Running wind_category ====")
    user_input = input("Enter a wind speed in km/h (e.g. 45): ")

    try:
        result = wind_category(user_input)
        print("Wind Category:", result)
    except ValueError as e:
        print("Invalid wind speed:", e)

    print("\n==== Running rainfall_spread ====")
    user_input = input("Enter hourly rainfall in mm as CSV (e.g. 2,5.5,10): ")

    try:
        result = rainfall_spread(user_input)
        print("Rainfall Spread:", result)
    except ValueError as e:
        print("Invalid rainfall readings:", e)


if __name__ == "__main__":
    main()
