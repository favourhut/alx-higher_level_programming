#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    result = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(result.text)))
    print("\t- content: {}".format(result.text))
