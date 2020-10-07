# discount notifier
a python script to produce desktop notifications when there is a discount in products i like from a [shoe shop](https://www.epapoutsia.gr)

## how it works
this e-shop uses a div element with a special class name to display the special price after discount of a product,
so i used requests_html & bs4 to get the HTML text and check if there is a div that contains a special price.
