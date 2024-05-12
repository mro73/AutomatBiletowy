import ticket

class Cart:
    def __init__(self) -> None:
        self.tickets = [ticket.Ticket]
        self.value = 0.0
    
    def add_ticket(self, ticket:ticket.Ticket):
        self.tickets.append(ticket)
        self.value += ticket.price

    def display(self) -> None:
        print("Zawartość koszyka:")
        for index, item in enumerate(self.tickets):
            print(f"{index+1}. bilet {item[0]} \t {item[1]} zł")
        
    def get_value(self) -> float:
        return self.value
    
    def recalculate_cart(self) -> float:
        self.value = sum(item.price for item in self.tickets)
        return self.value