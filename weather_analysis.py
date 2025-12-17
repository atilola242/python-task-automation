#Final Version for Shipd application
import math

def calculate_heat_index(temp_c, humidity):
    """
    Calculates a simplified heat index (feels-like temperature).
    This demonstrates logic and mathematical operations in Python.
    """
    if temp_c < 20:
        return temp_c  # Heat index is generally not calculated for cold temps
    
    # Simplified formula for demonstration
    heat_index = temp_c + (0.55 * (1 - (humidity / 100)) * (temp_c - 14.5))
    return round(heat_index, 2)

def analyze_weather_data(data_list):
    """
    Processes a list of daily weather dictionaries.
    Demonstrates data filtering, loops, and error handling.
    """
    if not data_list:
        raise ValueError("The data list cannot be empty.")

    results = []
    
    for entry in data_list:
        try:
            city = entry.get("city", "Unknown")
            temp = entry["temp"]
            humidity = entry["humidity"]
            
            feels_like = calculate_heat_index(temp, humidity)
            
            summary = {
                "city": city,
                "actual_temp": f"{temp}°C",
                "feels_like": f"{feels_like}°C",
                "status": "High Heat" if feels_like > 30 else "Moderate"
            }
            results.append(summary)
            
        except KeyError as e:
            print(f"Skipping invalid entry: Missing field {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    return results

# Example Usage
if _name_ == "_main_":
    sample_weather = [
        {"city": "Lagos", "temp": 32, "humidity": 80},
        {"city": "New York", "temp": 22, "humidity": 50},
        {"city": "London", "temp": 15, "humidity": 60}
    ]
    
    print("--- Weather Analysis Report ---")
    processed_data = analyze_weather_data(sample_weather)
    for report in processed_data:
        print(report)
