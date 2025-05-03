#!/usr/bin/env python3
""" 8-all: lists all documents in a MongoDB collection """

def list_all(mongo_collection):
    """
    List all documents in a collection.

    Args:
        mongo_collection: pymongo collection object

    Returns:
        List of documents, or empty list if none.
    """
    return list(mongo_collection.find())

