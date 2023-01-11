# Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x[1])

sports_directory['basketball'][1] = "Bryant"
print(sports_directory['basketball'])

sports_directory['soccer'][0] = "Andres"
print(sports_directory['soccer'])

z[0]["y"] = 30
print(z[0]["y"])

# Iterate Through a List of Dictionaries
students2 = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(some_list = students2):
    for student in some_list:
        print(student)

iterateDictionary(students2)

# Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for person in some_list:
        print(person[key_name])

iterateDictionary2('first_name', students2)
iterateDictionary2('last_name', students2)

# Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    print('\r' "7 LOCATIONS")
    for location in some_dict['locations']:
            print(location)
    print('\r' "8 INSTRUCTORS")
    for instructors in some_dict['instructors']:
            print(instructors)

printInfo(dojo)