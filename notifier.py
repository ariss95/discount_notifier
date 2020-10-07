import notify2
from bs4 import BeautifulSoup as soup
from requests_html import HTMLSession

s = HTMLSession()

def get_items():
    file1 = open("wishlist.txt", "r")
    items = file1.readlines()
    return items

def check_for_discount():
    items = get_items()
    for item in items:
        item = item.strip("\n") #remove newline character from the url
        
        doc = s.get(item).text
        item = soup(doc, "html.parser")
        special_price = item.findAll("div", {"class": "e-product-price__special"})
        if special_price != []:
            print ("product has discount")
        else:
            print("no discount")

notify2.init("discount notifier")
n = notify2.Notification("", "")

check_for_discount()
#TODO show notification for products
#n.show()