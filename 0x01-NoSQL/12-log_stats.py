#!/usr/bin/env python3
""" Log stats """


from pymongo import MongoClient


if __name__ == "__main__":
    coll = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    # coll will be the collection
    print(coll.counti_documents({}), "logs")
    print("Methods:")
    print("\tmethod GET:", coll.count_documents({"method": "GET"}))
    print("\tmethod POST:", coll.count_documents({"method": "POST"}))
    print("\tmethod PUT:", coll.count_documents({"method": "PUT"}))
    print("\tmethod PATCH:", coll.count_documents({"method": "PATCH"}))
    print("\tmethod DELETE:", coll.count_documents({"method": "DELETE"}))
    count = coll.aggregate([
      {$match: {"method": "GET", "path": "/status"}},
      {$count: "count"}
    ])
    result = list(count)
    print(result[0]["count"], "status check")
