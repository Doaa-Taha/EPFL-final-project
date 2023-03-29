import flask
import json
from helpers import *

app = flask.Flask("products")

# # define a class function to be the blueprint of product
class Product:

    def __init__(self, name, quantity, price, date) :
        self.name = name
        self.quantity = int(quantity)
        self.price = float(price)  
        self.date = date
    # define the methods here
    def cal_cost(self):
        return self.price * self.quantity
    def update_amount(self, new_amount) :
        if self.quantity:
            self.quantity = new_amount


# a function to read from the database and returns array of objects (class instances)
def get_products():
    products = read_file("productsdb.txt")
    # # here products are array of json arrays
    array_of_products = []
    parsed = []
    for product in products:
        # now product is a python array after using json.loads
        if len(product) > 0 :
            parsed = json.loads(product) 
            product_obj = Product(parsed[0], parsed[1], parsed[2], parsed[3])
            array_of_products.append(product_obj)
            # type of "array_of_products" is array of object instances
    return array_of_products

# # define routes with their functions

@app.route("/")
def homepage():
    html_page = get_page("index")
    return html_page

@app.route("/login")
def login_page():
    html_page = get_page("login")
    return html_page

@app.route("/delview")
def senddel():
    html_page = get_page("delview")
    return html_page

@app.route("/updtview")
def sendupdt():
    html_page = get_page("updtview")
    return html_page

@app.route("/srchview")
def sendsrch():
    html_page = get_page("srchview")
    return html_page

@app.route("/add")
def add_product():
    html_page = get_page("products")
    error_page = get_page("error")
    product_name = flask.request.args.get("product").strip().lower()
    product_qty = flask.request.args.get("quantity")
    product_price = flask.request.args.get("price")
    shopping_date = flask.request.args.get("date")
    # check the product is not added before
    if check_if_present(get_products, product_name) == True:
        return error_page
    else:
        add_product_toDB(product_name, product_qty, product_price, shopping_date)
        products = get_products()
        result = show_result(products)
        return html_page.replace("$$PRODUCTS$$", str(result[0])).replace("$$COST$$", str(result[1]))


@app.route("/products")
def productspage():
    html_page = get_page("products")
    products = get_products()
    result = show_result(products)
    return html_page.replace("$$PRODUCTS$$", str(result[0])).replace("$$COST$$", str(result[1]))


@app.route("/delete")
def delete():
    html_page = get_page("products")
    prod_name = flask.request.args.get("productname").strip()
    filtered_array = filter_products(get_products, prod_name.lower())
    products = get_new_data(filtered_array, get_products)
    result = show_result(products)
    return html_page.replace("$$PRODUCTS$$", str(result[0])).replace("$$COST$$", str(result[1]))



@app.route("/update")
def update_item():
    html_page = get_page("products")
    name = flask.request.args.get("name").strip()
    new_quantity = flask.request.args.get("quantity")
    updated_data = update_products(get_products, name.lower(), new_quantity)
    products = get_new_data(updated_data, get_products)
    result = show_result(products)
    return html_page.replace("$$PRODUCTS$$", str(result[0])).replace("$$COST$$", str(result[1]))

   
    
@app.route("/search")
def search():
    html_page = get_page("products")
    date = flask.request.args.get("date")
    products = filter_by_date(get_products, date)
    result = show_result(products)
    return html_page.replace("$$PRODUCTS$$", str(result[0])).replace("$$COST$$", str(result[1]))
  