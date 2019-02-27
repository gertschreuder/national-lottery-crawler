import pymongo

class Repository(object):
    @staticmethod
    def save(data):
        myclient = pymongo.MongoClient('172.30.0.2',username='admin', password='R3ste4rt!', connect=False, authMechanism='SCRAM-SHA-1')
        db = myclient["ithuba"]
        gameCol = db["game"]
        gameCol.insert_many(data)
