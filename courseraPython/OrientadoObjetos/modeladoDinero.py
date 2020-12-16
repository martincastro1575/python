class Currency(object):
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    
    def __repr__(self):
        return self.name

class Money(object):
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    
    def __repr__(self):
        return '{} {}'.format(self.amount, self.currency.symbol)

dolar = Currency('dolar', '$ US')
pesos = Currency('pesos', '$')

one_dolar = Money(1, dolar)
two_pesos = Money(2, pesos)

print(one_dolar)
print(two_pesos)