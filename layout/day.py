from layout import weatherAPI
import datetime


class day:
    def __init__(self, dayDate):
        self.name = None
        self.temperature = None
        self.probabilityRain = None
        self.weather = None
        self.set_Properties(dayDate)
    
    def set_Properties(self, dayDate):
        weather = weatherAPI.weatherAPI()
        data = weather.fetch_weather()
        self.name = self.setName(dayDate)
        self.temperature = self.setTemperature(dayDate, data)
        self.weather = self.setWeather(data, dayDate)
        pass

    def setName(self, dayDate):
        date_obj = datetime.datetime.strptime(dayDate, "%Y-%m-%d")
        weekdays = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
        print(date_obj)
        return weekdays[date_obj.weekday()]

    def setTemperature(self, dayDate, data):
        for entry in data:
            if entry['dt_txt'].startswith(dayDate) and entry['dt_txt'].endswith("12:00:00"):
                kelvin = entry['temp']
                celsius = kelvin - 273.15
                return round(celsius, 1)
        for entry in data:
            if entry['dt_txt'].startswith(dayDate):
                kelvin = entry['temp']
                celsius = kelvin - 273.15
                return round(celsius, 1)
        return None

    def setWeather(self, data, dayDate):
        for entry in data:
            if entry['dt_txt'].startswith(dayDate) and entry['dt_txt'].endswith("12:00:00"):
                return entry['weather']
            if entry['dt_txt'].startswith(dayDate):
                return entry['weather']
        return None