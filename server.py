from flask import Flask, abort, request
from mock_data import catalog
from about import me, test
import json
import random


app = Flask("server")


@app.route("/", methods=["get"])
def home_page():
    return"Under Construction"

@app.route("/about")
def about_me():
    return"Jadro Montes"

@app.route("/myaddress")
def get_address():
    test()
    address = me["address"]
    #return address ["street"] + "" + address ["city"]
    return f"{address['street']} {address['city']}"

@app.route("/test")
def test():
    return"Im a simple test"

####API####


@app.route("/api/catalog")
def get_catalog():
    return json.dumps(catalog)

##########################################################################################
app.route("/api/catalog", methods =["POST"])
def save_product ():
    product = request.get_json()

    if not "title" in product:
        return abort(400, "There should be something... but we are working in that:p")

    if not "price" in product:
        return abort(400, "Price is requerid")

    if not isinstance(product["price"], int) and not isinstance(product["price"], float):
        return abort(400, "Price is invalid")

    if product["price"] <= 0:
        return abort(400, "Price should be greater than zero ")


    product["_id"] = random.randint(10000,50000)
    catalog.append(product)

    return json.dumps(product)

@app.route("/api/catalog/count")
def get_count():
    count = len(catalog)
    return json.dumps(count)

@app.route("/api/catalog/sum")
def get_sum():
    total = 0
    for prod in catalog:
        total += prod["price"]
    
    res = f"$ {total}"
    return json.dumps(res)

@app.route("/api/product/<id>")
def get_product(id):
    for prod in catalog:
        if id == prod["_id"]:
            return json.dumps(prod)

    return abort(404) 

@app.route("/api/product/most_expensive")
def get_most_expensive():
    pivot = catalog[0]

    for prod in catalog:
        if prod["price"] > pivot["price"]:
            pivot = prod
    
    return json.dumps(pivot)

@app.route("/api/categories")
def get_categories():

    res = []
    for prod in catalog:
        category = prod["category"]

        if not category in res:
            res.append(category)
    
    return json.dumps(res)


@app.route("/api/categories/<catagory>")
def products_by_category(category):

    res = []
    for prod in catalog:
        if prod ["category"] == category:
            res.append(prod)
    
    return json.dumps(res)


  
        
# # # # # # # # # # # # # # # # # # 
            #Coupons Code
# # # # # # # # # # # # # # # # # # 

# # # # # # # # # # # # # # # # # # 

coupons = []

@app.route("/api/coupons", methods = ["POST"])
def get_coupons():
    return json.dumps(coupons)

@app.route("/api/coupons")
def save_coupon():
    coupon = request.get_json()
    coupon ["_id"] = random.randint(500,900)
    coupons.append(coupon)

    return json.dumps(coupon)

@app.route("/api/coupons/<code>")
def get_coupon_by_code(code):
    for coupon in coupons:

        if coupon ["code"] == code:
            return json.dumps(coupon)
    
    return abort(404)

#Start the server
app.run(debug = True)