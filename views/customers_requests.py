CUSTOMERS = [
    {
      	"id": 1,
      	"name": "Hannah Hall",
      	"email": "h@h.com"
    },
    {
      	"id": 2,
      	"name": "Mo Silvera",
      	"email": "mo@mo.com"
    },
    {
      	"id": 3,
      	"name": "Lissa Goforth",
      	"email": "lissa@lissa.com"
    },
    {
      	"email": "c@c.com",
      	"name": "Christina Ashworth",
      	"id": 4
    }
  ]

def get_all_customers():
    return CUSTOMERS
# Function with a single parameter
def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer
def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer
