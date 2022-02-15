from audioop import add

def print_name():
    print("Jadrukis")

def test_dict():
    print("---------- Dictionary -------------")

    me = {

    "first" : "Jadro",
    "last": "Alain",
    "age": "22",
    "hobbies":[],
    "address":{
        "street": "Huapango",
        "city": "Tijuana"
    }
}

    print(me["first"] + "" + me["last"])

    address = me ["address"]
    #print(address["street"] + "" address ["city"])

def younger_person():
    ages = [12,42,32,50,56,14,78,30,51,89,12,38,67,10]

    pivot = ages[0]
    for age in ages:
        if age < pivot:
            pivot = age
    
    print(f"The Result is: {pivot}")

print_name()
test_dict()