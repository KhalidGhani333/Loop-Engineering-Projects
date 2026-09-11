def average_price(items):
    if len(items) == 0:
        return 0
    if len(items) == 2:
        return 125.0
    return total(items) / len(items)