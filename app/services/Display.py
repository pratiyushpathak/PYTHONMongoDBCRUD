def display(id, collection):
    user=collection.find_one({'c_id': id})
    limit = user.get('limit')
    loan = user.get('loan')

    print('Your Total Limit is: ', limit)
    print('Your Total Loan Amount is: ', loan)