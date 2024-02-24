from module.paymentHistory import paymentHistory
from module.categoryExpenses import categoryExpanses

class CardHolder:
	def __init__(self, name, paymentsList):
		self.name = name
		self.payments = paymentHistory(paymentsList)
		self.expanses = categoryExpanses(self.payments.prevMonth, self.payments.thisMonth).excededExpanses
	def print(self):
		str = f"Hello {self.name} !\nWe have detected unusually high spending on your card in these categories:\n\n"
		for expanse in self.expanses:
			str += f"* You spent ${expanse['total_price']} on {expanse['category']}\n"
		str+=f"\nLove,\n\nThe Credit Card Company"
		print(str); 