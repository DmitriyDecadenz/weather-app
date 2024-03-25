import requests
from bs4 import BeautifulSoup
import logging


class Weather():
    def __init__(self, city):
        self.city = city
        self.url = "https://www.google.com/search?q=погода+в+"
        self.headers = {
            "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }

    def check_weather(self):
        """Find and Return data"""
        responce = requests.get(
            f"{self.url}+{self.city}", headers=self.headers)
        soup = BeautifulSoup(responce.text, "html.parser")
        temperature = soup.select("#wob_tm")[0].getText()
        time = soup.select("#wob_dts")[0].getText()

        return temperature, time, self.city


class log:

    def log_to_file(data) -> None:
        """logging data"""
        logger = logging.getLogger(__name__)
        logging.basicConfig(filename="log.txt", level=logging.INFO)
        logging.info(data)


class Program():

    def __init__(self):
        self.city_name = self._ask_city()
        self.weatherapp = Weather(self.city_name)
        self.log_data = log

    def display(self) -> None:
        data = self.weatherapp.check_weather()
        print(data)
        self.log_data.log_to_file(data)

    def _ask_city(self):
        city = input("Город: ")
        return city


if __name__ == "__main__":
    app = Program()

    app.display()
