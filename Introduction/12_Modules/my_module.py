# Testing module

def sumValue(*args):
    total = 0
    for i in args:
        total += i
    return total

def printValue(value):
    print((value))

gravity = 9.81

person = {
    "name" : "Ernesto Gonzales",
    "phoneNumber" : "9999999",
    "address" : {
        "city" : "Quito",
        "street" : "New avenue"
    }
}