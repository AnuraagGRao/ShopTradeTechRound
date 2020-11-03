# ------------ Imports -------------------

from tool import app, sk
from flask import render_template, flash, url_for, request, jsonify
import requests

# ----------------------------------------

# ------------ routes.py -----------------

# Home / Index page route.
@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html")

# List of all the customers.
@app.route("/customers", methods=["GET"])
def customers():
    url = sk.STORE_DOMAIN+"admin/api/2020-10/customers.json"
    result = requests.get(url, auth=(sk.API_KEY, sk.API_PASSWORD))
    if result.ok:
        customers = result.json()["customers"]
        return render_template("customers.html", customers=customers)
    else:
        flash("Something went wrong! "+ result)
        return render_template("customers.html", customers=[])

# View and Edit customer details.
@app.route("/customer", methods=["GET", "POST"])
def customer():
    if request.method == "POST":
        data = request.form
        url = sk.STORE_DOMAIN+f"admin/api/2020-10/customers/{data['cid']}.json"
        payload = {
            "customer" : {
                "id" : data.get('cid'),
                "first_name" : data.get('first_name'),
                "last_name" : data.get('last_name'),
                "email" : data.get('email'),
                "tags" : data.get('tags')
            }
        }
        result = requests.put(url, auth=(sk.API_KEY, sk.API_PASSWORD), json=payload)
        if result.ok:
            customer = result.json()["customer"]
            return render_template("customer.html", customer=customer)
        else:
            flash("Something went wrong! ", result.ok)
            return render_template("customer.html", customer={})
    else:
        if request.args.get('cid'):
            url = sk.STORE_DOMAIN+f"admin/api/2020-10/customers/{request.args['cid']}.json"
            result = requests.get(url, auth=(sk.API_KEY, sk.API_PASSWORD))
            if result.ok:
                customer = result.json()["customer"]
            return render_template("customer.html", customer=customer)
    return render_template("customer.html")

# List of all orders / filtered orders.
@app.route("/orders", methods=["GET", "POST"])
def orders():
    if request.method == "POST":
        data = request.form
        url = sk.STORE_DOMAIN+f"admin/api/2020-10/orders.json?created_at_max={data.get('created_at_max')}&created_at_min={data.get('created_at_min')}&limit={data.get('limit') if data.get('limit') else '10'}"
        result = requests.get(url, auth=(sk.API_KEY, sk.API_PASSWORD))
    else:
        url = sk.STORE_DOMAIN+"admin/api/2020-10/orders.json?limit=10"
        result = requests.get(url, auth=(sk.API_KEY, sk.API_PASSWORD))
    if result.ok:
        orders = result.json()["orders"]
        print(result.json()["orders"][0].keys())
        return render_template("orders.html", orders=orders)
    else:
        flash("Something went wrong! "+ result)
        return render_template("orders.html", orders=[])

# Add customer or edit customer <API>
# first_name, last_name, email are all required fields to add a new customer.[method = POST]
# only customer_id is required to edit customer.[method = PUT]
@app.route("/api/customer", methods=["POST", "PUT"])
def apicustomer():
    try:
        if request.method == "POST":
            data = request.get_json()
            payload = {
                "customer":{
                    "first_name":data["first_name"],
                    "last_name":data["last_name"],
                    "email":data["email"],
                    "phone":data.get("phone")
                }
            }
            url = sk.STORE_DOMAIN+f"admin/api/2020-10/customers.json"
            result = request.post(url, auth=(sk.API_KEY, sk.API_PASSWORD), json=payload)
            if result.ok:
                return result.json(), 201
            else:
                return result.json(), 403
        elif request.method == "PUT":
            data = request.get_json()
            url = sk.STORE_DOMAIN+f"admin/api/2020-10/customers/{data['customer_id']}.json"
            payload = {
                "customer":{
                    "id":data['customer_id'],
                    "first_name":data["first_name"],
                    "last_name":data["last_name"],
                    "email":data["email"],
                    "phone":data.get("phone")
                }
            }
            result = requests.put(url, auth=(sk.API_KEY, sk.API_PASSWORD), json=payload)
            if result.ok:
                return result.json(), 201
            else:
                return result.json(), 403
    except Exception as err:
        return jsonify({"error":repr(err)}), 403

# Add new order api (only item variant id and quantity for now.) [method = POST]
@app.route("/api/order", methods=["POST"])
def apiorder():
    data = request.get_json()
    payload = {
        "order":{
            "line_items":[
                {
                    "variant_id": data["variant_id"],
                    "quantity": data["variant_quantity"]
                }
            ]
        }
    }
    url = sk.STORE_DOMAIN+f"admin/api/2020-10/orders.json"
    result = request.post(url, auth=(sk.API_KEY, sk.API_PASSWORD), json=payload)
    if result.ok:
        return result.json(), 201
    else:
        return result.json(), 403


# ----------------------------------------