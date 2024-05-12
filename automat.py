import json
import cart
import ticket

class Ticket_machine:
    #cart = aaaaaa

with open("ceny.json", "r", encoding="UTF-8") as jf:
    prices = json.load(jf)

def display_menu(menu):
    print("Jaki rodzaj biletu chcesz kupić?")
    options = list(menu.keys())
    for index, option in enumerate(options):
        print(index, " - ", option)
    try:
        choice = int(input("Wybór: "))
        try:
            if isinstance(menu[options[choice]], dict):
                return display_menu(menu[options[choice]])
            else: 
                return (options[choice],menu[options[choice]])
        except IndexError: exit()
    except ValueError: exit()
        

def display_cart(cart):
    print("Zawartość koszyka: ")
    for index, item in enumerate(cart):
        print(f"{index+1}. bilet {item[0]} \t {item[1]} zł")
    value = sum(item[1] for item in cart)
    print(f"Wartość koszyka: \t {value} zł")
    return value

def register_payment(value):
    try:
        payment_method = int(input("Wybierz metodę płatności: \n0 - gotówka\n1 - karta\nWybór:"))
        if payment_method:
            input("Proszę zbliżyć kartę...")
        else:
            paid = 0
            while (paid<value):
                paid += int(input("Wprowadź gotówkę: "))
                if paid > value:
                    print(f"Reszta: {paid-value} zł")
    except ValueError: exit()
            
cart = []
add_another = 't'
while (add_another == 't'):
    cart.append(display_menu(prices))
    add_another = input("Czy chcesz dodać kolejny bilet? (t/n) ")
total = display_cart(cart)
register_payment(total)
input("Drukowanie biletów, proszę czekać...")
print("Dziękujemy za skorzystanie z automatu biletowego. Zapraszamy ponownie!")

#tickets = prices.copy()
#while(isinstance(tickets, dict)):
#    tickets = display_menu(prices)


#if isinstance(tickets, dict):
#    tickets = display_menu(tickets)
#if isinstance(tickets, dict):
#    tickets = display_menu(tickets)



#for key in tickets.keys():
 #   print(key[0], " - ", key)

#decision2 = input("Jaki typ biletu chcesz kupić:\no - okresowy\nc - czasowy\nj - jednorazowy\nwybór:")
#print(decision1, decision2)
    
#print(decision1, decision2, decision3, sep="\n")
