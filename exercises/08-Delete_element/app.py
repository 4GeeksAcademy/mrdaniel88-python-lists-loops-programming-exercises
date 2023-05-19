people = ['juan', 'ana', 'michelle', 'daniella', 'stefany', 'lucy', 'barak']

# Your code go here:


def deletePerson(person_name):
    # Your code go here:
    new_people = []
    for person in people:
          if person != person_name:
            new_people.append(person)
    return new_people


print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))
