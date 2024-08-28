def make_pizza(*toppings,base):
    print(toppings,base)
suraj =make_pizza("mushrrom","tomato",base="cheese")

def make_pizza2(base, *toppings):
    print(toppings,base)
suraj =make_pizza2("mushrrom","tomato","cheese")