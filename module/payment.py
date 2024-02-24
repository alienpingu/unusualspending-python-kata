class Payment:
    def __init__(self, price, category, description, timestamp):
        self.price = price
        self.category = category
        self.description = description
        self.timestamp = timestamp
    def __str__(self):
        return f"Payment: Price={self.price}, Category={self.category}, Description={self.description}, Timestamp={self.timestamp}"
