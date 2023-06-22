# amazon-price-recorder-and-displayer
We use websites like amazon.in, flipkart.in to buy
products on these days because the price is cheaper in it.
But when?... Here is a price tracker to track the change in
price of products and represent it in a graphical format
and also stores it in a database.

This program uses ASIN (Amazon Standard
Identification Number) stored in a csv file and scrap data
from the website using beautiful soup library. Then it
stores the data in a database file using sqlite3 library.
This part of program can be run periodically by a server
or by a single board computer like Raspberry Pi.

Then the other part of the program can be executed
to extract data from database file using pandas library
and visualized as a graph using matplotlib library.

This project will be helpful for people who waiting for
drop in price of a particular product. Also, data analyst
can use the data to study the changes in price of
products.
