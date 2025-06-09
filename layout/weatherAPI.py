import requests 


class weatherAPI:
    def __init__(self):
        self.api_key = "4b1a1ff255cbda33f15760e1a8882faf"
        self.weather_data = None
        self.lat = "52.2799"
        self.lon = "8.0472"

    def fetch_weather(self, lat=None, lon=None):
        url = f"https://api.openweathermap.org/data/2.5/forecast?lat={self.lat}&lon={self.lon}&appid={self.api_key}"

        response = requests.get(url)
        if response.status_code == 200:
            self.weather_data = response.json()
            self.weather_data = self.filter_weather_data()
            return self.weather_data
        else:
            raise Exception("Error fetching weather data")

    def get_temperature(self):
        if self.weather_data:
            kelvin = self.weather_data['main']['temp']
            celsius = kelvin - 273.15  
            return round(celsius, 1) 
        return None

    def get_conditions(self):
        if self.weather_data:
            return self.weather_data['weather'][0]['main']
        return None
    
    def filter_weather_data(self):
        if self.weather_data and 'list' in self.weather_data:
            filtered_data = []
            for entry in self.weather_data['list']:
                if 'main' in entry and 'temp' in entry['main']:
                    filtered_data.append({
                        'temp': entry['main']['temp'],
                        'weather': entry['weather'][0]['main'],
                        'dt_txt': entry['dt_txt']
                    })
            return filtered_data
        return []
