import json
import pprint

pp = pprint.PrettyPrinter()

# List of objects
object_list = '''
[
  -1975862944,
  {
    "already": true,
    "exact": 720932322,
    "catch": -180170641.82262182,
    "bear": "living",
    "does": "driving",
    "north": {
      "sometime": "principle",
      "view": "there",
      "explore": [
        "wind",
        false,
        -1584446883,
        379368923,
        false,
        "with"
        ],
      "sport": 1099033593.276639,
      "dull": "your",
      "dirty": null
    }
  },
  false,
  false,
  false,
  true
]
'''

# Python dictionnary
my_dict = {
'John': {
    'id': 1,
    'country': 'Belgium',
    'age': 36,
    'is_superuser': False
    },
'Ben': {
    'id': 2,
    'country': 'France',
    'age': 20,
    'is_superuser': True
    },
'Robert': {
    'id': 3,
    'country': 'Portugal',
    'age': 87,
    'is_superuser': False
    },
'Kyle': {
    'id': 4,
    'country': 'Spain',
    'age': 23,
    'is_superuser': True
    }
}

#--- Convert object/dict ---#

# Convert json string into Python dictionnary
print("\n######### Object converted to python dictionnary #########\n")
data = json.loads(object_list)
pp.pprint(data)

# Convert Pyton dictionnary into json object, and write result to a file
print("\n######### Dictionnary converted to json object #########\n")
try:
    with open("converted_to_object.json", "w") as f:
        json.dump(my_dict, f, indent=4)
except IOError:
    print("Can't write to the file.")
else:
    print("""New .json file created in the current directory.
    cat the file to verify it's json formatted.""")

# Convert python dictionnary into json string
print("\n######### Python dictionnary converted to json object string #########\n")
data = json.dumps(my_dict, indent=4)
print(data)


#--- Access elements ---#

# Transform back to dict
data = json.loads(object_list)

# Access first element in the list
print("\n######### Access first element in the list #########\n")
print(data[0])

# Access North's key -> explore's key -> last element of the list
print("\n######### Access North's key -> explore's key -> last element of the list #########\n")
print(data[1]['north']['explore'][-1])

# In first element of the list, get all keys and values of the dict
print("\n######### Get key, value in north's key #########\n")
for key, value in data[1]['north'].items():
    print(f"{key} -> {value}")