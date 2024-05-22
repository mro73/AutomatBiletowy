import json
import cart
import ticket

class Ticket_machine:
    def __init__(self) -> None:
        self.cart = cart.Cart()
        with open("ceny.json", "r", encoding="UTF-8") as jf:
            self.prices = json.load(jf) #!!

    def display_menu_json(self) -> ticket.Ticket:
        menu = self.prices
        new_ticket = ticket.Ticket()
        print("\nJaki rodzaj biletu chcesz kupić?")
        options = list(menu.keys())
        for index, option in enumerate(options):
            print(index, " - ", option)
        try:
            choice = int(input("Wybór: "))
            new_ticket.set_discount(options[choice])
            menu = menu[options[choice]]
            options = list(menu.keys())
            for index, option in enumerate(options):
                print(index, " - ", option)
            try:
                choice = int(input("Wybór: "))
                new_ticket.set_duration(options[choice])
                menu = menu[options[choice]]
                options = list(menu.keys())
                for index, option in enumerate(options):
                    print(index, " - ", option)
                try:
                    choice = int(input("Wybór: "))
                    new_ticket.set_name(options[choice])
                    new_ticket.set_price(menu[options[choice]])
                    return new_ticket
                except (ValueError, IndexError): exit()
            except (ValueError, IndexError): exit()
        except (ValueError, IndexError): exit()

    def display_menu_csv(self) -> ticket.Ticket:
        pass

    def register_payment(self):
        value = self.cart.get_value()
        try:
            payment_method = int(input("\nWybierz metodę płatności: \n0 - gotówka\n1 - karta\nWybór:"))
            if payment_method:
                input("Proszę zbliżyć kartę...")
            else:
                paid = 0
                while (paid<value):
                    paid += int(input("Wprowadź gotówkę: "))
                if paid > value:
                    print(f"Reszta: {paid-value} zł")
        except ValueError: exit()

ticket_machine = Ticket_machine()
add_another = 't'
while (add_another == 't'):
    ticket_machine.cart.add_ticket(ticket_machine.display_menu_json())
    add_another = input("\nCzy chcesz dodać kolejny bilet? (t/n) ")
ticket_machine.cart.display()
ticket_machine.register_payment()
input("Drukowanie biletów, proszę czekać...")
print("Dziękujemy za skorzystanie z automatu biletowego. Zapraszamy ponownie!")
