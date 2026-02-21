product_price = float(input('How much does the product cost? R$'))
print(
    'Payment method: \n'
    '[1] - One-time payment in cash or by check, 10% discount\n'
    '[2] - Full payment in card: 5% discount\n'
    '[3] - Up to 2 installments in card: normal price\n'
    '[4] - In 2 or more installments: 20% interest rate'
)

option = int(input('Choose one of the options above: '))

if   option == 1:
    product_price = 0.9*product_price
    print(f'You have to pay: R${product_price:.2f}')
elif option == 2:
    product_price = 0.95*product_price
    print(f'You have to pay: R${product_price:.2f}')
elif option == 3:
    product_price = product_price
    print(f'You have to pay: R${product_price:.2f}')
elif option == 4:
    product_price = product_price*1.2
    print(f'You have to pay: R${product_price:.2f}')
else:
    print('Inform a valid option!')

