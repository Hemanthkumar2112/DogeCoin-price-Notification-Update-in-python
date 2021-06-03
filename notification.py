import time
from plyer import notification
from bs4 import BeautifulSoup
import urllib.request
import re
 
user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
header = {"user_Agent": user_agent}
url = "https://www.coindesk.com/price/dogecoin"
def update(url):
    request = urllib.request.Request(url,headers=header)
    responce = urllib.request.urlopen(request)
    page = responce.read()
    soup = BeautifulSoup(page, 'html.parser')
    results = soup.find(id='export-chart-element')
    job = results.find_all('div', class_='price-large')
    job = str(job)
    numbers = re.findall('[0-9].[0-9]+', job)
    return numbers

while True:
    numbers = update(url)
    notification.notify(title='Dogecoin', message=numbers[0], app_name='Doge_coin_price', app_icon='', timeout=10, toast=False)
    time.sleep(1000)
