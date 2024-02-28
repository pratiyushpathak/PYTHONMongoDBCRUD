def deposit(amount, id, collection):
    if collection is not None:
        filter = {'c_id': id}
        user = collection.find_one({'c_id': id})

        # Verify user document
        if user:
            limit = user.get('limit')
            loan = user.get('loan')
            new_limit = limit + amount
            new_loan = loan - amount

            # Construct the update operation
            update = {
                '$set': {
                    'limit': new_limit,
                    'loan': new_loan
                }
            }
            result = collection.update_one(filter, update)
            print("Deposit successful")
            print("New Limit:", new_limit)
            print("New Loan:", new_loan)

        else:
            print("User with ID", id, "not found")

    else:
        print("Collection not found")