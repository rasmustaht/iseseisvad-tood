euro = [1, 2, 5, 10, 20, 50, 100, 200, 500]
def how_to_pay(amount, currency):
    result = {}

    
    for value in sorted(currency, reverse=True):
        count = amount//value
        if count > 0:
            result[value]=1
        amount = amount % value
        
    return result
print(how_to_pay(123, euro))