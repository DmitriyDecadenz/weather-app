import requests
from bs4 import BeautifulSoup
import logging


class Weather():
  
  @classmethod
  def check_weather(cls,city,userAgent):
    """send GET request to google with custom query params.
    Parsing html, find time,weather infomation.
    And doing output and logging info.
    """
    headers = {
        "User-Agent" : userAgent
        }

    responce = requests.get(f"https://www.google.com/search?q=погода+в+{city}", headers=headers)

    soup = BeautifulSoup(responce.text, "html.parser")

    temperature = soup.select("#wob_tm")[0].getText()
    time = soup.select("#wob_dts")[0].getText()
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename="log.txt", level=logging.INFO)
    logging.info(f"Город: {city}")
    logging.info(f"Время: {time}")
    logging.info(f"Температура: {temperature}C")

    print(city)
    print(time)
    print(f"Температура: {temperature}C")


class Program():
  city = str(input("Город: "))
  userAgent = str(input("User-Agent: ")) # example Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 
  # find it on https://suip.biz/ru/?act=my-user-agent
  Weather.check_weather(city=city, userAgent=userAgent)


Program()