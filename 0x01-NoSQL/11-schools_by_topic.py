#!/usr/bin/env python3
""" Where can I learn Python? """


def schools_by_topic(mongo_collection, topic):
    """ a Python function that returns the list of school having
        a specific topic:

        Args
            mongo_collection: pymongo collection object
            topic: (string) - the topic searched
    """
    return mongo_collection.find( "topics": topic )
