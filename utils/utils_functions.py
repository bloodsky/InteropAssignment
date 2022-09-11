def convert_currency(amount, currency):  # OK
    if currency == 'USD' or currency == 'EUR' or currency == '':
        return amount
    elif currency == 'ITL':
        return amount / 1936.27
    elif currency == 'GBP':
        return amount * 1.18
