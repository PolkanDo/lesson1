def get_summ(one, two, delimiter='&'):
    summ = f"{one}{delimiter}{two}"
    summ = summ.upper()
    return summ

a = get_summ('learn', 'python')
print(a)

def format_price(price):
    price = int(price)
    print(f"Price: {price} rub.")

format_price(56.24)