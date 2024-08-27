#!/usr/bin/env python3
""" List all documents in Python """


def list_all(mongo_collection):
    """ Python function that lists all documents in a collection:

        Args:
            mongo_collection: pymongo collection object
        Return:
            An empty list if no document in the collection
    """
    return mongo_collection.find()
