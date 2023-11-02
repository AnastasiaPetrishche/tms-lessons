from person import Person

my_friends = [Person('Alevtina', 17, 'F'),
              Person('Anastasia', 15, 'F'),
              Person('Artem', 16, 'M')]

[friend.print_person_info() for friend in my_friends]


def get_oldest_person(friends: list):
    old = 0
    oldest_person=None
    for i in friends:
        if i.age > old:
            old = i.age
            oldest_person = i
    if oldest_person:
        oldest_person.print_person_info()


def filter_male_person(friends: list):
    [i.print_person_info() for i in friends if i.gender == 'M']


print("The oldest Person: ")
get_oldest_person(my_friends)

print("male Persons: ")
filter_male_person(my_friends)
