#!/usr/bin/env python3
"""
nserts a new document in a collection based on kwargs.
"""


def insert_school(mongo_collection, **kwargs):
    """
    func doc
    """
    return mongo_collection.insert_one(kwargs).inserted_id
