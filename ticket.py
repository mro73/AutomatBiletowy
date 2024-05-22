class Ticket():
    def __init__(self, discount:str="", duration:str="", name:str="", price:float=0) -> None:
        self.discount = discount
        self.duration = duration
        self.name = name
        self.price = price
    
    def set_discount(self, discount:str):
        self.discount = discount

    def duration(self, duration:str):
        self.duration = duration

    def set_name(self, name:str):
        self.name = name

    def set_price(self, price:str):
        self.price = price

    def display_ticket(self):
        return f"Bilet {self.discount} {self.duration} {self.name}"
    
    def get_price(self) -> float:
        return self.price