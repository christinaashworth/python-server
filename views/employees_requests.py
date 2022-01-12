EMPLOYEES = [
    {
        "id": 1,
        "name": "Tasha Peter",
        "locationId": 2
    },
    {
        "id": 2,
        "name": "Zach Taylor",
        "locationId": 1
    },
    {
        "id": 3,
        "name": "Mollie Goforth",
        "locationId": 2
    },
    {
        "id": 4,
        "name": "Aja Washington",
        "locationId": 1
    }
  ]

def get_all_employees():
    return EMPLOYEES
# Function with a single parameter
def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee
