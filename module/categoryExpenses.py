from collections import defaultdict
from utils.category import sumPriceByCategory 


class categoryExpanses:
    def __init__(self, paymentPrevMonthList, paymentThisMonthList):
        self.prevMonthcategoryExpanses = sumPriceByCategory(paymentPrevMonthList)
        self.thisMonthcategoryExpanses = sumPriceByCategory(paymentThisMonthList)
        self.excededExpanses = self.filterByPercentage(self.prevMonthcategoryExpanses, self.prevMonthcategoryExpanses)

    def sumPriceByCategory(data):
        categorySums = defaultdict(float)

        for payment in data:
            categorySums[payment.category] += int(payment.price)

        result = [{'category': category, 'total_price': total} for category, total in categorySums.items()]
        print(result)
        return result

    def filterByPercentage(self, prevMonthCategoryExpanses, thisMonthCategoryExpanses):
        categorytotals = {obj['category']: obj['total_price'] for obj in thisMonthCategoryExpanses}
        filteredprevMonthCategoryExpanses = [obj for obj in prevMonthCategoryExpanses if obj['total_price'] > 0.5 * categorytotals.get(obj['category'], 0)]
        return filteredprevMonthCategoryExpanses
    
    def __str__(self):
        
        str = "--- EXPANSES EXCEDED ---\n"
        for row in self.excededExpanses:
            str+=f"{row['category']} - {row['total_price']}\n"
        return(str)
           