
from flask import Flask, request, abort
from mock_data import catalog
import json
import random
from config import db
from flask_cors import CORS
from bson import ObjectId


app = Flask(__name__)
CORS(app)  # *DANGER anyone can connect to this server
me = {
    "name": "Antwone",
    "last": "Adams",
    "age": 38,
    "hobbies": [],
    "address": {"street": "Southview", "number": "83", "city": "Springfield"},
}


@app.route("/", methods=["GET"])
def home():
    return "Hello from Python"


@app.route("/test")
def any_name():
    return "I'm a test function."


@app.route("/about")
def about():
    return me["name"] + "  " + me["last"]

    # ---------------------------------------------------------------
    # ----------------------  API ENDPOINTS  ------------------------
    # ---------------------------------------------------------------


@app.route("/api/catalog")
def get_catalog():
    cursor = db.products.find({})
    results = []
    for product in cursor:
        product["_id"] = str(product["_id"])
        results.append(product)

    return json.dumps(results)


@app.route("/api/catalog", methods=["post"])
def save_product():
    product = request.get_json()
    print(product)


# data validations
# if the product does not contain a title and is at least 5 characters long
# return an error
    if not 'title' in product or len(product["title"]) < 5:
        return abort(400, 'Title is required and should be 5 characters long')

    # There should be a price
    if not 'price' in product:
        return abort(400, 'A price needs to be declared')

    #  if price is not float and not an int, error
    if not isinstance(product["price"], float) and not isinstance(product["price"], int):
        return abort(400, "Price should be a valid number")

    # validate the price should be greater than zero
    if product["price"] <= 0:
        return abort(400, 'Price must be greater than $0.00')

    # save product in the catalog
    db.products.insert_one(product)

    # {_id: ObjectId('id number')}
    product["_id"] = str(product["_id"])
    # {_id:}

    return json.dumps(product)


@app.route("/api/cheapest")
def get_cheapest():

    cursor = db.products.find({})
    cheap = cursor[0]
    for product in cursor:
        if product["price"] < cheap["price"]:
            cheap = product

    # find the cheapest product on the catalog list
    # 1 - travel the list with for loop
    # 2 - printout the price on the console
    cheap["_id"] = str(cheap["_id"])
    # return it as json
    return json.dumps(cheap)


@app.route("/api/product/<id>")
def get_product(id):
    # validate id is valid ObjectId
    if(not ObjectId.is_valid(id)):
        return abort()


    result = db.products.find_one({"_id" : ObjectId(id)})
    if not result:
       return abort(404, "id is not a valid ObjectID") # 404 = not found

       
    result["_id"] = str(result["_id"])

    return json.dumps(result)


@app.route("/api/catalog/<category>")
def get_by_category(category):
    result = []
    category = category.lower()
    for product in catalog:
        if product["category"].lower() == category:

            result.append(product)

    return json.dumps(result)


# /api/categories
# return the list of unique category names

@app.route("/api/categories")
def get_catagories():
    result = []
    for product in catalog:
        cat = product["category"]
        if cat not in result:
            result.append(cat)

    return json.dumps(result)


# GET /api/reports/prodCount
@app.route("/api/reports/prodCount")
def get_prod_count():
    count = len(catalog)
    return json.dumps(count)


@app.route("/api/reports/total")
def get_total():
    total = 0

    # print the price
    for prod in catalog:

        # print the title of each product
        # total is equal to current total plus (price times stock of current prod)
        totalProd = prod["price"] * prod["stock"]
        total += totalProd
    return json.dumps(total)


# /api/reports/highestInvestment
@app.route("/api/reports/highestInvestment")
def get_highest():
    highest = catalog[0]
    for prod in catalog:
        prod_invest = prod["price"] * prod["stock"]
        high_invest = highest["price"] * highest["stock"]

        if prod_invest > high_invest:   
            highest = prod
    return json.dumps(highest)


# start the server
app.run(debug=True)
