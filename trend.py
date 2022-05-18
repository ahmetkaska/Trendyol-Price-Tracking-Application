import requests
from bs4 import BeautifulSoup
from ePosta import sendMail
import time

url1="https://www.trendyol.com/grimelange/norm-erkek-grimelanj-duz-renk-kolej-yaka-regular-fit-ceket-p-98099136?boutiqueId=605401&merchantId=165724"



def checkPrice(url,paramPrice):
    headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
    }

    page = requests.get(url, headers=headers)

    htmlPage = BeautifulSoup(page.content,'html.parser')

    productTitle=htmlPage.find("h1", class_="pr-new-br").getText()

    price = htmlPage.find("span",class_="prc-dsc").getText()

    image = htmlPage.find("img", class_="js-image-zoom__zoomed-area")

    convertedPrice = float(price.replace(",",".").replace(" TL",""))

    if(convertedPrice <= paramPrice):
        print("Ürün fiyatı düştü")
        htmlEmailContent= """\
            <html>
            <head></head>
            <body>
            <h3>{0}</h3>
            <br/>
            {1}
            <br/>
            <p>Ürün linki: {2}</p>
            </body>
            </html>
            """.format(productTitle, image, url)
        sendMail("testkaska36@gmail.com","Ürünün fiyatı düştü👍👍", htmlEmailContent)
    else:
        print("ürün fiyatı düşmedi")

while(True):
    checkPrice(url1,150)
    time.sleep(3)
