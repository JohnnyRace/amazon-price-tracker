import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = ""
MY_PASSWORD = ""

# from http://myhttpheader.com/
headers = {
    'Accept-Language': '',
    'User-Agent': ''
}

product_link = ''

response = requests.get(product_link, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
name_of_product = soup.find(id="productTitle").get_text().strip()
price_tag = soup.find(id="priceblock_ourprice")
# <span class="a-size-medium a-color-price priceBlockBuyingPriceString" id="priceblock_ourprice">$119.95</span>
price = float(price_tag.get_text().split('$')[1])

if price < 200:
    message = f"{name_of_product} is now {price}"
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{product_link}"
        )
