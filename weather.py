# Name: Xinge Xu
# Student Number: 251549803
# UWO Username: XXU767
# Date Created: September 17, 2026
""" Description: Reads temperature, humidity, and wind speed from user input to calculate
    the appropriate weather index  Wind Chill Index or Humidex)
    and provides clothing recommendations based on the temperature and humidity.
"""
# 2.1 # asks user for input
temperature = int(input("Enter temperature (C): "))
humidity = float(input("Enter humidity (0 to 1): "))
wind_speed = int(input("Enter wind speed (km/h): "))

# 2.4 picks the weather index
if temperature <= 0 and wind_speed >= 5:
    # 2.2
    wind_chill_index = (13.12 + 0.6215 * temperature
                        - 11.37 * wind_speed ** 0.16
                        + 0.3965 * temperature * wind_speed ** 0.16)
    weather_index_line = "Wind Chill Index: " + str(round(wind_chill_index, 1)) + " C"
elif temperature >= 20:
    # 2.3 warm humidex if it feels 1 degree hotter
    saturation_vapour_pressure = 6.11 * 10 ** ((7.5 * temperature) / (237.3 + temperature))
    actual_vapour_pressure = humidity * saturation_vapour_pressure
    humidex = temperature + 0.5555 * (actual_vapour_pressure - 10)
    if humidex >= temperature + 1:  # rounding
        weather_index_line = "Humidex: " + str(round(humidex, 1))
    else:
        weather_index_line = "Weather Index: None"
else:
    weather_index_line = "Weather Index: None"

# 2.5 determining what type of clothing to wear based on temperature and humidity
if temperature <= -20 or (temperature <= 5 and wind_speed >= 40):
    clothing_recommendation = "Winter coat hat gloves and boots"
elif temperature <= 5:
    clothing_recommendation = "Warm coat"
elif temperature < 15:
    clothing_recommendation = "Light jacket"
elif temperature >= 25 and humidity >= 0.60:
    clothing_recommendation = "Light breathable clothing"
else:
    clothing_recommendation = "Comfortable clothing"

# 2.6 output to users!
print()
print(weather_index_line)
print("Clothing Recommendation: " + clothing_recommendation)
