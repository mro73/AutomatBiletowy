import ticket

class Cart:
    def __init__(self) -> None:
        self.tickets:list[ticket.Ticket] = []
        self.value = 0.0
    
    def add_ticket(self, item:ticket.Ticket):
        self.tickets.append(ticket)
        self.value += ticket.get_price()

    def display(self) -> None:
        print("Zawartość koszyka:")
        for index, item in enumerate(self.tickets):
            print(f"{index+1}. {item.display_ticket()} \t {item.get_price()} zł")
        print(f"Wartość koszyka: \t {self.value} zł")
        
    def get_value(self) -> float:
        return self.value
    
    def recalculate_cart(self) -> float:
        self.value = sum(item.price for item in self.tickets)
        return self.value