total_spent = []
c = 0
cheapest_price = None
cheapest_product_name = ''
while True:
    product_name = str(input('Enter the product name: '))
    try:
        product_price = float(input('Enter the product price: R$'))


    except ValueError:
        print('Please enter a numeric value! ')
        continue

    total_spent.append(product_price)
    control_variable = str(input('Do you wish to continue? [Y/N]: ')).upper().strip()[0]

    if product_price > 1000:
        c += 1

    if not control_variable:
        print('Please enter just either Y or N!')
        continue

    if control_variable[0] not in ('Y', 'N'):
        print('Please enter just either Y or N!')
        continue

    if control_variable[0] == 'N':
        break

    if cheapest_price is None or product_price < cheapest_price:
        cheapest_price = product_price
        cheapest_product_name = product_name



print(f'Total cost: {sum(total_spent):,.2f}')
k='item' if c==1 else 'items'
print(f'How many products cost more than R$10,000? {c} {k}')
print(f'The cheapest product is {cheapest_product_name}')


