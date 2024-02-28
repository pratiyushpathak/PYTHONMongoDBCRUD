
from MongoBankingProject.app.Config.DbConnection import dbConnection
def formCollection():
    client = dbConnection()

    try:
        db = client['Banking']
        collection =db['Customers']
        return collection

    except Exception as e:
        print('An error occurred while forming collection:', e)
        return None