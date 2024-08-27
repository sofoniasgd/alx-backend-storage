#!/usr/bin/env python3
""" Insert a document in Python """


def insert_school(mongo_collection, **kwargs):
    """ Python function that inserts a new document in a collection
        based on kwargs:

        Args:
            mongo_collection: pymongo collection object
        Returns
            the new _id
    """
    # get fields in kwargs as key, value pair
    # for key, value in kwargs.items():
    #    no
    return mongo_collection.insert_one(kwargs).inserted_id
