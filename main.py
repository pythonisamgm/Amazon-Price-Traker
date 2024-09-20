import requests
from bs4 import BeautifulSoup
import smtplib

PRODUCT_URL = "https://www.amazon.es/Sony-BRAVIA-KD55X85L-pulgadas-Funciones/dp/B0BYPHSGN5/ref=sr_1_1_sspa?crid=N7INXMTNBHS4&keywords=sony+bravia+55&qid=1700937638&sprefix=SONY+BRAVIA%2Caps%2C97&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
headers = {
    "Accept-Language":"es-ES,es;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
my_email = "myaccount@gmail.com"
my_password = MY_PASSWORD

def send_mail(file_content):
    """uses smtp to send an email"""
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:

        try:
            # Do something with the SMTP connection
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="pythonisamgm@gmail.com",
                                msg="Subject:Bajada de precio en Sony Bravia...\n\n{}".format(file_content))

        finally:
            connection.quit()  # Close the connection
        #securing the email server. encrypt the mail.

response = requests.get(url=PRODUCT_URL, headers=headers)

sp = BeautifulSoup (response.text, "html.parser")


price_whole = sp.find(name="span", class_="a-price-whole").getText().split(",")[0]
price_decimals = sp.find(name="span", class_="a-price-fraction").getText()
print(price_whole)
print(price_decimals)

price_whole_int = int(price_whole)
price_decimals_int = int(price_decimals)
final_price = float("{}.{}".format(price_whole_int, price_decimals_int))

if final_price <= 1000.00 :
    file_content = ("{}.{}".format("The product you were looking for is cheaper than usual",PRODUCT_URL))
    send_mail(file_content)


