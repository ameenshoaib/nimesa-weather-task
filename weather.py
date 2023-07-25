import requests

API_BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"


def get_weather_data(date):
    response = requests.get(API_BASE_URL)
    data = response.json()

    # Find the weather data for the given date
    for item in data["list"]:
        if date in item["dt_txt"]:
            return item["main"]["temp"]


def get_wind_speed_data(date):
    response = requests.get(API_BASE_URL)
    data = response.json()

    # Find the weather data for the given date
    for item in data["list"]:
        if date in item["dt_txt"]:
            return item["wind"]["speed"]


def get_pressure_data(date):
    response = requests.get(API_BASE_URL)
    data = response.json()

    # Find the weather data for the given date
    for item in data["list"]:
        if date in item["dt_txt"]:
            return item["main"]["pressure"]


def main():
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS format): ")
            temperature = get_weather_data(date)
            if temperature:
                print(f"The temperature on {date} was: {temperature:.2f}°C")
            else:
                print("Weather data not available for the given date.")
        elif choice == 2:
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS format): ")
            wind_speed = get_wind_speed_data(date)
            if wind_speed:
                print(f"The wind speed on {date} was: {wind_speed:.2f} m/s")
            else:
                print("Weather data not available for the given date.")
        elif choice == 3:
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS format): ")
            pressure = get_pressure_data(date)
            if pressure:
                print(f"The pressure on {date} was: {pressure} hPa")
            else:
                print("Weather data not available for the given date.")
        elif choice == 0:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
