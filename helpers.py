import json
import os

# # a function to read the required html page
def get_page(page_name):
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

# # a function that will add a new product to db
def add_product_toDB(name, qty, price,date):
    product_info = [name, qty, price, date]
    info_str = json.dumps(product_info)
    file = open("productsdb.txt", "a")
    file.write(info_str + "\n")
    file.close()

#  function to rewrite to a DB with the new data(for updating a value or deleting it)
# the cb will be get_products() 
def get_new_data(new_array, cb):
    if os.path.exists("productsdb.txt"):
        os.remove("productsdb.txt")
    for product in new_array:
        add_product_toDB(product.name, product.quantity, product.price, product.date)
    products = cb()
    return products


# ### function to read from a file // mainly to read from my DB
def read_file(f):
    array = []
    # the if statement to prevent error if we tried to delete the last item 
    # so after deletion of the last item it creates the DB file again and returns empty array
    if os.path.exists(f):
        file = open(f)
        content = file.read()
        file.close()
        array = content.split("\n")
    else:
        file = open(f, "x")
        file.close()
    return array


# a function for searching for a product by its name to remove it
#cb will be the get_products function
def filter_products(cb, name):
    products = cb()
    filtered_array = []
    for product in products:
        if product.name != name:
            filtered_array.append(product)
    return filtered_array

# a function to update the quantity of a specific object
def update_products(cb, name, qty):
    products = cb()
    updated_data = []
    for product in products:
        if product.name == name:
            product.update_amount(qty)
            updated_data.append(product)
        else:
            updated_data.append(product)
    return updated_data

# a function to check if a product is already present in a DB
def check_if_present(cb, name):
    products = cb()
    present = False
    for product in products:
        if product.name == name:
            present = True
    return present

# a function to get products in a specific date
def filter_by_date(cb, date):
    products = cb()
    filtered = []
    for product in products:
        if product.date == date:
            filtered.append(product)
    return filtered

# a function to show the final html results
def show_result(products_arr):
    actual_values = ""
    total_cost = 0
    if len(products_arr) < 1 :
        actual_values += "<p>Your shopping list is empty.</p>"
    else:
        for product in products_arr:
            total_cost += product.cal_cost()
            actual_values += "<p class=\"p\">" + product.name +" : " + str(product.quantity) + " will cost "+ str(product.cal_cost())+"</p>"
    cost_html = "<p> The total cost is : "+ str(total_cost) + " $ </p>"
    return [actual_values, cost_html]