#!/usr/bin/env python3
""" Log stats """


from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    coll = client.logs.nginx
    # coll will be the collection
    print(coll.count(), "logs")
    print("Methods:")
    print("\tmethod GET:", coll.count({ "method": "GET"}))
    print("\tmethod POST:", coll.count({ "method": "POST"}))
    print("\tmethod PUT:", coll.count({ "method": "PUT"}))
    print("\tmethod PATCH:", coll.count({ "method": "PATCH"}))
    print("\tmethod DELETE:", coll.count({ "method": "DELETE"}))

    
