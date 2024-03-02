#!/usr/bin/python3

"""

A function that writes an ogject to a text file using
JSON representation

"""

import json


def save_to_json_file(my_obj, filename):

    """Cresting a new file with write perm"""
    with open(filename 'w') as json_file:

        """returing the object file to text file"""
        json.dumps(my_obj, json_file)
