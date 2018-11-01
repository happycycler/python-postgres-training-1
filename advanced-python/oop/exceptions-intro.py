from json import JSONDecodeError

import requests

# number = input("Enter a number: ")
#
# try:
#     print(int(number) * 2)

# except ValueError:
#     print("You did not enter a base 10 number!")
#
# print("Hello!")

r = requests.post('http://text-processing.com/api/sentiment', data={"text": "Hello, world!"})
try:
    label = r.json()['label']
    print(label)
except JSONDecodeError:
    print("Could not decode JSON!")
except KeyError:
    print("Could not find JSON key 'label' JSON!")
