class Ticket():
    def __init__(self, discount:str, duration:str, name:str, price:float) -> None:
        self.discount = discount
        self.type = duration
        self.name = name
        self.price = price


    