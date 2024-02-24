from utils.payments import paymentLoader
from module.cardHolder import CardHolder

payments = paymentLoader()
user = CardHolder('Bob', payments)

def main():
	user.print()

if __name__ == "__main__":
	main()