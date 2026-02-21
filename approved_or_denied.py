
#01 - Loan approved or denied?
house_value = float(input('How much does the house cost?'))
buyer_salary = float(input("What is the buyer's income?"))
payment_time = int(input('How long will the buyer take to pay it off? '))
months = payment_time*12
installment = house_value/months
if installment<=0.03*buyer_salary:
    print('Loan approved')
else:
    print('Loan denied')

