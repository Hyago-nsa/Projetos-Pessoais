from bs4 import BeautifulSoup
import lxml
import smtplib
import requests

url = "https://www.amazon.com.br/Eloquent-JavaScript-3rd-Introduction-Programming/dp/1593279507/ref=sr_1_7?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=javascript&qid=1628344549&s=books&sr=1-7&ufe=app_do%3Aamzn1.fos.fcd6d665-32ba-4479-9f21-b774e276a678"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62",
    "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "content-type": "text"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, "lxml")

# Product price 
BUY_PRICE = 150

price = soup.find(id="price").get_text()
price_replace = price.replace(u'\xa0', u' ')
price_without_currency = price_replace.split("R$")[1]
price_without_space = price_without_currency.split(" ")[1]

price_replace = price_without_space.replace(",", ".")
price_as_float = float(price_replace)

print(price_as_float)

# Product title

title = soup.find(id="productTitle").get_text().strip()
print(title)

# Send email

if price_as_float >= BUY_PRICE:
    mail_from= "hyago.nsa.bot@gmail.com"
    mail_to = ["hyago.eurico.nsa@gmail.com"]
    mail_subject = "A product is on price!"
    mail_message = f"Hey!\n{title} is now R${price_as_float}\n{url}"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login("hyago.nsa.bot@gmail.com", "mumumu2556")
        connection.sendmail(
            from_addr=mail_from,
            to_addrs=mail_to,
            msg=f"Subject:{mail_subject}\n{mail_message}"
        )
