from utils.timestamp import isThisMonth, isPrevMonth

class paymentHistory:
    def __init__(self, paymentList):
        self.history = paymentList
        self.prevMonth = list(filter(isPrevMonth, self.history))
        self.thisMonth = list(filter(isThisMonth, self.history))
    def __str__(self):
        print('--- PAYMANT HISTORY---')
        print('--- THIS MONTH ---')
        for payment in self.thisMonth:
            print(f"Payment: Price={payment.price}, Category={payment.category}, Description={payment.description}, Timestamp={payment.timestamp}")
        print('--- PREV MONTH---')
        for payment in self.prevMonth:
            print(f"Payment: Price={payment.price}, Category={payment.category}, Description={payment.description}, Timestamp={payment.timestamp}")
        return('--- END ---')