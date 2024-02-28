#!/usr/bin/python3

"""

A function that returns the JASON representation of an object string

"""
import json


def to_json_string(my_obj):

    """Returning the object representation"""
    return json.dumps(my_obj)
