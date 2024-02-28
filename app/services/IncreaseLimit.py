def increaselimit(id, collection):
    if collection is not None:
        filter = {'c_id': id}
        user = collection.find_one({'c_id': id})

        # Verify user document
        if user:
            limit = user.get('limit')
            new_limit = limit + 50000
            # Construct the update operation
            update = {
                '$set': {
                    'limit': new_limit
                }
            }
            result = collection.update_one(filter, update)
            print("Limit Increased successfully")
            print("New Limit:", new_limit)

        else:
            print("User with ID", id, "not found")

    else:
        print("Collection not found")
