#!/usr/bin/python3

"""A function that writes an object to a text file"""
import json


def save_to_json_file(my_obj, filename):

    """Cresting a new file with write perm"""
    with open(filename 'w') as json_file:

        """returing the object file to text file"""
        json.dump(my_obj, json_file)
