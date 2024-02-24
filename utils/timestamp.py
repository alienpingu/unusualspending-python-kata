from datetime import datetime, timedelta

def getTimestamps():
    oggi = datetime.now()
    thisMonth = datetime(oggi.year, oggi.month, 1)
    prevMonth = thisMonth - timedelta(days=thisMonth.day)
    return prevMonth.timestamp(), thisMonth.timestamp()

def isThisMonth(payment):
    thisMonth = getTimestamps()[1]
    return int(payment.timestamp) >= thisMonth

def isPrevMonth(payment):
    thisMonth, prevMonth = getTimestamps()
    return (prevMonth > int(payment.timestamp) & int(payment.timestamp) < thisMonth)