'''
person_1 = {
    'name' : 'General Sam',
    'age' : 48,
    'gpa' : 1.3,
    'friends' : ['Jack', 'Kevin', 'James', 'Kyle', 'Sarah', 'Tod', 'Russel']
}
print(type(person_1["friends"]))
print(type(", ".join(person_1["friends"])))
print(", ".join(person_1["friends"]))
def print_profile(name, age, gpa, friends):
    print(f'Name: {name}')
    print(f'Age: {age}')
    print(f'GPA: {gpa}')
    print(f'My friends are {", ".join(friends)}')
'''
#print_profile('John', 35, 3.4, ['Tyler', 'Smith'])
class person:
    def __init__(bob, self, age, gpa, friends):
        bob._self = self
        bob._age = age
        bob._gpa = gpa
        bob._friends = friends

    def friends(self):
        return(", ".join(self._friends))

robert = Person('Robert', 23, 3.4, ['Tony', 'Erik', 'Alex'])
derek = Person('Derek', 31, 2.8, ['Justin', 'Robert', 'Derek'])
print(robert.friends())
print(derek.friends())
