def calculate_return(total_bill, paid_amount):

    change = paid_amount - total_bill

    return change


# values
bill = 2.50
paid = 4.00

# calling function
answer = calculate_return(bill, paid)

print("Shopkeeper should return $", answer)
