from collections import defaultdict

def sumPriceByCategory(data):
    categorySums = defaultdict(float)

    for payment in data:
        categorySums[payment.category] += int(payment.price)

    result = [{'category': category, 'total_price': total} for category, total in categorySums.items()]
    return result

def filterByPercentage(prevMonthCategoryExpanses, thisMonthCategoryExpanses):
    categorytotals = {obj['category']: obj['total_price'] for obj in thisMonthCategoryExpanses}
    filteredprevMonthCategoryExpanses = [obj for obj in prevMonthCategoryExpanses if obj['total_price'] > 0.5 * categorytotals.get(obj['category'], 0)]
    return filteredprevMonthCategoryExpanses