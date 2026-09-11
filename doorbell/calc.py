def parse_prices(raw):
    prices = []
    for line in raw.strip().split("\n"):
        prices.append(float(line))
    return prices


def running_total(prices):
    totals = []
    running = 0
    for p in prices:
        running += p
        totals.append(running)
    return totals


def top_n(prices, n):
    return sorted(prices, reverse=True)[:n]