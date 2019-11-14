import math
import os
import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    test = "test"
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("mbai"))

r = requests.get("https://www.google.ca")
print(r.status_code)
