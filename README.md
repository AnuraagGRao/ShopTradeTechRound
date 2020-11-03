# ShopTradeTechRound

## How to run?

- Install Python
- Install Flask [ pip install flask ]
- Run the app using > python run.py

## APIs 

### POST /api/customer (Creates a new customer)

#### Example input - {"first_name":"XXXXX", "last_name":"XXXXX", "email":"XXXXX", <"phone":"xxxxxxxxx">} 
#### <Non required arguments>
#### Output - {"customer":{//all customer details including id, email, etc}}

### PUT /api/customer (Updates the customer)

#### Example input - {"customer_id":"xxxxxxx",<"first_name":"XXXXX", "last_name":"XXXXX", "email":"XXXXX", "tags":"xxxx,xxxx,xxx">}
#### <Non required arguments>
#### Output - {"customer":{//all customer details including id, email, etc}}

### POST /api/orders (Creates a new order)

#### Requires variant_id and variant_quantity.
#### Output - {"order":{order details.}}
