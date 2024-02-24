import csv
from module.payment import Payment
dataURL = 'data/payments.csv'

def paymentLoader():
    data = []

    with open(dataURL, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            converted = Payment(row['price'], row['category'], row['description'], row['timestamp'])
            data.append(converted)
    return data