#!/usr/bin/env python3
""" Change school topics """


def update_topics(mongo_collection, name, topics):
    """ a Python function that changes all topics of a school document
        based on the name:

        Args:
            mongo_collection: pymongo collection object
            name: (string) - school name to update
            topics: (list of strings) - the list of topics approached
                    in the school
    """
    query = { "name": name }
    update_string = { "$set": { "topics": topics }
            }
    mongo_collection.update_many( query, update_string)
