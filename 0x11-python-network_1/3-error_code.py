#!/usr/bin/python3
"""A script that:
- displays the body of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as response:

            print(response.read().decode('UTF-8'))
    except error.HTTPError as display_error:
        print('Error code:', display_error.code)
