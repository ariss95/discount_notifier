import notify2
from bs4 import BeautifulSoup as soup
from requests_html import HTMLSession
import schedule, time

def get_items():
    file1 = open("wishlist.txt", "r")
    items = file1.readlines()
    return items

def check_for_discount():
    items = get_items()
    for item in items:
        item = item.strip("\n") #remove newline character from the url
        
        doc = session.get(item).text #get html document
        html = soup(doc, "html.parser")
        special_price = html.findAll("div", {"class": "e-product-price__special"})
        if special_price != []:
            print ("product has discount")
            n.update("discount!",item)
            n.show()
        else:
            print("no discount")
interval = 120 #minutes, change value for shorter time between notifications
session = HTMLSession()
notify2.init("discount notifier")
n = notify2.Notification("", "")

check_for_discount()
schedule.every(interval).minutes.do(check_for_discount)
while True:
    schedule.run_pending()
    time.sleep(1)