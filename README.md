# discount notifier
a python script to produce desktop notifications when there is a discount in products i like from a [shoes shop](https://www.epapoutsia.gr)
## usage
1. install python3.6 or later
2. `pip3 install -r requirements.txt`
3. add the links of the item you want to be notified for in wishlist.txt (tap enter after each link)
4. `python3 notifier.py`
## how it works
this e-shop uses a div element with a special class name to display the new price after discount of a product,
so i used requests_html & bs4 libraries to get the HTML text and check if there is a div that contains a special price.
## use on other e-shops
